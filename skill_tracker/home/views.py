from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from .forms import SkillForm, CheckpointForm
from .models import Skill, Checkpoint
from django.forms import modelformset_factory

checkformset = modelformset_factory(Checkpoint, fields=('completed',), extra=0)

def index(request):
    return render(request, 'index.html')

class signUpView(generic.CreateView): 
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        skills = Skill.objects.filter(user=request.user)
    else:
        skills = []
    return render(request, 'home.html', {'skills': skills})

@login_required
def addSkill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            new_skill = form.save(commit=False)
            new_skill.user = request.user
            new_skill.save()
            return redirect('home')
    else:
        form = SkillForm()
    return render(request, 'add_skill.html', {'form': form})


@login_required
def skills(request, sk):
    skill = get_object_or_404(Skill, name=sk, user=request.user)
    checkpoints = Checkpoint.objects.filter(skill=skill)
    total_count = checkpoints.count()
    completed_count = checkpoints.filter(completed=True).count()
    #forms
    form = CheckpointForm()
    formset = checkformset(queryset=checkpoints)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add_checkpoint':
            form = CheckpointForm(request.POST)
            if form.is_valid():
                new_checkpoint = form.save(commit=False)
                new_checkpoint.skill = skill
                new_checkpoint.save()
                return redirect("skills", sk=sk)
        elif action == 'update_checkpoints':
            formset = checkformset(request.POST, queryset=checkpoints)
            if formset.is_valid():
                formset.save()
                return redirect("skills", sk=sk)

    return render(request, 'openskill.html', {
        'skill': skill,
        'checkpoints': checkpoints,
        'form': form,
        'total_count': total_count,
        'completed_count': completed_count,
        'formset': formset
    })

@login_required
def deleteSkill(request, sk):
    skill = get_object_or_404(Skill, name=sk, user=request.user)
    if request.method == 'POST':
        skill.delete()
        return redirect('home')
    return render(request, 'delete_skill.html', {'skill': skill})
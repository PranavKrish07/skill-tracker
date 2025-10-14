from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from .forms import SkillForm, CheckpointForm
from .models import Skill, Checkpoint

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
    if request.method == 'POST':
        form = CheckpointForm(request.POST)
        if form.is_valid():
            new_checkpoint = form.save(commit=False)
            new_checkpoint.user = request.user
            new_checkpoint.skill = skill  
            new_checkpoint.save()
            return redirect("skills", sk=sk)
    else:
        form = CheckpointForm()
    return render(request, 'openskill.html', {'skill': skill, "checkpoints": checkpoints, "form": form, "total_count": total_count, "completed_count": completed_count})

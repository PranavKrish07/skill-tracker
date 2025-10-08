from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from .forms import SkillForm
from .models import Skill

def index(request):
    return render(request, 'index.html')

class signUpView(generic.CreateView): 
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def home(request):
    skills = Skill.objects.filter(user=request.user)
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
    return render(request, 'openskill.html', {'skill':skill})

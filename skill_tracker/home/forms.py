from django import forms
from .models import Skill, Checkpoint

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']
    
class CheckpointForm(forms.ModelForm):
    class Meta:
        model = Checkpoint
        fields = ['name', 'completed']
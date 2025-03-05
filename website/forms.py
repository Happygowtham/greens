# forms.py
from django import forms
from .models import Gallery, Activity

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['description', 'image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['description', 'image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }
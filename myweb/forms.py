from django import forms
from .models import register
 
class reg(forms.ModelForm):
 class Meta:
   model=register
   fields=('username','password','name','email','mobile')

 

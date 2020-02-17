from django import forms
from .models import ImageUploadModel

#1. hard code html: form, input, label, button..
#2. forms.Form: 양식(Form class)안에 받아들일 필드 선언
#3. forms.ModelForm: Model class 안에 받아들일 필드를 선언하고 해당 클래스를 당겨와 활용

class SimpleUploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    image = forms.ImageField()

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUploadModel
        fields = ('description', 'document',)

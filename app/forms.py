from django import forms
from .models import Car
from captcha.fields import CaptchaField

class CarForm(forms.ModelForm):
    captcha = CaptchaField(label='Введите текст с картинки', error_messages={'invalid':'Неправильный текст'})
    
    class Meta:
        model = Car
        fields = ('brand_name', 'model_name','captcha')

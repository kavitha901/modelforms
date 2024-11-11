from django import forms
from app.models import *


class TopicmodelForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'


class WebpagemodelForm(forms.ModelForm):
    class Meta:
        model=Webpage
        #fields='__all__'
        fields=['name','topic_name','url']
        labels={'name':'Name'}
        #widgets={'url':forms.PasswordInput}
        exclude=['email']
        help_texts={'topic_name':'this is parent col'}
from django.forms import ModelForm, Textarea, TextInput
from MainApp.models import Snippet


class SnippetForm(ModelForm):
   class Meta:
        model = Snippet
       # Описываем поля, которые будем заполнять в форме
        fields = ['name', 'is_public', 'lang', 'code']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Название сниппета'}),
            'code': Textarea(attrs={'placeholder': 'Код сниппета'})
        }
        labels = {
            'name': '', 'is_public': '', 'lang': '', 'code': ''
        }



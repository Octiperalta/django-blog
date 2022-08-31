from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')

        widgets = {
            "name": forms.TextInput(),
            "email": forms.TextInput(),
            "content": forms.Textarea()
        }

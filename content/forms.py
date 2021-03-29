from django import forms
from content.models import Content


class ContentForm(forms.ModelForm):
    """Form post."""
    class Meta:
        model = Content
        fields = ["title", "text", "videofile"]
        help_texts = {
            "text": ("Напишите текст"),
            "title": ("Напишите заголовок"),
            "videofile":("Загрузите видео")
        }

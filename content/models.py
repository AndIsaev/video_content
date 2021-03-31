from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Content(models.Model):
    """Model for posts."""
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts", verbose_name="Автор")
    title = models.CharField("Название", max_length=120)
    text = models.TextField("Текст", max_length=400)
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    videofile = models.FileField("Видео", upload_to='videos/')

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return f"{self.author} ({self.title}) ({self.text})"

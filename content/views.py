from django.urls import reverse
from django.views.generic import ListView, CreateView
from .models import Content
from .forms import ContentForm


class CreateNewPost(CreateView):
    """Create new post."""
    model = Content
    form_class = ContentForm
    template_name = "new.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("index")


class IndexView(ListView):
    """Main page."""
    model = Content
    template_name = "index.html"
    context_object_name = "posts"

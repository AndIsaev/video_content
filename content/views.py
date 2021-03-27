from django.shortcuts import render
from .models import Content
from .forms import ContentForm


# def new_post(request):
#     lastvideo = Content.objects.last()
#
#     videofile = lastvideo.videofile
#
#     form = ContentForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#
#     context = {'videofile': videofile,
#                'form': form
#                }
#
#     return render(request, 'new.html', context)


def index(request):
    posts = Content.objects.all()
    return render(
        request,
        "index.html",
        {"posts": posts})
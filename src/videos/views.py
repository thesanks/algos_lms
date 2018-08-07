from django.shortcuts import render
from django.views.generic import (
            CreateView,
            DetailView,
            ListView,
            UpdateView,
            DeleteView
        )

from .models import Video

class VideoCreateView(CreateView):
    queryset = Video.objects.all()

class VideoDetailView(DetailView):
    queryset = Video.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(VideoDetailView, self).get_context_data(*args, **kwargs)
        return context

class VideoListView(ListView):
    queryset = Video.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(VideoListView, self).get_context_data(*args, **kwargs)
        return context

class VideoUpdateView(UpdateView):
    queryset = Video.objects.all()

class VideoDeleteView(DeleteView):
    queryset = Video.objects.all()

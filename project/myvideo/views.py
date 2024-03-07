from django.shortcuts import render, get_object_or_404, redirect
from .models import Video
from .forms import VideoForm

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

def watch_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'watch.html', {'video': video})

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})

def edit_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm(instance=video)
    return render(request, 'edit_video.html', {'form': form})

def delete_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        video.delete()
        return redirect('video_list')
    return render(request, 'delete_video.html', {'video': video})
from django.shortcuts import render, get_object_or_404, redirect

from warcraftapp.forms import ScreenshotsCreateModelForm, AudioCreateModelForm, VideoCreateModelForm
from warcraftapp.models import Game, Screenshots, Audio, Category, Video


def start_view(request):
    return render(request, 'warcraftapp/start.html')

def about_game_view(request):
    game = Game.objects.all()
    context = {
        'game': game,

    }
    return render(request, 'warcraftapp/about_game.html', context)

def screenshots_view(request):
    context = {
        'screenshots': Screenshots.objects.all()
    }
    return render(request, 'warcraftapp/screenshots.html', context)




def audio_view(request):

    category = None
    audios = None

    if 'category' in request.GET:
        category = get_object_or_404(Category, pk=request.GET['category'])
        audios = Audio.objects.filter(category=category)

    context = {
        'categories': Category.objects.filter(name__in=['music','character replicas']),
        'audios': audios
    }

    return render(request, 'warcraftapp/audio.html', context)


def video_view(request):

    category = None
    videos = None

    if 'category' in request.GET:
        category = get_object_or_404(Category, pk=request.GET['category'])
        videos = Video.objects.filter(category=category)

    context = {
        'categories': Category.objects.filter(name__in=['gameplay','game video']),
        'videos': videos
    }

    return render(request, 'warcraftapp/video.html', context)


def create_view(request):
    form = ScreenshotsCreateModelForm()
    return render(request, 'warcraftapp/create.html', {'forn': form})
def create_screenshots_view(request):
    form = ScreenshotsCreateModelForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ScreenshotsCreateModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('screenshots')
        context['form'] = form
    return render(request, 'warcraftapp/createscreenshot.html', context)


def create_audio_view(request):
    form1 = AudioCreateModelForm()
    context = {'form1': form1}

    if request.method == 'POST':
        form1 = AudioCreateModelForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect('audio')
        context['form1'] = form1
    return render(request, 'warcraftapp/createaudio.html', context)

def create_video_view(request):
    form = VideoCreateModelForm()
    context = {'form': form}

    if request.method == 'POST':
        form = VideoCreateModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('video')
    return render(request, 'warcraftapp/createvideo.html', context)

# def create_view(request):
#
#     form1 = ScreenshotsCreateModelForm()
#     form2 = AudioCreateModelForm()
#     form3 = VideoCreateModelForm()
#     context = {}
#
#     if request.method == 'POST':
#         form1 = ScreenshotsCreateModelForm(request.POST, request.FILES)
#         if form1.is_valid():
#             form1.save()
#             return redirect('screenshots')
#     elif request.method == 'POST':
#         form2 = AudioCreateModelForm(request.POST, request.FILES)
#         if form2.is_valid():
#             form2.save()
#             return redirect('audio')
#     elif request.method == 'POST':
#         form3 = VideoCreateModelForm(request.POST, request.FILES)
#         if form3.is_valid():
#             form3.save()
#             return redirect('video')
#     else:
#
#         context['form1'] = form1
#         context['form2'] = form2
#         context['form3'] = form3
#         return render(request, 'warcraftapp/create.html', context)
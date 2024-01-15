from django.urls import path
from .views import start_view, about_game_view, screenshots_view, audio_view, video_view, create_screenshots_view, \
    create_audio_view, create_view, create_video_view

urlpatterns = [
    path('', start_view, name='start'),
    path('about-game/', about_game_view, name='about_game'),
    path('screenshots/', screenshots_view, name='screenshots'),
    path('audio/', audio_view, name='audio'),
    path('video/', video_view, name='video'),
    path('create/', create_view, name='create'),
    path('create-screenshots/', create_screenshots_view, name='create_screenshots'),
    path('create-audio/', create_audio_view, name='create_audio'),
    path('create-video/', create_video_view, name='create_video'),
]

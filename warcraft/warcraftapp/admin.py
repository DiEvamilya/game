from django.contrib import admin

from warcraftapp.models import Game, Screenshots, Audio, Category, Video

admin.site.register(Game)
admin.site.register(Screenshots)
admin.site.register(Audio)
admin.site.register(Category)
admin.site.register(Video)
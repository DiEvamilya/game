
from django import forms


from warcraftapp.models import Screenshots, Audio, Video


class ScreenshotsCreateModelForm(forms.ModelForm):
    class Meta:
        model = Screenshots
        exclude = ('slug',)
        fields = ('image', 'title')
class AudioCreateModelForm(forms.ModelForm):
    class Meta:
        model = Audio
        exclude = ('slug',)


class VideoCreateModelForm(forms.ModelForm):
    class Meta:
        model = Video
        exclude = ('slug',)

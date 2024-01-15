from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return f'{self.name}'
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f'{self.name}')
        return super().save()

class Game(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f'{self.title}'

class Screenshots(models.Model):
    image = models.ImageField(upload_to='images/',
                              null=True,
                              blank=True,)
    title = models.CharField(max_length=255, primary_key=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f'{self.title}')
        return super().save()


class Audio(models.Model):
    audio = models.FileField(upload_to='audio/',
                              null=True,
                              blank=True,)
    title = models.CharField(max_length=255, primary_key=True)
    category = models.ForeignKey(Category, max_length=255,
                                on_delete=models.DO_NOTHING)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f'{self.title}')
        return super().save()


class Video(models.Model):
    video = models.FileField(upload_to='video/',
                              null=True,
                              blank=True,)
    title = models.CharField(max_length=255, primary_key=True)
    category = models.ForeignKey(Category, max_length=255,
                                on_delete=models.DO_NOTHING,
                                related_name='category')
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f'{self.title}')
        return super().save()
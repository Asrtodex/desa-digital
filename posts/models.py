from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings

# Create your models here.
class Post(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete = models.CASCADE)
    title       = models.CharField(max_length = 50)
    slug        = models.SlugField(blank = True)
    content     = models.TextField()
    published   = models.BooleanField()
    created     = models.DateTimeField(auto_now_add = True)
    updated     = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',kwargs = {'slug':self.slug})

    def save(self, *args, **kwargs):
        self.slug   = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

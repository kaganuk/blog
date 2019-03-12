from django.conf import settings
from django.db import models
from django.utils import timezone


class PostQuerySet(models.QuerySet):
    def posts(self):
        return self.filter(publish_date__lte=timezone.now()).order_by('publish_date')


class PostManager(models.manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self.db)

    def posts(self):
        return self.get_queryset().posts()


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    publish_date = models.DateTimeField(blank=True, null=True)
    objects = PostManager()

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

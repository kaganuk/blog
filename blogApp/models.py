from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models import Q


class PostManager(models.Manager):
    def posts(self):
        """Returns posts ordered by publish_date"""
        condition = Q(publish_date__lte=timezone.now()) & Q(archive_date__isnull=True)
        return self.get_queryset().filter(condition).order_by('publish_date')

    def archived_posts(self):
        """Returns archived posts ordered by archive_date"""
        return self.get_queryset().filter(archive_date__isnull=False).order_by('archive_date')

    def search_posts(self, text):
        condition = Q(text__contains=text) | Q(title__contains=text)
        return self.get_queryset().filter(condition)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    publish_date = models.DateTimeField(blank=True, null=True)
    archive_date = models.DateTimeField(blank=True, null=True)
    objects = PostManager()

    def publish(self):
        """Updates publish_date"""
        self.publish_date = timezone.now()
        self.save()

    def archive(self):
        """Updates archive_date"""
        self.archive_date = timezone.now()
        self.save()

    def is_archived(self):
        """Returns archive state"""
        return self.archive_date is not None

    def __str__(self):
        return self.title

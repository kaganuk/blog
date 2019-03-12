from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models import Q


class PostQuerySet(models.QuerySet):
    def posts(self):
        return self.filter(Q(publish_date__lte=timezone.now()) & Q(archive_date__isnull=True)).order_by('publish_date')

    def archived_posts(self):
        return self.filter(archive_date__isnull=False).order_by('archive_date')


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def posts(self):
        return self.get_queryset().posts()

    def archived_posts(self):
        return self.get_queryset().archived_posts()


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    publish_date = models.DateTimeField(blank=True, null=True)
    archive_date = models.DateTimeField(blank=True, null=True)
    objects = PostManager()

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def archive(self):
        self.archive_date = timezone.now()
        self.save()

    def is_archived(self):
        return self.archive_date is not None

    def __str__(self):
        return self.title

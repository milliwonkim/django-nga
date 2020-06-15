from django.conf import settings
from django.db import models
from django. utils import timezone

class Front(models.Model):
    # 출발, 도착, 시간, 작성자, 내용, 제목
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    start = models.CharField(max_length=5) 
    dest = models.CharField(max_length=5)
    title = models.CharField(max_length=30)
    time = models.DateTimeField(default = timezone.now)
    body = models.TextField()


    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def summary(self):
        return self.body[:100]
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    created = models.DateTimeField()
    image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return '/project/{}/'.format(self.pk)
    
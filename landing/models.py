from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name

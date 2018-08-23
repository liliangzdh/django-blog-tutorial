from django.db import models

# Create your models here.


class Comments(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.name.join(":").join(self.text[:20])



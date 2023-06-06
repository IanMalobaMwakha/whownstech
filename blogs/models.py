from django.db import models

import blogs


class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    reading_time = models.CharField(max_length=10)
    cover_image_url = models.CharField(max_length=2083)





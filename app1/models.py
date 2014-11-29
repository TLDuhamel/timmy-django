from django.db import models

POST_TYPES = (
    ('T', 'Text'),
    ('P', 'Photo'),
    ('L', 'Link'),
)

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    type = models.CharField(max_length=1, choices=POST_TYPES)

    def __unicode__(self):
        return self.title

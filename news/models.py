from django.db import models


# Create your models here.
STATUS_CHOICES = (
    ('E', 'Edit'),
    ('P', 'Published'),
    ('D', 'Deleted'),
)
CATE_CHOICES = (
    ('sport', 'Sport News'),
    ('social', 'Social News'),
    ('economy', 'Economy News'),
    ('culture', 'Culture News'),
)


class news_model(models.Model):
    title = models.CharField(max_length=50, unique=True)
    pub_time = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    author = models.CharField(max_length=20)
    category = models.CharField(max_length=10, choices=CATE_CHOICES)
    article = models.TextField()
    like = models.PositiveIntegerField(blank=True, default=0)
    dislike = models.PositiveIntegerField(blank=True, default=0)

    class Meta:
        verbose_name = "Sohu news"
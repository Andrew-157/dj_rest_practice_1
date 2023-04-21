from django.db import models


class Story(models.Model):
    title = models.CharField(max_length=55)
    content = models.TextField()
    writer = models.ForeignKey(
        'auth.User', related_name='stories', on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    rating_choices = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
                      (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]
    content = models.TextField()
    writer = models.ForeignKey(
        'auth.User', related_name='reviews', on_delete=models.CASCADE
    )
    story = models.ForeignKey(
        'stories.Story', related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=rating_choices)
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.content

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

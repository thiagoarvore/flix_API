from django.db import models


NACIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil')
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nacionality = models.CharField(
        max_length=100,
        choices=NACIONALITY_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.

ROAST_CHOICES = (
    ("dark", "DARK"),
    ("medium", "MEDIUM"),
    ("light", "LIGHT"),
)


class User(models.Model):
    name = models.CharField(max_length=50, default="")
    fav_roast = models.CharField(max_length=6, choices=ROAST_CHOICES, default="Medium")
    brew_method = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name


class Coffee(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="coffees", null=True
    )
    name = models.CharField(max_length=50, default="")
    roast = models.CharField(max_length=50, default="")
    origin = models.CharField(max_length=50, default="")
    notes = models.TextField()
    brew_method = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name

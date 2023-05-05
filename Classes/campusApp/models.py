from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    campus_id = models.IntegerField()

    objects = models.Manager()

    class Meta:
        verbose_name = "University Campus"
        verbose_name_plural = "University Campuses"
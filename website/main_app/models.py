from django.db import models
from django.utils import timezone
from django.conf import settings


class Sport(models.Model):
    name = models.CharField(max_length = 55)

    def __str__(self):
        return self.name


class Active_game(models.Model):
    name = models.CharField(max_length=200)
    register_date = models.DateTimeField()
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField()
    place = models.CharField(max_length=200)
    description = models.TextField(null=True)
    sports = models.ManyToManyField(Sport)

    def __str__(self):
        return self.name


class Year(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Archive(models.Model):
    year =  models.DateTimeField()
    sport = models.CharField(max_length = 55)
    champion = models.CharField(max_length = 500)


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.faculty_name

    class Meta:
        verbose_name_plural = "Faculties"


class Participant(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    surname = models.CharField(max_length=30, blank=False, null=False)
    captain = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Captain")
    phone = models.CharField(max_length=20, blank=True, null=True)
    student_number = models.CharField(max_length=20, blank=False, null=False)
    year = models.ForeignKey(Year, blank=True, null=True, on_delete=models.PROTECT)
    sport_id = models.ForeignKey(Sport, on_delete=models.PROTECT, verbose_name="Sport type")

    def __str__(self):
        return "{} {}".format(self.name, self.surname)

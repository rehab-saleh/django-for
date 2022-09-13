from django.db import models

# Create your models here.
class Informations(models.Model):
    name = models.CharField(max_length=200, null=True)
    j_title = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email_1 = models.CharField(max_length=200, null=True)
    email_2 = models.CharField(max_length=200, null=True, blank=True)

    about_me = models.TextField(null=True)

    p_pic = models.ImageField(null=True)

    def __str__(self):

        return self.name


class Languages(models.Model):
    language_name = models.CharField(max_length=200, null=True)

    def __str__(self):

        return self.language_name

class Projects(models.Model):
    p_name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    brief_info = models.TextField(null=True)
    language_skilles = models.ManyToManyField(Languages)
    belonging = models.ForeignKey(Informations, null=True, on_delete=models.SET_NULL)

    def __str__(self):

        return self.p_name


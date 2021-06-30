from django.db import models

# Create your models here.


class Contact(models.Model):
    name        =models.CharField(max_length=120)
    email       =models.CharField(max_length=120)
    contact_no  =models.IntegerField(verbose_name='Contact no')
    message     =models.TextField(max_length=1000)

    def __str__(self):
        return str(self.name)

class Slider(models.Model):
    IMG     =models.ImageField(upload_to='slider')
    heading =models.CharField(max_length=999,null=True,blank=True)
    title   =models.CharField(max_length=9999,null=True,blank=True)
    order   =models.IntegerField()

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return str(self.IMG)

from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('APARTMENT','APARTMENT'),
    ('VILLA HOUSE','VILLA HOUSE'),
    ('PENTHOUSE','PENTHOUSE'),
    ('MORDERN CONDO','MORDERN CONDO')
)

class Category(models.Model):
    type = models.CharField(choices=CATEGORY_CHOICES, max_length=50)

    def __str__(self):
        return self.type


class Property(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    address = models.CharField(max_length=200)
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    area = models.IntegerField()
    floor = models.IntegerField()
    parking = models.IntegerField()
    image = models.FileField(upload_to = "images/")
    created_at = models.DateTimeField(auto_now_add=True)


class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=25)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    
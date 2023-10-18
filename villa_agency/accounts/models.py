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
    image = models.ImageField(upload_to = "images/")
    created_at = models.DateTimeField(auto_now_add=True)

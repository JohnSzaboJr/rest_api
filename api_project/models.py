from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
import sys

def validate_image(image):
    file_size = sys.getsizeof(image.file)
    limit_kb = 150
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb) 

class City(models.Model):
    # representation of an object in the database
    name = models.CharField(max_length=20, null=False)
    population = models.PositiveIntegerField(
        validators = [MinValueValidator(0)],
        null=False)
    photo = models.ImageField(
        upload_to='images/',
        max_length=100,
        null=True,
        blank=False,
        help_text="City Photo",
        verbose_name="City Photo",
        validators=[validate_image])
    owner = models.ForeignKey('auth.User',
        related_name='cities',
        on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

def __str__(self):
    # return a human readable representation of the object instance
    return "{} - {}".format(self.name, self.population, self.photo)

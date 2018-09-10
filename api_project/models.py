from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.core.validators\
import MinValueValidator, MaxValueValidator, RegexValidator
import sys

def validate_image(image):
    # setting max size on uploaded images
    file_size = sys.getsizeof(image.file)
    limit_kb = 150
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb) 

class City(models.Model):
    # representation of an object in the database

    validate_name = RegexValidator(r'^[A-Z][A-Za-z -]*$', \
    'City names have to be formatted properly (has to start with uppercase,\
    and can only include letters, and hyphens).')
    # setting accepted format for city names

    name = models.CharField(
        max_length=20,
        null=False,
        validators=[validate_name])
    population = models.PositiveIntegerField(
        validators = [MinValueValidator(0), MaxValueValidator(2147483647)],
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

# deleting image from database when entry is deleted
@receiver(post_delete, sender=City)
def submission_delete(sender, instance, **kwargs):
    instance.photo.delete(False)

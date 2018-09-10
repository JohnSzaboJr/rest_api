from django.contrib import admin
from .models import City

# registers the model to be editable on the admin interface
admin.site.register(City)

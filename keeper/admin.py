from django.contrib import admin
from keeper import models

# Register your models here.
admin.site.register(models.profile)
admin.site.register(models.password_store)
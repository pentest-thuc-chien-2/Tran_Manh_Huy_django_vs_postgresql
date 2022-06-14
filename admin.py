from django.contrib import admin
from .models import hospital
from .models import doctor

# Register your models here.
admin.site.register(hospital)
admin.site.register(doctor)

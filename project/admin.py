from django.contrib import admin
from .models import Category, Product, Subscriber
# Register your models here.
admin.site.register([Category, Product, Subscriber])
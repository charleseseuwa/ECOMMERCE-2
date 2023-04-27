from django.contrib import admin
from .models import Category, Product, Subscriber, Social
# Register your models here.
admin.site.register([Category, Product, Subscriber, Social])
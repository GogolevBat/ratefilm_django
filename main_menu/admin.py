from django.contrib import admin
from .models import Titles


admin.site.register(Titles)
# @admin.register(Titles) #  Современный способ регистрации с использованием декоратора
# class MyModelAdmin(admin.ModelAdmin):
#     list_display = ('title', 'rate')  # Поля, которые будут отображаться в списке
#     search_fields = ('title',)  # Поля, по которым можно осуществлять поиск
#     list_filter = ('title',)

from django.contrib import admin
from .models import Post  # импортирвали модель


class Blog_admin(
    admin.ModelAdmin):  # класс -редактор для дополнительных настроек представления модели в админке, это подкласс
    list_display = ['author', 'title', 'created_date', 'published_date']  # что отображать в админке
    list_display_links = ('author', 'created_date')  # указываем что хотим сделать ссылкой
    search_fields = ('author', 'created_date')  # поля по которым можно осуществлять поиск
    list_editable = ()  # Редактируемые поля
    list_filter = ('author', 'created_date')  # по каким полям хотим фильтровать


admin.site.register(Post,Blog_admin)  # зарегестрировали

from django.contrib import admin
from .models import Appointment

# Создаем кастомизированный админ-класс
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'date', 'message')  # Указываем, какие поля отображать в списке
    search_fields = ('client_name', 'message')  # Добавляем поиск по имени клиента и сообщению
    list_filter = ('date',)  # Добавляем фильтр по дате
    ordering = ('-date',)  # Сортировка по убыванию даты (от новых к старым)

# Регистрируем модель с кастомным админ-классом
admin.site.register(Appointment, AppointmentAdmin)
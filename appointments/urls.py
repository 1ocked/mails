# from django.urls import path
# from .views import AppointmentView
#
# # app_name = 'appointments'  # задаем пространство имен для URL
#
# urlpatterns = [
#     path('appointments/', AppointmentView.as_view(), name='appointment_created'),
# ]

from django.views.generic import TemplateView
from django.urls import path

from appointments.views import AppointmentView

urlpatterns = [
    path('make_appointment/', AppointmentView.as_view(), name='make_appointment'),
    path('appointment_created/', TemplateView.as_view(template_name='appointment_created.html'), name='appointment_created'),
]
from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.mail import send_mail
from datetime import datetime

from .models import Appointment

class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'appointments/make_appointment.html', {})  # Убедитесь, что путь к шаблону правильный

    def post(self, request, *args, **kwargs):
        # Преобразуем дату из строки в объект datetime
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        # Отправляем письмо
        send_mail(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%m-%d")}',
            message=appointment.message,
            from_email='ruslan7maslianov@yandex.ru',
            recipient_list=['habay@mail.ru']  #
        )

        return redirect('appointments:appointment_created')  # Заменил на правильный redirect

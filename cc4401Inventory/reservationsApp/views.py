from django.shortcuts import render, redirect
from spaceReservationsApp.models import SpaceReservation
from django.contrib import messages


def show(request, reservation_id):
    if request.method == 'GET':
        reservation = SpaceReservation.objects.get(id=reservation_id)
        context = {
            'reservation': reservation
        }
        if reservation.state == 'P':
            return render(request, 'reservation_data.html', context=context)
        else:
            return redirect('landing_articles')


def delete(request):
    if request.method == 'POST':
        reservation_ids = request.POST.getlist('reservation')
        try:
            for reservation_id in reservation_ids:
                reservation = SpaceReservation.objects.get(id=reservation_id)
                if reservation.state == 'P':
                    reservation.delete()
        except:
            messages.warning(request, 'Ha ocurrido un error y la reserva no se ha eliminado')

        return redirect('user_data', user_id=request.user.id)


def modify_reservations(request):
    user = request.user
    if not (user.is_superuser and user.is_staff):
        return redirect('/')
    if request.method == "POST":

        accept = True if (request.POST["accept"] == "1") else False
        reservations = SpaceReservation.objects.filter(id__in=request.POST.getlist("selected"))
        if accept:
            for reservation in reservations:
                reservation.state = 'A'
                reservation.save()
        else:
            for reservation in reservations:
                reservation.state = 'R'
                reservation.save()

    return redirect('/admin/actions-panel')

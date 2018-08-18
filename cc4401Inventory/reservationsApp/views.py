from django.shortcuts import render, redirect
from spaceReservationsApp.models import SpaceReservation
from articleReservationsApp.models import ArticleReservation
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


def modify_articleReservations(request):
    user = request.user
    if not (user.is_superuser and user.is_staff):
        return redirect('/')
    if request.method == "POST":
        try:
            reservations = ArticleReservation.objects.filter(id__in=request.POST.getlist("selected"))
            #recibido
            if request.POST["accept"] == "1":
                for reservation in reservations:
                    reservation.state = 'E'
                    reservation.article.state = 'D'
                    reservation.article.save()
                    reservation.save()
            #perdido
            else:
                for reservation in reservations:
                    reservation.state = 'L'
                    reservation.article.state = 'L'
                    reservation.article.save()
                    reservation.save()
        except:
            messages.warning(request, 'Error: el cambio de estado no se ha efectuado.')
    return redirect("/admin/actions-panel/")


def modify_spaceReservations(request):
    user = request.user
    if not (user.is_superuser and user.is_staff):
        return redirect('/')
    if request.method == "POST":
        reservations = SpaceReservation.objects.filter(id__in=request.POST.getlist("selected"))
        #A de aceptado, R de rechazado
        new_state = 'A' if (request.POST["accept"] == "1") else 'R'
        for reservation in reservations:
            reservation.state = new_state
            reservation.save()
    return redirect('/admin/actions-panel')

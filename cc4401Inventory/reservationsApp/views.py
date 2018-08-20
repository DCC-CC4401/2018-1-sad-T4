from django.shortcuts import render, redirect
from spaceReservationsApp.models import SpaceReservation
from articleReservationsApp.models import ArticleReservation
from django.contrib import messages


def show_space_reservation(request, reservation_id):
    return show_reservation(request, reservation_id, 'space')


def show_article_reservation(request, reservation_id):
    return show_reservation(request, reservation_id, 'article')


def show_reservation(request, reservation_id, item_type):
    if request.method == 'GET':
        reservation_type = SpaceReservation if item_type == 'space' else ArticleReservation
        reservation = reservation_type.objects.get(id=reservation_id)
        item = reservation.space if item_type == 'space' else reservation.article
        context = {
            'reservation': reservation,
            'item': item,
            'item_type': item_type,
            'correct_user': (request.user == reservation.user),
        }
        if reservation.state == 'P':
            return render(request, 'reservationsApp/reservation_data.html', context=context)
        else:
            return redirect('landing_articles')


def delete_space_reservation(request):
    return delete_reservation(request, 'space')


def delete_article_reservation(request):
    return delete_reservation(request, 'article')


def delete_reservation(request, item_type):
    if request.method == 'POST':
        reservation_ids = request.POST.getlist('reservation')
        reservation_type = SpaceReservation if item_type == 'space' else ArticleReservation
        try:
            for reservation_id in reservation_ids:
                reservation = reservation_type.objects.get(id=reservation_id)
                if reservation.state == 'P' and request.user == reservation.user:
                    reservation.delete()
        except:
            messages.warning(request, 'Ha ocurrido un error y la reserva no se ha eliminado')

        return redirect('user_data', user_id=request.user.id)


def modify_reservations(request):
    user = request.user
    if not (user.is_superuser and user.is_staff):
        return redirect('/')
    if request.method == "POST":
        selected = request.POST.getlist('selected')
        reservations = []
        for s in selected:
            item_type, item_id = s.split('-')
            model_type = SpaceReservation if item_type == 'space' else ArticleReservation
            reservations.append(model_type.objects.get(id=item_id))
        #A de aceptado, R de rechazado
        new_state = 'A' if (request.POST["accept"] == "1") else 'R'
        for reservation in reservations:
            reservation.state = new_state
            reservation.save()
    return redirect('/admin/actions-panel')


def modify_loans(request):
    user = request.user
    if not (user.is_superuser and user.is_staff):
        return redirect('/')
    if request.method == 'POST':
        selected = request.POST.getlist('selected')
        reservations = []
        for s in selected:
            item_type, item_id = s.split('-')
            model_type = SpaceReservation if item_type == 'space' else ArticleReservation
            reservations.append(model_type.objects.get(id=item_id))
        new_finish_state = 'E' if (request.POST['accept'] == '1') else 'L'
        for reservation in reservations:
            reservation.finish_state = new_finish_state
            reservation.save()
    return redirect('/admin/actions-panel')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from spaceReservationsApp.models import SpaceReservation
from loansApp.models import Loan
from articlesApp.models import Article
from spacesApp.models import Space
from mainApp.models import User
from datetime import datetime, timedelta, date
import pytz, os
from django.utils.timezone import localtime


@login_required
def user_panel(request):
    user = request.user
    if not (user.is_superuser and user.is_staff):
        return redirect('/')
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'user_panel.html', context)

@login_required
def items_panel(request):
    user = request.user
    if not (user.is_superuser and user.is_staff):
        return redirect('/')
    articles = Article.objects.all()
    spaces = Space.objects.all()
    context = {
        'articles': articles,
        'spaces': spaces
    }
    return render(request, 'items_panel.html', context)

@login_required
def actions_panel(request):
    user = request.user
    if not (user.is_superuser and user.is_staff):
        return redirect('/')
    try:
        current_week = datetime.strptime(request.GET["date"], "%Y-%m-%d").date().isocalendar()[1]
        current_date = request.GET["date"]
    except:
        current_date = date.today().strftime("%Y-%m-%d")
        current_week = date.today().isocalendar()[1]

    colores = {'A': 'rgba(0,153,0,0.7)',
               'P': 'rgba(51,51,204,0.7)',
                'R': 'rgba(153, 0, 0,0.7)'}

    reservations = SpaceReservation.objects.filter(state='P').order_by('starting_date_time')
    current_week_reservations = SpaceReservation.objects.filter(starting_date_time__week = current_week)
    actual_date = datetime.now(tz=pytz.utc)
    try:
        if request.method == "GET":
            if request.GET["filter"]=='vigentes':
                loans = Loan.objects.filter(ending_date_time__gt=actual_date).order_by('starting_date_time')
            elif request.GET["filter"]=='caducados':
                loans = Loan.objects.filter(ending_date_time__lt=actual_date, article__state='P').order_by('starting_date_time')
            elif request.GET["filter"]=='perdidos':
                loans = Loan.objects.filter(ending_date_time__lt=actual_date, article__state='L').order_by('starting_date_time')
            else:
                loans = Loan.objects.all().order_by('starting_date_time')
    except:
        loans = Loan.objects.all().order_by('starting_date_time')

    res_list = []
    for i in range(5):
        res_list.append(list())
    for r in current_week_reservations:
        reserv = list()
        reserv.append(r.space.name)
        reserv.append(localtime(r.starting_date_time).strftime("%H:%M"))
        reserv.append(localtime(r.ending_date_time).strftime("%H:%M"))
        reserv.append(colores[r.state])
        res_list[r.starting_date_time.isocalendar()[2] - 1].append(reserv)

    move_controls = list()
    move_controls.append(
        (datetime.strptime(current_date, "%Y-%m-%d") + timedelta(weeks=-4)).strftime("%Y-%m-%d"))
    move_controls.append(
        (datetime.strptime(current_date, "%Y-%m-%d") + timedelta(weeks=-1)).strftime("%Y-%m-%d"))
    move_controls.append(
        (datetime.strptime(current_date, "%Y-%m-%d") + timedelta(weeks=1)).strftime("%Y-%m-%d"))
    move_controls.append(
        (datetime.strptime(current_date, "%Y-%m-%d") + timedelta(weeks=4)).strftime("%Y-%m-%d"))

    delta = (datetime.strptime(current_date, "%Y-%m-%d").isocalendar()[2]) - 1
    monday = (
        (datetime.strptime(current_date, "%Y-%m-%d") - timedelta(days=delta)).strftime("%d/%m/%Y"))


    context = {
        'reservations_query': reservations,
        'loans': loans,
        'reservations': res_list,
        'current_date': current_date,
        'controls': move_controls,
        'actual_monday': monday
    }
    return render(request, 'actions_panel.html', context)





def add_item(request):

    if request.method == "POST":
        r_name = request.POST["name"] ##Obligatorio
        r_uploaded_file = request.FILES['file']
        r_extension = os.path.splitext(r_uploaded_file.name)[1]
        r_description = request.POST["description"]
        new_art = Article.objects.create(name=r_name, description = r_description)
        new_art.state='D'
        new_art.save()
        new_art.image.save(str(new_art.id)+"_image"+r_extension, r_uploaded_file)
        new_art.save()

    return redirect("/admin/items-panel/")

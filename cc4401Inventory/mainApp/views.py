from django.shortcuts import render, redirect
from django.utils.timezone import localtime
import datetime
from articlesApp.models import Article
from spacesApp.models import Space
from spaceReservationsApp.models import SpaceReservation
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json

@login_required
def landing_articles(request):
    context = {}
    return render(request, 'articulos.html', context)


@login_required
def landing_spaces(request, date=None):

    if date:
        current_date = date
        current_week = datetime.datetime.strptime(current_date,"%Y-%m-%d").date().isocalendar()[1]
    else:
        try:
            current_week = datetime.datetime.strptime(request.GET["date"], "%Y-%m-%d").date().isocalendar()[1]
            current_date = request.GET["date"]
        except:
            current_week = datetime.date.today().isocalendar()[1]
            current_date = datetime.date.today().strftime("%Y-%m-%d")

    reservations = SpaceReservation.objects.filter(starting_date_time__week = current_week, state__in = ['P','A'])
    colores = {'A': 'rgba(0,153,0,0.7)',
               'P': 'rgba(51,51,204,0.7)'}

    res_list = []
    for i in range(5):
        res_list.append(list())
    for r in reservations:
        reserv = []
        reserv.append(r.space.name)
        reserv.append(localtime(r.starting_date_time).strftime("%H:%M"))
        reserv.append(localtime(r.ending_date_time).strftime("%H:%M"))
        reserv.append(colores[r.state])
        res_list[r.starting_date_time.isocalendar()[2]-1].append(reserv)

    move_controls = list()
    move_controls.append((datetime.datetime.strptime(current_date,"%Y-%m-%d")+datetime.timedelta(weeks=-4)).strftime("%Y-%m-%d"))
    move_controls.append((datetime.datetime.strptime(current_date,"%Y-%m-%d")+datetime.timedelta(weeks=-1)).strftime("%Y-%m-%d"))
    move_controls.append((datetime.datetime.strptime(current_date,"%Y-%m-%d")+datetime.timedelta(weeks=1)).strftime("%Y-%m-%d"))
    move_controls.append((datetime.datetime.strptime(current_date,"%Y-%m-%d")+datetime.timedelta(weeks=4)).strftime("%Y-%m-%d"))

    delta = (datetime.datetime.strptime(current_date, "%Y-%m-%d").isocalendar()[2])-1
    monday = ((datetime.datetime.strptime(current_date, "%Y-%m-%d") - datetime.timedelta(days=delta)).strftime("%d/%m/%Y"))
    spaces = Space.objects.all()
    context = {'reservations' : res_list,
               'current_date' : current_date,
               'controls' : move_controls,
               'actual_monday' : monday,
               'spaces' : spaces}
    return render(request, 'espacios.html', context)


@login_required
def landing_search(request, products):
    if not products:
        return landing_articles(request)
    else:
        context = {'productos' : products,
                   'colores' : {'D': '#009900',
                                'R': '#ffcc00',
                                'P': '#3333cc',
                                'L': '#cc0000'}
                   }
        return render(request, 'articulos.html', context)


@login_required
def search(request):
    if request.method == "GET":
        query = request.GET['query']
        #a_type = "comportamiento_no_definido"
        a_state = "A" if (request.GET['estado'] == "A") else request.GET['estado']

        if not (a_state == "A"):
            articles = Article.objects.filter(state=a_state,name__icontains=query.lower())
        else:
            articles = Article.objects.filter(name__icontains=query.lower())

        products = None if (request.GET['query'] == "") else articles
        return landing_search(request, products)




@login_required
def reserve_spaces(request):
    if request.method == "POST":
        horarios = ''
        try:
            horarios = json.loads(request.POST["horarios"])
        except Exception as e:
            messages.warning(request, 'Debe seleccionarse al menos 1 celda para hacer la reservación del espacio.')
            return redirect("/spaces/")
        espacio = request.POST["espacio"]
        try:
            espacio_a_reservar = Space.objects.get(pk=espacio)
        except Exception as e:
            messages.warning(request, 'Debe seleccionarse el espacio donde hacer la reservación.')
            return redirect("/spaces/")

        for h in horarios:

            di = datetime.datetime.strptime(h['dti'], "%Y-%m-%d %H:%M")
            df = datetime.datetime.strptime(h['dtf'], "%Y-%m-%d %H:%M")
            r = SpaceReservation()
            r.space = espacio_a_reservar
            r.starting_date_time = di
            r.ending_date_time = df
            r.user = request.user
            r.save()
            pass
        messages.success(request, 'Reservación realizada con éxito.')
        return redirect("/spaces/")

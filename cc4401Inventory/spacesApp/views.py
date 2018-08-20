from spacesApp.models import Space
from spaceReservationsApp.models import SpaceReservation
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import os

@login_required
def space_data(request, space_id):
    try:
        space = Space.objects.get(id=space_id)
        context = {'space': space}

        return render(request, 'space_data.html', context)
    except Exception as e:
        print(e)
        return redirect('/')

@login_required
def space_edit_name(request, space_id):

    if request.method == "POST":
        a = Space.objects.get(id=space_id)
        a.name = request.POST["name"]
        a.save()
    return redirect('/space/'+str(space_id))


@login_required
def space_edit_image(request, space_id):

    if request.method == "POST":
        u_file = request.FILES["image"]
        extension = os.path.splitext(u_file.name)[1]
        a = Space.objects.get(id=space_id)
        a.image.save(str(space_id)+"_image"+extension, u_file)
        a.save()

    return redirect('/space/' + str(space_id))



@login_required
def space_edit_description(request, space_id):
    if request.method == "POST":
        a = Space.objects.get(id=space_id)
        a.description = request.POST["description"]
        a.save()

    return redirect('/space/' + str(space_id))

@login_required
def space_delete(request, space_id):
    if not request.user.is_staff:
        return redirect('/')
    try:
        space = Space.objects.get(id=space_id)
        space.delete()
        space.save()
        return redirect('items-panel')
    except Exception as e:
        print(e)
        return redirect('items-panel')

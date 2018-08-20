from django.shortcuts import render, redirect
from spacesApp.models import Space
from django.contrib.auth.decorators import login_required

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

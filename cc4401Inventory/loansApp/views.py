from django.shortcuts import render, redirect
from articleReservationsApp.models import ArticleReservation


def show(request, loan_id):
    if request.method == 'GET':
        loan = ArticleReservation.objects.get(id=loan_id)
        context = {
            'loan': loan
        }
        if loan.state == 'P':
            render(request, 'loan_data.html', context=context)
        else:
            redirect('landing_articles')

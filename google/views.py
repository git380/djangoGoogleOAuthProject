from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def toppage(request):
    return render(request, 'toppage.html')


@login_required
def home(request):
    return render(request, 'home.html')

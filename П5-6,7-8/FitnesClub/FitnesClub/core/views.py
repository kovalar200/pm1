from django.shortcuts import render

def report(request):
    return render(request, 'app.html', context={'clients': client})

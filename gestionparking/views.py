from django.shortcuts import render

def home(request):
    # Logique de la vue
    return render(request, 'home.html')
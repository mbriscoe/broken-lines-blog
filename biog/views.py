from django.shortcuts import render
from .models import Biog

def biog(request):
    
    biogs = Biog.objects.all()

    return render(request, "biog/biog_list.html", {"biogs": biogs})


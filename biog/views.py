from django.shortcuts import render
from .models import Biog


def biog(request):
    """
    Renders the most recent list of biography entries

    Displays instances of :model:'biog.Biog`.
    **Context**
    ``biogs``
        The most recent instances of :model:`biog:Biog`.

    **Template**
    :template:`biog/biog_list.html`
    """
    biogs = Biog.objects.all()

    return render(request, "biog/biog_list.html", {"biogs": biogs})

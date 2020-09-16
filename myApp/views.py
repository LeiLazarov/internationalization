from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _


# Create your views here.
def index(request):
    context = {'msg': _("Welcome to China")}
    return render(request, 'myApp/index.html', context)




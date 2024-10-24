from bas.models import *
from web.models import *

#Empresa
def empresa(request):
    emp = Empresa.objects.all().first()

    return {'emp': emp}

#Menu
def menu(request):
    men = Menu.objects.all()
    print('oe', men)

    return {'menu': men}

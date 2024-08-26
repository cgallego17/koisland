from bas.models import *

def empresa(request):
    emp = Empresa.objects.all().first()

    return {'emp': emp}
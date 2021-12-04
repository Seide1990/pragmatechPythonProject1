from .models import About
def global_about(request):
    about1=About.objects.filter(pk=1).first
    return {'about':about1}
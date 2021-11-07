from django.shortcuts import redirect, render
from django.http import request
from .forms import ContactForm

# Create your views here.
def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mekteb/')
    return render(request, 'contact.html', {'form': form})
# Create your views here.

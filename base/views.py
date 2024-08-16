from django.shortcuts import render
from .forms import contact
from .models import user

# Create your views here.
def home(request):
    if request.method == 'POST':
        fm = contact(request.POST)
        if fm.is_valid():
            em = fm.cleaned_data['email']
            msg = fm.cleaned_data['message']
            reg = user(email = em, message=msg)
            reg.save()
        else:
            # Handle form errors here
            print("Form errors:", fm.errors)
    else:
        fm = contact()
        print("Its come from GET method")

    return render(request, 'base/index.html',{'form': fm})



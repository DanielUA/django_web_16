from django.shortcuts import redirect, render, HttpResponse

from .forms import PictureForm
from .models import Pictures

def index(request):
    return render(request, 'app_photo/index.html', context={'msg': 'Hello world!!!!'})

def pictures(request):
    pics = Pictures.objects.all()
    return render(request, 'app_photo/pictures.html', context={'pics': pics})

def upload(request):
    form = PictureForm(instance=Pictures())
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES, instance=Pictures())
        if form.is_valid():
            form.save()
            return redirect(to='app_photo:pictures')
    return render(request, 'app_photo/upload.html', context={'form': form})

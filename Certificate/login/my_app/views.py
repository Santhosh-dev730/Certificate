from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .models import certificate  # model_name
from bson import ObjectId       #get id from mongodb
from .forms import certificate_form  # form_name

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = certificate_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form = certificate_form()
    return render(request, 'create.html', {'form': form})

def read(request):
    datas = certificate.objects.all()
    return render(request,'read.html',{'datas': datas})

def update(request, id):
    object_id = ObjectId(id)
    item = get_object_or_404(certificate, _id=object_id)
    if request.method == 'POST':
        form = certificate_form(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form = certificate_form(instance=item)
    return render(request, 'update.html', {'form': form})

def delete(request, id):
    object_id = ObjectId(id)
    item = get_object_or_404(certificate, _id=object_id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('read') 

    return render(request, 'delete.html', {'item': item})
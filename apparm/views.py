from django.shortcuts import render

# My imports
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from apparm.models import Proveedor, Call
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.


# =========== FRONTEND SECTION ============
# function to render home
def frontend(request):
    return render(request, 'frontend.html')


# =========== BACKEND SECTION ============
# function to render backend
@cache_control(no_cache = True, must_revalidate= True, no_store = True)
@login_required(login_url='login')
def backend(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_proveedor_list = Proveedor.objects.filter(
            Q(nombre__icontains=q) | Q(telefono=q) | Q(email=q) | Q(direccion=q) | Q(rrss=q) | Q(nota=q)
        ).order_by('-created_at')


    else:
        all_proveedor_list = Proveedor.objects.all().order_by('-created_at')

    paginador = Paginator(all_proveedor_list, 4)
    page = request.GET.get('page')
    all_proveedor = paginador.get_page(page)

    total = Proveedor.objects.all().count()

    return render(request, 'backend.html', {"proveedor": all_proveedor, 'count':total})


# funtion to insert add_proveedor
@cache_control(no_cache = True, must_revalidate= True, no_store = True)
@login_required(login_url='login')
def add_proveedor(request):
    if request.method == "POST":

        email = request.POST['email']

        if Proveedor.objects.filter(email=email).exists():
            messages.error(request, 'El mail ya esta registrado')
            return render(request, 'add.html')

        elif request.POST.get('nombre') and request.POST.get('telefono') and request.POST.get('email') and request.POST.get('direccion') and request.POST.get('rrss') or request.POST.get('nota'):
            proveedor=Proveedor()
            proveedor.nombre = request.POST.get('nombre')
            proveedor.telefono = request.POST.get('telefono')
            proveedor.email = request.POST.get('email')
            proveedor.direccion = request.POST.get('direccion')
            proveedor.rrss = request.POST.get('rrss')
            proveedor.nota = request.POST.get('nota')
            proveedor.save()
            messages.success(request, "Patient added successfully !")
            return HttpResponseRedirect('/backend')
    else:
            return render(request, 'add.html')


# FUNCTION to delete proveedor
@cache_control(no_cache = True, must_revalidate= True, no_store = True)
@login_required(login_url='login')
def delete_proveedor(request, pro_id):
    proveedor = Proveedor.objects.get(id=pro_id )
    proveedor.delete()
    messages.success(request, 'Proveedor removido exitosamente')
    return HttpResponseRedirect('/backend')


# FUNCTION  to access the proveedor individual
@cache_control(no_cache = True, must_revalidate= True, no_store = True)
@login_required(login_url = 'login')
def provee(request, pro_id):
    proveedor = Proveedor.objects.get(id=pro_id)
    if proveedor != None:
        return render(request, 'edit.html', {'proveedor':proveedor})


#FUNCTION  to edit proveedor 
@cache_control(no_cache = True, must_revalidate= True, no_store = True)
@login_required(login_url = 'login')
def edit_proveedor(request):

    if request.method == 'POST':
        proveedor = Proveedor.objects.get(id = request.POST.get('id'))
        if proveedor != None:

            proveedor.nombre = request.POST.get('nombre')
            proveedor.telefono = request.POST.get('telefono')
            proveedor.email = request.POST.get('email')
            proveedor.direccion = request.POST.get('direccion')
            proveedor.rrss = request.POST.get('rrss')
            proveedor.nota = request.POST.get('nota')
            proveedor.save()
            
            messages.success(request, 'Proveedor actualizado exitosamente')
            return HttpResponseRedirect('/backend')

#FUNCTION Support
@cache_control(no_cache = True, must_revalidate= True, no_store = True)
@login_required(login_url = 'login')
def support(request):
    if request.method == "POST":

        support = Call()

        user = request.POST.get('user')
        message = request.POST.get('message')
        terms = request.POST.get('terms')
        option = request.POST.get('option')
        reason = request.POST.get('reason')

        support.user = user
        support.message = message
        support.terms = terms
        support.option = option
        support.reason = reason

        support.save()
        messages.success(request, "Responderemos en breve !")
        return HttpResponseRedirect('/backend')

    else:
        return HttpResponseRedirect('/backend')

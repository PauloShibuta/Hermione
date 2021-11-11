from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .forms import Clienteform
from .models import Cliente
# Create your views here.

def index(request):
    #return HttpResponse("<h1>Aqui é o índice<h1>")
    return render(request, 'locacao/index.html')

def cliente(request):
    #return HttpResponse("<h1>Aqui é a área de clientes<h1>")
    clientes = Cliente.objects.all()
    busca = request.GET.get('search')
    if busca:
    	clientes = Cliente.objects.filter(nome__icontains = busca)
    return render(request, 'locacao/cliente.html',{'clientes':clientes})

def editar(request, id):
	clie = get_object_or_404(Cliente, pk = id)
	form = Clienteform(instance = clie)

	if request.method == "POST":
		form = Clienteform(request.POST, instance = clie)

		if form.is_valid():
			clie = form.save()
			clie.save()
			return redirect('clientes')

		else:
			return render(request, "locacao/editar_clientes.html", {'form':form, 'clie':clie})
	else:
		return render(request, "locacao/editar_clientes.html", {'form':form, 'clie':clie})		


def criar_clientes(request):
	form = Clienteform(request.POST)
	if request.method == "POST":
		form= Clienteform(request.POST, request.FILES)
		if form.is_valid():
			clie = form.save()
			clie.save()
			form = Clienteform()
	return render(request, 'locacao/criar_clientes.html',{'form':form})


def excluir(request, id):
	clie = get_object_or_404(Cliente, pk = id)
	if request.method == "POST":
		clie.delete()
		return redirect('clientes')
	return render(request, 'locacao/excluir_clientes.html', {'clie':clie})


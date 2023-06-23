from django.http import Http404, HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import View
from .models import Producto
from .forms import SearchBebidaForm
import json
# Create your views here.

def para_ajax(request):
    params = {}
    search = SearchBebidaForm()
    params['search'] = search
    return render(request, "ver_ajax.html", params)

class BuscarBebida(View):
    def get(self, request):
        if request.is_ajax:
            palabra=request.GET.get('term', '')
            bebida=Producto.objects.filter(nombre__icontains=palabra)
            result= []
            for an in bebida:
                data= {}
                data['label']=an.nombre
                result.append(data)
            data_json= json.dumps(result)
        else:
            print("fallo")
            data_json= "fallo"
        mimetype="application/json"
        return HttpResponse(data_json, mimetype)

class BuscarBebida2(View):

    def get(self, request):
        if request.is_ajax:
            q = request.GET['valor']
            bebida = Producto.objects.filter(nombre__icontains=q)
            results = []
            for rec in bebida:
                print(rec.nombre)
                print(rec.estado)
                print(rec.img)

                data = {}
                data['producto'] = rec.nombre
                data['estado'] = rec.estado
                data['ruta_imagen'] = str(rec.img)
                results.append(data)
            data_json = json.dumps(results)

        else:
            data_json = "fallo"
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)
    
class EjemploTienda(View):
    template= "tienda.html"

    def get(self, request):
        params={}
        try:
            productos = Producto.objects.all()
        except Producto.DoesNotExist:
            raise Http404
        params ["productos"] = productos

        try:
            request.session["carro"]
        except:
            request.session["carro"] = {}


        return render(request, self.template, params)


class VerImagenes(View): 
    template = "verimagenes.html"

    def get(self, request):
        params={}
        try:
            productos = Producto.objects.all()
        except Producto.DoesNotExist:
            raise Http404
        params["productos"] = productos
        
        return render(request, self.template, params)


def ver_imagen(request, producto_id):
    params={}
    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:
        raise Http404
    params["producto"] = producto
    
    return render(request, "verimagen.html", params)

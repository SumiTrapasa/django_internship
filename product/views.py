from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import product
from .form import ProductForm, RawProductForm

def product_update_view(request,id=id):
    obj = get_object_or_404(product, id=id)
    form=ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        "form":form
    }
    return render(request, "products/product_create.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None) 
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form' : form
    }
    return render(request, "products/product_create.html", context)

def product_list_view(request):
    queryset = product.objects.all()
    context = {
        "object_list" : queryset
    }
    return render(request, "products/product_list.html", context)

def product_detail_view(request,id):
    obj = get_object_or_404(product,id=id)
    # context = {
    #     'title' : obj.title,
    #     'description' : obj.description
    # }
    context = {
        'object' : obj
    }
    return render(request, "products/product_detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object" : obj
    }
    return render(request, "products/product_delete.html", context)

# def dynamic_lookup_view(request, id):
#     obj = product.objects.get(id=id)
#     obj = get_object_or_404(product, id=id)
#     # try:
#     #     obj = product.objects.get(id=my_id)
#     # except product.DoesNotExist:
#     #     raise Http404
#     context = {
#         "object" : obj
#     }
#     return render(request, "products/product_detail.html", context)

# def render_initial_data(request):
#     initial_data = {
#         'title': "my awesome title"
#     }
#     obj = product.objects.get(id=1)
#     form=ProductForm(request.POST or None, initial=initial_data, instance=obj)
#     if form.is_valid():
#         form.save()
#     context = {
#         "form":form
#     }
#     return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     my_form= RawProductForm()
#     if request.method == "POST":
#         my_form= RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             product.objects.create( **my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form":my_form
#     }
#     return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#     # project.object.create(title=my_new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     form = ProductForm(request.POST or None) 
#     if form.is_valid():
#         form.save()
#         form = ProductForm()

#     context = {
#         'form' : form
#     }
#     return render(request, "products/product_create.html", context)

# # Create your views here.
# def product_detail_view(request):
#     obj = product.objects.get(id=1)
#     # context = {
#     #     'title' : obj.title,
#     #     'description' : obj.description
#     # }
#     context = {
#         'object' : obj
#     }
#     return render(request, "products/product_detail.html", context)
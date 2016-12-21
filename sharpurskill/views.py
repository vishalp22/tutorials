from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from myproject.models import Course_detail

from .models import Sub_Category


# Create your views here.

def single_product(request):
    return render(request, 'single-product.html', {})


def category_grid(request):
    sub_category = Sub_Category.objects.all()
    queryset = {
        'queryset': sub_category,
    }
    return render(request, 'category-grid-2.html', queryset)


def authentication(request):
    return render(request, 'authentication.html', {})


def Contact_Us(request):
    return render(request, 'contact.html', {})

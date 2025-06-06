from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from .models import Product
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .forms import ProductForm, ProductModeratorForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def get_form_class(self):
        user = self.request.user
        if user.has_perm('can_unpublish_product') and user.has_perm('can_delete_product'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:home')
    context_object_name = 'product'


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request):
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")

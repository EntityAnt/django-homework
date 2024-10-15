from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse

from catalog.forms import ProductForm, CategoryForm
from catalog.models import Product, Category

from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')

    def get_success_url(self):
        return reverse('catalog:products_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')


class CategoryListView(ListView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:category_list')


class CategoryDetailView(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('catalog:category_list')




class ContactView(TemplateView):
    template_name = 'catalog/contact.html'

    def get_context_data(self, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            phone = self.request.POST.get('phone')
            message = self.request.POST.get('message')
            print(f"Получено сообщение от {name} тел. {phone}: {message}")
            return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
        return super().get_context_data(**kwargs)


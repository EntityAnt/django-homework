from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products_list.html', context)


def products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'products_detail.html', context)


# def home(request):
#     return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        print(f"Получено сообщение от {name} тел. {phone}: {message}")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'contacts.html')

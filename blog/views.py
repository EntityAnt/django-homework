from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views import View
from django.shortcuts import render

from .models import BlogPost

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self):
        # Получаем только опубликованные объекты
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = '__all__'
    success_url = reverse_lazy('blog:post_list')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = '__all__'
    success_url = reverse_lazy('blog:post_list')

    def get_success_url(self):
        return reverse('blog:post_detail', args=[self.kwargs.get('pk')])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:post_list')


class ContactView(View):
    template_name = 'blog/blog_contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Получено сообщение от {name} тел. {phone}: {message}")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")

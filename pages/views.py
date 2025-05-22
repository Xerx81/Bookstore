from django.views.generic import ListView, TemplateView

from books.models import Book


class HomePageView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "home.html"

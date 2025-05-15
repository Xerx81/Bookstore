from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView

from .models import Book
from .forms import ReviewForm


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"
    login_url = "account_login"

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get("category")

        valid_categories = [choice[0] for choice in Book.CATEGORY_CHOICES]

        if category in valid_categories:
            queryset = queryset.filter(category=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_value = self.request.GET.get("category")

        category_name = None
        if category_value:
            for value, name in Book.CATEGORY_CHOICES:
                if value == category_value:
                    category_name = name

        context["category_name"] = category_name
        return context
        

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"
    login_url = "account_login"
    queryset = Book.objects.all().prefetch_related("reviews__author",)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["form"] = ReviewForm
        return context

    def post(self, request, *args, **kwargs):
        book = self.get_object()
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.book = book
            review.save()
            return redirect(book)
        else:
            context = self.get_context_data()
            context["form"] = form
            return self.render_to_response(context)


class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list" 
    template_name = "books/search_results.html"

    def get_queryset(self):
        self.query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=self.query) |
            Q(author__icontains=self.query)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.query
        return context

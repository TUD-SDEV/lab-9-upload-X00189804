from django.views.generic import ListView, DetailView 
from .models import Book
from django.db.models import Q 

# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'book_list'

class BookDetailView(DetailView):
    model = Book
    tempalte_name = 'books/book_detail.html'


class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    tempalte_name = 'book/search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(authur__icontains=query)
        )

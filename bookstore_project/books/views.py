from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin # new
from django.views.generic import ListView,DetailView
from .models import Book
from django.db.models import Q # new

class BookListView(LoginRequiredMixin,ListView):
    model = Book
    context_object_name = 'book_list' # new
    template_name = 'books/book_list.html'
    login_url = 'account_login' # new

class BookDetailView(LoginRequiredMixin,DetailView,PermissionRequiredMixin): # new
    model = Book
    context_object_name = 'book' # new
    template_name = 'books/book_detail.html'   
    login_url = 'account_login' # new 
    permission_required = 'books.special_status'


class SearchResultsListView(ListView): # new
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'   
    
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
                ) 
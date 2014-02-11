# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from books.models import Author, Publisher, Book

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

from django.http import HttpResponse

# Index
def index(request):
	return render(request, 'books/index.html')

# Author
class AuthorList(ListView):
    model=Author
    paginate_by = 10
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):        
        return super(AuthorList, self).dispatch(request, *args, **kwargs)

class AuthorDetail(DetailView):
    model=Author

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):        
        return super(AuthorDetail, self).dispatch(request, *args, **kwargs)

class AuthorCreate(CreateView):
    model = Author
    template_name = 'books/object_create_form.html'
    success_url = reverse_lazy('books:author-list',)

    #@method_decorator(login_required)
    @method_decorator(permission_required('books.add_author', login_url='/books/login/'))
    def dispatch(self, request, *args, **kwargs):        
        return super(AuthorCreate, self).dispatch(request, *args, **kwargs)

class AuthorUpdate(UpdateView):
    model = Author
    template_name = 'books/object_update_form.html'
    success_url = reverse_lazy('books:author-list',)

    #@method_decorator(login_required)
    @method_decorator(permission_required('books.change_author', login_url='/books/login/'))
    def dispatch(self, request, *args, **kwargs):        
        return super(AuthorUpdate, self).dispatch(request, *args, **kwargs)

class AuthorDelete(DeleteView):
    model = Author
    template_name='books/object_confirm_delete.html'
    success_url = reverse_lazy('books:author-list',)

    #@method_decorator(login_required)
    @method_decorator(permission_required('books.delete_author', login_url='/books/login/'))
    def dispatch(self, request, *args, **kwargs):        
        return super(AuthorDelete, self).dispatch(request, *args, **kwargs)

# Publisher
class PublisherList(ListView):
    model=Publisher
    paginate_by = 10

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):        
        return super(PublisherList, self).dispatch(request, *args, **kwargs)

class PublisherDetail(DetailView):
    model=Publisher

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):        
        return super(PublisherDetail, self).dispatch(request, *args, **kwargs)

class PublisherCreate(CreateView):
    model = Publisher
    template_name = 'books/object_create_form.html'
    success_url = reverse_lazy('books:publisher-list',)

    #@method_decorator(login_required)
    @method_decorator(permission_required('books.add_publisher', login_url='/books/login/'))
    def dispatch(self, request, *args, **kwargs):        
        return super(PublisherCreate, self).dispatch(request, *args, **kwargs)

class PublisherUpdate(UpdateView):
    model = Publisher
    template_name = 'books/object_update_form.html'
    success_url = reverse_lazy('books:publisher-list',)

    #@method_decorator(login_required)
    @method_decorator(permission_required('books.change_publisher', login_url='/books/login/'))
    def dispatch(self, request, *args, **kwargs):        
        return super(PublisherUpdate, self).dispatch(request, *args, **kwargs)

class PublisherDelete(DeleteView):
    model = Publisher
    template_name='books/object_confirm_delete.html'
    success_url = reverse_lazy('books:publisher-list',)

    #@method_decorator(login_required)
    @method_decorator(permission_required('books.delete_publisher', login_url='/books/login/'))
    def dispatch(self, request, *args, **kwargs):        
        return super(PublisherDelete, self).dispatch(request, *args, **kwargs)

# Book
class BookList(ListView):
    model=Book
    paginate_by = 10

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):        
        return super(BookList, self).dispatch(request, *args, **kwargs)

class BookDetail(DetailView):
    model=Book

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):        
        return super(BookDetail, self).dispatch(request, *args, **kwargs)

class BookCreate(CreateView):
    model = Book
    fields = ('title', 'publisher', 'publication_date', 'authors')
    #template_name = 'books/object_create_form.html'
    template_name = 'books/book_create_form.html'
    success_url = reverse_lazy('books:book-list')

    #@method_decorator(login_required)
    @method_decorator(permission_required('books.add_book', login_url='/books/login/'))
    def dispatch(self, request, *args, **kwargs):        
        return super(BookCreate, self).dispatch(request, *args, **kwargs)

class BookUpdate(UpdateView):
    model = Book
    fields = ('title', 'publisher', 'publication_date', 'authors')
    #template_name = 'books/object_update_form.html'
    template_name = 'books/book_update_form.html'
    success_url = reverse_lazy('books:book-list')

    #@method_decorator(login_required)
    @method_decorator(permission_required('books.change_book', login_url='/books/login/'))
    def dispatch(self, request, *args, **kwargs):        
        return super(BookUpdate, self).dispatch(request, *args, **kwargs)

class BookDelete(DeleteView):
    model = Book
    template_name='books/object_confirm_delete.html'
    success_url = reverse_lazy('books:book-list',)

    #@method_decorator(login_required)
    @method_decorator(permission_required('books.delete_book', login_url='/books/login/'))
    def dispatch(self, request, *args, **kwargs):        
        return super(BookDelete, self).dispatch(request, *args, **kwargs)


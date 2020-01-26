from .models import Book
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BookListView(ListView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'pages']

    success_url = '/'


class BookDetailView(DetailView):
    model = Book


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'pages']
    success_url = '/'


class BookDeleteView(DeleteView):
    model = Book
    success_url = '/'
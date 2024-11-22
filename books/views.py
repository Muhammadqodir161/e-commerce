from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Book
from .forms import BookForm


def book_list(request):
    books = Book.objects.all()
    ctx = {'books': books}
    return render(request, 'book_list.html', ctx)


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    ctx = {'book': book}
    return render(request, 'book_detail.html', ctx)


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            return HttpResponse("Form is invalid")
    form = BookForm()
    ctx = {'form': form}
    return render(request, 'add_book.html', ctx)


def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=pk)
        else:
            return HttpResponse("Form is invalid")
    form = BookForm(instance=book)
    ctx = {'form': form, 'book': book}
    return render(request, 'add_book.html', ctx)


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('list')
    return render(request, 'confirm.html', {'book': book})
# celery


# get -> foydalanuvchiga ma'lumotni jo'natish
# post -> foydalanuvchidan serverga ma'lumot jo'natish uchun
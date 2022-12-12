from django.shortcuts import render, redirect

from bookapp.web.forms import ProfileForm, BookForm, DeleteProfileForm
from bookapp.web.models import Profile, Book


# Create your views here.

def get_profile():
    profile = Profile.objects.first()
    return profile


def home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    else:
        books = Book.objects.all()
        context = {
            'books': books,
            'profile': profile,
        }
        return render(request, 'home-with-profile.html', context)


def add_page(request):
    print(request)
    if request.method == 'POST':
        print(1)
        form = BookForm(request.POST)
        if form.is_valid:
            print(2)
            form.save()
            return redirect('home')

    else:
        print(3)
        form = BookForm()
        context = {
            'form': form,

        }
        return render(request, 'add-book.html', context)


def edit_page(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid:
            form.save()
            redirect('home')
    else:
        form = BookForm(instance=book)
        context = {
            'form': form,
            'book': book,

        }
        return render(request, 'edit-book.html', context)


def page_details(request, pk):
    book = Book.objects.get(pk=pk)
    profile = get_profile()
    context = {
        'book': book,
        'profile': profile,
    }
    return render(request, 'book-details.html', context)


def delete_page(request, pk):
    book = Book.objects.get(pk=pk)

    book.delete()
    return redirect('home')


def profile(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':

        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:


        form = ProfileForm()
        context = {
            'form': form
        }
        return render(request, 'home-no-profile.html', context)


def edit_profile(request):

    profile = get_profile()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
        context = {
            'form': form,
            'profile': profile,
        }
        return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        Profile.objects.all().delete()
        Book.objects.all().delete()
        return redirect('home')
    else:
        form = DeleteProfileForm()
        context = {
            'profile': profile,
            'form': form,
        }
        return render(request, 'delete-profile.html', context)

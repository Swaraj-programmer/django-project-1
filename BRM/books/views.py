from django.shortcuts import render,redirect
from . forms import NewBookForm,SearchForm
from . import models
from django.contrib import messages
from django.contrib.auth.models import User, auth
from books.models import Book
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('http://localhost:8000/books/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('http://localhost:8000/books/register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('http://localhost:8000/books/')

        else:
            messages.info(request,'password not matching..')    
            return redirect('http://localhost:8000/books/register/')
        return redirect('/')
        
    else:
        return render(request,'books/register.html')
def register(request):
    data={}
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,username=username, email=email ,password=password)
        if user:
            register(request,user)
            return HttpResponseRedirect('http://localhost:8000/books/views-books')
        else:
            data['error']='Username or Password is incorrect'
            return render(request, 'books/register.html')
        
    else:
            return render(request,'books/register.html',data)
    if request.method=='POST':
        username.data['username']
        email.data['email']
        password.data['password']
        book.save()
        return HttpResponseRedirect('http://localhost:8000/books/')

def userLogin(request):
    data={}
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username, password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('http://localhost:8000/books/views-books')
        else:
            data['error']='Username or Password is incorrect'
            return render(request, 'books/user_login.html')
    else:
            return render(request,'books/user_login.html',data)
                               
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('http://localhost:8000/books/')
@login_required(login_url='http://localhost:8000/books/')
def viewBooks(request):
    books=Book.objects.all()
    res=render(request,'books/view_books.html', {'book': books})
    return res
@login_required(login_url='http://localhost:8000/books/')
def deleteBook(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('http://localhost:8000/books/views-books/')
@login_required(login_url='http://localhost:8000/books/')
def editBook(request):
    book=models.Book.objects.get(id=request.GET['bookid'])
    fields={'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    res=render(request, 'books/edit_books.html', {'form':form,'book':book})
    return res
@login_required(login_url='http://localhost:8000/books/')
def edit(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.id=request.POST['bookid']
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    return HttpResponseRedirect('http://localhost:8000/books/views-books/')
@login_required(login_url='http://localhost:8000/books/')
def searchBook(request):
    form=SearchForm()
    res=render(request, 'books/search_book.html',{'form':form})
    return res
@login_required(login_url='http://localhost:8000/books/')
def search(request):
    form=SearchForm(request.POST)
    books=models.Book.objects.filter(title=form.data['title'])
    res=render(request, 'books/search_book.html', {'form':form,'books':books})
    return res
@login_required(login_url='http://localhost:8000/books/')
def insertBook(request):
    form=NewBookForm()
    res=render(request, 'books/insert_book.html',{'form':form})
    return res
@login_required(login_url='http://localhost:8000/books/')
def insert(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    s="Record Inserted Successfully<br><a href='http://localhost:8000/books/views-books'>Views Books</a>"

    return HttpResponse(s)

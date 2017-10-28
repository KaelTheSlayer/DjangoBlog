from .models import *
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.

def archive(request):
    return render(request, "archive.html", {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, "article.html", {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if not request.user.is_anonymous():
        if request.method == "POST":
            form = {
                'text': request.POST["text"],
                'title': request.POST["title"]
            }
            if form["text"] and form["title"]:
                if not Article.objects.filter(title=form["title"]).exists():
                    article = Article.objects.create(text=form["text"],
                                                     title=form["title"],
                                                     author=request.user)
                    return redirect('get_article', article_id=article.id)
                else:
                    form['errors'] = u"Статья с таким именем уже существует"
                    return render(request, "create_post.html", {'form': form})
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, "create_post.html", {'form': form})

        else:
            return render(request, 'create_post.html', {})
    else:
        raise Http404


def reg(request):
    if request.method == "POST":
        form = {
            'username': request.POST['username'],
            'email': request.POST['email'],
            'password': request.POST['password'],
            'sec_password': request.POST['sec_password']
        }
        if form["username"] and form["password"] and form["sec_password"]:
            if not User.objects.filter(username=form["username"]).exists():
                if form["password"] == form["sec_password"]:
                    User.objects.create_user(username=form["username"],
                                             email=form["email"],
                                             password=form["password"])
                    return redirect('archive')
                form['errors'] = u"Пароли не совпадают"
                return render(request, "reg.html", {'form': form})
            else:
                form['errors'] = u"Пользователь с таким именем уже существует"
                return render(request, "reg.html", {'form': form})
        else:
            form['errors'] = u"Не все поля заполнены"
            return render(request, "reg.html", {'form': form})
    else:
        return render(request, 'reg.html', {})


def auth(request):
    if request.method == "POST":
        form = {
            'username': request.POST['username'],
            'password': request.POST['password'],
        }
        if form["username"] and form["password"]:
            user = authenticate(username=form["username"], password=form["password"])
            if user is not None:
                login(request, user)
                return redirect('archive')
            else:
                form['errors'] = u"Нет аккаунта с такими сочетанием никнейма и пароля"
                return render(request, "auth.html", {'form': form})

    else:
        return render(request, "auth.html", {})

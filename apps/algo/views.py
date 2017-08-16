from django.shortcuts import render, redirect, HttpResponse
from models import User, Algo, UserAlgo
from django.contrib import messages, sessions

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# /////////////////////////start////////////////

# def index(request):
#     # print request.session.userid
#     show_algos = Algo.objects.all()
#     context = {
#     'show_algos': show_algos
#     }
#     return render(request,'index.html', context)

# def test_page(request):
#     return render(request, 'page_test.html')

def level_two(request):
    return render(request, 'level_two.html')

# //////////////////////login-reg/////////////////


# def index(request):
#     # print request.session.userid
#     show_algos = Algo.objects.all()
#     context = {
#     'show_algos': show_algos
#     }
#     return render(request,'index.html', context)

def loginPage(request):
	return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        user = User.objects.register(request.POST)
        if 'errors' in user:
            for error in user['errors']:
                messages.error(request, error)
            return redirect('/loginPage')
        if 'theuser' in user:
            request.session['theuser'] = user['theuser']
            request.session['username'] = user['username']
            request.session['userid'] = user['userid']
            return redirect('/')

def login(request):
    if request.method == "POST":
        user = User.objects.login(request.POST)
        if 'errors' in user:
            for error in user['errors']:
                messages.error(request, error)
            return redirect('/loginPage')
        if 'theuser' in user:
            request.session['theuser'] = user['theuser']
            request.session['username'] = user['username']
            request.session['userid'] = user['userid']
            request.session['points'] = user['points']
            return redirect('/')

# ///////////////////////////////////////////////////////////

def show_all(request):
    show_users = User.objects.all()
    show_algos = Algo.objects.all()
    show_join = UserAlgo.objects.all()
    context = {
    'show_users': show_users,
    'show_algos': show_algos,
    'show_joins' : show_join

    }
    return render(request, 'admin_dash.html',context)

def user(request, id):
    show_user = User.objects.get(id=id)
    context = {
    'show': show_user
    }
    return render(request, 'user_dash.html', context)

def logout(request):
    del request.session['userid']
    del request.session['theuser']
    del request.session['username']
    return redirect('/')


# ///////////////////algo logic//////////////////

def submit_algo(request):
    if request.method == "POST":
        algo = Algo.objects.addAlgo(request.POST)
        if 'errors' in algo:
            for error in algo['errors']:
                messages.error(request,error)
            return redirect ('/')
        if 'algoid' in algo:
            return redirect('/show_users')

def submit_answer(request,id,page):
    if request.method == "POST":
        answer = Algo.objects.checkAlgo(request.POST, id=id, page=page)
        print answer
        if 'errors' in answer:
            for error in answer['errors']:
                messages.error(request,error)
            return redirect ('/?page='+page)
        if 'messageCorrect' in answer:
            messages.success(request, "That is Correct")
            return redirect('/?page='+page)

def submit_answer_nologin(request, page):
    if request.method == "POST":
        answer = Algo.objects.checkAlgo_nologin(request.POST, id=page)
        if 'errors' in answer:
            for error in answer['errors']:
                messages.error(request,error)
            return redirect ('/?page='+page)
        if 'messageCorrect' in answer:
            messages.success(request, "That is Correct")
            return redirect('/?page='+page)

# ///////////////////////Paginator/////////////////////////

def algo_view(request):
        algo_list = Algo.objects.all()
        show_algos = Algo.objects.all()
        paginator = Paginator(algo_list, 1)
        page = request.GET.get('page')
        try:
            algos = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            algos = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            algos = paginator.page(paginator.num_pages)
        context = {
        'show_algos': show_algos
        }
        return render(request, 'index.html', {'algos': algos}, context)

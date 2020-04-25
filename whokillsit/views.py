from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from Werewolf.settings import MEDIA_KEY_PREFIX
from whokillsit.models import Tutor, Ranking, UserInfo, PersonInfo, Strategy, Remark


def home(request):
    return render(request, 'home.html')


def tutors(request):
    tutors = Tutor.objects.all()
    return render(request, 'tutors.html', context=locals())


def tutor(request, t_id):
    tutor = Tutor.objects.get(id=t_id)
    return render(request, 'tutor.html', locals())


def strategies(request):
    strategies_added = Strategy.objects.all()
    return render(request, 'strategies.html', locals())


def add_strategy(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = UserInfo.objects.get(id=user_id)
        if request.method == 'GET':
            return render(request, 'add_strategy.html')
        elif request.method == 'POST':
            adding_strategy = Strategy()
            adding_strategy.strategy = user
            adding_strategy.s_title = request.POST.get('title')
            adding_strategy.s_content = request.POST.get('content')
            adding_strategy.s_words = len(adding_strategy.s_content)

            adding_strategy.save()

            return redirect(reverse('whokillsit:strategies'))
    else:
        context = {
            'alert': 'alert',
            'wrong': 'Please login firstly!'
        }
        return render(request, 'login.html', context)


def strategy(request, s_id):
    user_id = request.session.get('user_id')
    if user_id:
        if request.method == 'GET':
            strategy_added = Strategy.objects.get(id=s_id)
            remarks = Remark.objects.filter(s_remark_id=s_id)
            data = {
                'strategy_added': strategy_added,
                'remarks': remarks,
            }
            return render(request, 'strategy.html', data)
        elif request.method == 'POST':
            remark = Remark()
            remark.s_remark = Strategy.objects.get(id=s_id)
            user = UserInfo.objects.get(id=user_id)
            remark.u_remark = user
            remark.r_name = user.u_name
            remark.r_content = request.POST.get('remark')

            remark.save()
            return redirect(request.path)
    else:
        context = {
            'alert': 'alert',
            'wrong': 'Please login firstly!'
        }
        return render(request, 'login.html', context)


def ranking(request):
    rankings = Ranking.objects.all()
    rankings.order_by('r_no')
    return render(request, 'ranking.html', locals())


def about(request):
    return render(request, 'about.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('un')
        password = request.POST.get('pwd')
        users = UserInfo.objects.filter(u_name=username)
        user = users.first()
        if user:
            if check_password(password, user.u_pwd):
                request.session['user_id'] = user.id
                return redirect(reverse('whokillsit:mine'))
            else:
                context = {
                    'alert': 'alert',
                    'wrong': 'Password is wrong!',
                }
                # return messages.success(request, 'Password is wrong!')
                return render(request, 'login.html', context)
        else:
            context = {
                'alert': 'alert',
                'wrong': 'Username is wrong!'
            }
            # return messages.success(request, 'Username is wrong!')
            return render(request, 'login.html', context)


def register(request):
    if request.method == "GET":

        return render(request, 'register.html')

    elif request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        icon = request.FILES.get("icon")

        name = request.POST.get("name")
        age = request.POST.getlist("age")
        sex = request.POST.get("sex")
        tel = request.POST.get("tel")
        intro = request.POST.get("intro")
        print(age)
        print(type(age))

        password = make_password(password)

        user = UserInfo()
        user.u_name = username
        user.u_pwd = password
        user.u_email = email
        user.u_img = icon

        person = PersonInfo()
        person.person = user
        person.p_name = name
        person.p_age = int(age[0])
        person.p_sex = sex
        person.p_tel = tel
        person.p_intro = intro

        user.save()
        person.save()

        return redirect(reverse("whokillsit:login"))


def mine(request):
    user_id = request.session.get('user_id')
    user = UserInfo.objects.get(id=user_id)
    person = PersonInfo.objects.get(person_id=user_id)
    data = {
        'id': user.id,
        'username': user.u_name,
        'icon': MEDIA_KEY_PREFIX + user.u_img.url,
        'response': user.u_response,
        'fans': user.u_fans,
        'name': person.p_name,
        'age': person.p_age,
        'sex': person.p_sex,
        'tel': person.p_tel,
        'intro': person.p_intro,
    }
    return render(request, 'mine.html', data)

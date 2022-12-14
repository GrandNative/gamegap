import string
import random

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from . import models
from operator import itemgetter
# Create your views here.


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def login_page(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        number = request.POST.get('number')
        username = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
        user = User.objects.create(username=username, first_name=name, last_name=number)
        user.save()
        login(request, user)
        return redirect(request.GET.get('next'))
    else:
        context = {}
        return render(request, "login.html", context)


@login_required(login_url='login')
def panel(request):
    first_q = models.Question.objects.all().first()
    if not first_q.is_start:
        return render(request, 'start_page.html', {})
    if is_ajax(request=request):
        user = request.user
        print(user.username)
        q_num = request.POST.get('q_num')
        answer_id = request.POST.get('answer_id')
        print(answer_id)
        print(q_num)
        print(request)
        answer = models.Answer.objects.get(id=answer_id)
        if answer.is_true:
            is_true = True
        else:
            is_true = False
        now_question = models.Question.objects.get(id=q_num)
        user_rate = models.UserRate.objects.create(
            question=now_question,
            user=user,
            is_true=is_true,
        )
        user_rate.save()
        now_question.active = False
        now_question.save()
        next_q_num = request.POST.get('next_q_num')
        try:
            next_question = models.Question.objects.get(id=next_q_num)
        except Exception as e:
            print('yesssssssss')
            context = {
                'last': 1,
            }
            return JsonResponse(context, safe=False)

        answer = models.Answer.objects.filter(question__id=next_question.id)
        answer_1 = {
            'title': answer[0].title,
            'id': answer[0].id,
        }
        answer_2 = {
            'title': answer[1].title,
            'id': answer[1].id,
        }
        answer_3 = {
            'title': answer[2].title,
            'id': answer[2].id,
        }
        answer_4 = {
            'title': answer[3].title,
            'id': answer[3].id,
        }
        context = {
            'answer_1': answer_1,
            'answer_2': answer_2,
            'answer_3': answer_3,
            'answer_4': answer_4,
            'question_title': next_question.title,
            'question_id': next_question.id,
            'last': 0,
        }
        return JsonResponse(context, safe=False)
    else:
        try:
            question = models.Question.objects.filter(active=True)[0]
            answer = models.Answer.objects.filter(question__id=question.id)
        except:
            return render(request, 'goodbye.html', {})
        c_list = []
        answer_1 = {
            'title': answer[0].title,
            'id': answer[0].id,
        }
        answer_2 = {
            'title': answer[1].title,
            'id': answer[1].id,
        }
        answer_3 = {
            'title': answer[2].title,
            'id': answer[2].id,
        }
        answer_4 = {
            'title': answer[3].title,
            'id': answer[3].id,
        }
        context = {
            'answer_1': answer_1,
            'answer_2': answer_2,
            'answer_3': answer_3,
            'answer_4': answer_4,
            'question_title': question.title,
            'question_id': question.id
        }
        return render(request, 'page.html', context)


def last_page(request):
    users = User.objects.all().exclude(username='admin')
    list1 = []
    for user in users:
        list1.append({
            'rates': models.UserRate.objects.filter(user=user, is_true=True).count(),
            'user_name': user.first_name,
            'user_number': user.last_name,
        })
    sorted_list = sorted(list1, key=lambda d: d['rates'], reverse=True)
    context = {
        'rates': sorted_list,
    }
    return render(request, 'end.html', context)

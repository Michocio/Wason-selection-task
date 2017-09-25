import csv
from random import randrange

from django.http import HttpResponse
from django.shortcuts import render
import json
from karty.models import CurrentSettings, User, Session, GIL_data, Task, Task_data, Task_presented, Card, Training
import datetime
from karty_projekt import settings
import random

def selection(request, mode, which):

    settings = CurrentSettings.objects.all()[0].settings


    trening =  request.session.get('how_many_training')
    if trening < 0:
        request.session['count'] = 0
        # Wszystkie zostają niewylosowane
        tasks = Task.objects.all()
        for i in tasks:
            i.used = False
            i.save()

        if(mode == '1'):
            request.session['how_many_training'] = 1
            trening = 1
        else:
            request.session['how_many_training'] = 2
            trening = 2

    ile = request.session.get('how_many_tasks')
    if ile < 0:
        request.session['how_many_tasks'] = settings.number_of_sets

    czy = 0
    if trening > 0:
        czy = 1
        if (which != '0'):
            #request.session['count'] += 1
            request.session['how_many_training'] -= 1
    else:
        if (which != '0'):
            request.session['count'] += 1
            request.session['how_many_tasks'] -= 1

    if request.session['how_many_tasks'] == 0:
        request.session['how_many_training'] = -1


    # Niewylosowane
    tasks = Task.objects.filter(used = False)
    x = randrange(tasks.count())
    if (which != '0'):
        tasks[x].used = True
        tasks[x].save()

    if(trening > 0):
        f = Training.objects.all()[0]
        if(request.session['how_many_training'] == 2):
            choosen = f.first
        else:
            choosen = f.second
    else:
        choosen = tasks[x]

    rule = choosen.rule
    description =choosen.description
    additional_description = choosen.additional_description
    task = choosen.task

    if(which == '0'):
        non_activity = settings.non_activity_time_cards_try
        duration = settings.duration_cards_try
    else:
        non_activity = settings.non_activity_time_cards
        duration = settings.number_of_sets

    cards = [choosen.card1, choosen.card2, choosen.card3, choosen.card4]
    random.shuffle(cards)

    left = request.session['how_many_tasks']
    return render(request, 'selection.html',{'training' : czy, 'count' : request.session['count'] - 1,
        'card1' : cards[0], 'card2' : cards[1],  'card3' : cards[2],  'card4' : cards[3],
                                            'left' : left,
                                             'duration': duration, 'which':which, 'non_activity': non_activity,
                                             'settings' : settings, 'mode' : mode,
                                             'description' : description, 'additional_description' : additional_description,
                                             'task' : task, 'rule' : rule, 'choosen' : choosen})

def main(request):
    request.session['how_many_tasks'] = -1
    request.session['how_many_training'] = -1
    return render(request, 'main.html')


def save_data(request):
    session = Session.objects.get(pk = request.POST['pk'])
    clicks = (request.POST['clicks'].replace("[","").replace("]","")).split(',')
    cards = (request.POST['cards'].replace("[","").replace("]","")).split(',')

    j = 0

    task = Task.objects.get(pk = int(request.POST['task_pk']))

    card1 = Card.objects.get(pk = request.POST['card1'])
    card2 = Card.objects.get(pk=request.POST['card2'])
    card3 = Card.objects.get(pk=request.POST['card3'])
    card4 = Card.objects.get(pk=request.POST['card4'])

    choosen = Task_presented(session=session, task= task, card1 = card1, card2= card2, card3 = card3, card4 = card4,
                             overall_time= float(request.POST['overall_time']), task_time= float(request.POST['task_time']))
    choosen.save()

    if (len(request.POST['clicks']) > 2):
        for i in clicks:
            Task_data(session = session, time = float(i), which = int(cards[j]), task=choosen).save()
            j+=1
    return HttpResponse(str(choosen.pk))


def data(request):
    session = Session.objects.get(pk = request.POST['pk'])
    clicks = (request.POST['clicks'].replace("[","").replace("]","")).split(',')

    if(len(request.POST['clicks']) == 2):
        return HttpResponse("OK")

    if 'task_pk' not in request.POST:
        for i in clicks:
            GIL_data(session=session, time=float(i), what=int(request.POST['what'])).save()
    else:
        y = Task_presented.objects.get(pk = request.POST['task_pk'])
        for i in clicks:
            GIL_data(session = session, time = float(i), what = int(request.POST['what']), task = y).save()
    return HttpResponse("OK")


def user(request, pilotaz):
    return render(request, 'user.html', {'pilotaz' : pilotaz})

def experimentator(request):
    return render(request, 'experimentator.html')

def session(request, which):
    settings = CurrentSettings.objects.all()[0].settings

    if(which == 0):
        non_activity = settings.non_activity_time_GIL_try
        duration = settings.duration_GIL_try
    else:
        non_activity = settings.non_activity_time_GIL
        duration = settings.duration_GIL

    return render(request, 'session.html', {"which" : which, "non_activity" : non_activity, 'duration' : duration})

def info(request, phase):
    session_pk = 0
    user = User.objects.all()[0]
    info = CurrentSettings.objects.all()[0]

    if request.method == 'GET' and phase == '1':
        if(request.GET.get('gender', 0) == '1'):
            gender = 'M'
        else:
            gender = 'F'

        age = request.GET.get('age', 7)
        nick = request.GET.get('nick', '')

        try:
            user = User.objects.get(nick = nick.lower())
        except:# Add new User if doesnt exists
            user = User(nick = nick.lower(), sex = gender, age = age)
            user.save()

        session = Session(user=user, info=info.settings)
        session.save()
        session_pk = session.pk

    settings = CurrentSettings.objects.all()[0].settings
    description = ""
    phase = int(phase)
    pilotaz = 0
    if (request.GET.get('pilotaz', 0) == '1'):
        pilotaz = 1
        description = settings.describtion_phase_5
    else:
        if phase == 0:
            description = settings.describtion_phase_1
        elif phase == 1:
            description = settings.describtion_phase_2
        elif phase == 2:
            description = settings.describtion_phase_3
        elif phase == 3:
            description = settings.describtion_phase_4
        elif phase == 4:
            description = settings.describtion_phase_5

    return render(request, 'info.html', {'pilotaz' : pilotaz,
        'session': session_pk, 'phase' : phase, 'description' : description, 'nick' : user.nick, 'age' : user.age, 'gender' : user.sex})
# Create your views here.

def dane(request):
    users = User.objects.all()
    print(users)
    return render(request, 'dane.html', {'users':users})


def excel(request, id):
    user = User.objects.get(pk = id)
    session = Session.objects.filter(user=user)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="raport.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nick' + ' ' + user.nick])
    writer.writerow(['Wiek' + ' ' + str(user.age)])
    writer.writerow(['Plec' + ' ' + user.sex])
    writer.writerow([''])

    for s in session:
        writer.writerow(['Sesja' + ' ' + str(s.pk) + ' ' + str(s.startTime)])
        arkusz = Task_presented.objects.filter(session = s)
        gil = GIL_data.objects.filter(session= s, what = 0)
        writer.writerow(['GIL_dane:'])
        for g in gil:
            writer.writerow([str(g.time)])
        writer.writerow([' '])
        writer.writerow([' '])
        writer.writerow(['Selekcja_dane:'])

        for a in arkusz:
            writer.writerow(['Numeracja_zadania Overall_Time Task_time Karta1 Karta2 Karta3 Karta4'])
            writer.writerow([str(a.pk) +' ' +  str(a.overall_time) +' ' + str(a.task_time) + ' ' + str(a.card1.logic)
                             +' ' + str(a.card2.logic)+ ' '+ str(a.card3.logic) +' ' + str(a.card4.logic)])
            writer.writerow(['GIL_dane:'])
            gil2 = GIL_data.objects.filter(session= s, what = 1, task = a)
            for i in gil2:
                writer.writerow([str(i.time)])
            writer.writerow(['Klikanie_kart_dane:'])
            klik = Task_data.objects.filter(session=s, which=1, task=a)
            cards = [0, 0, 0, 0]
            for k in klik:
                if(cards[k.which] == 1):
                    cards[k.which] = 0
                else:
                    cards[k.which] = 1
                writer.writerow([str(k.which) + ' ' + str(k.time)])
            writer.writerow(['Ostateczny_stan_kart:'])
            writer.writerow([str(cards[0]) + ',' + str(cards[1]) +','+ str(cards[2]) +',' + str(cards[3])])
            writer.writerow(['Poprawnosc:'])
            czy = True
            if(a.card1.logic == 'P' and cards[0] == 0):
                czy = False
            if (a.card2.logic == 'P' and cards[0] == 0):
                czy = False
            if (a.card2.logic == 'P' and cards[0] == 0):
                czy = False
            if (a.card2.logic == 'P' and cards[0] == 0):
                czy = False
            if (a.card2.logic == 'P' and cards[0] == 0):
                czy = False

            if (a.card1.logic == 'nQ' and cards[0] == 0):
                czy = False
            if (a.card2.logic == 'nQ' and cards[0] == 0):
                czy = False
            if (a.card2.logic == 'nQ' and cards[0] == 0):
                czy = False
            if (a.card2.logic == 'nQ' and cards[0] == 0):
                czy = False
            if (a.card2.logic == 'nQ' and cards[0] == 0):
                czy = False
            writer.writerow([str(czy)])
            writer.writerow(['_________ ________ ___________ _______ _______ ______ _________'])
    return response
from django.db import models
from django.utils import timezone


class ExperimentSettings(models.Model):
    describtion_phase_1 = models.TextField(max_length=1000, default="", verbose_name="Wiadomość powitalna")

    describtion_phase_2 = models.TextField(max_length=1000, default="", verbose_name="Instrukcja fazy GIL treningowej")
    non_activity_time_GIL_try = models.IntegerField(default=10, verbose_name="Dozwolony czas braku aktywności fazy GIL treningowej")
    duration_GIL_try = models.IntegerField(default=25, verbose_name="Czas trwania fazy GIL treningowej")

    describtion_phase_3 = models.TextField(max_length=1000, default="",  verbose_name="Instrukcja fazy GIL pomiarowej")
    non_activity_time_GIL = models.IntegerField(default=10,verbose_name="Dozwolony czas braku aktywności fazy GIL pomiarowej")
    duration_GIL = models.IntegerField(default=25, verbose_name="Czas trwania fazy GIL pomiarowej")

    describtion_phase_4 = models.TextField(max_length=1000, default="", verbose_name="Instrukcja fazy GIL wraz z wyborem kart - trening")
    non_activity_time_cards_try = models.IntegerField(default=10, verbose_name="Dozwolony czas braku aktywności fazy GIL wraz z wyborem kart - trening")
    duration_cards_try = models.IntegerField(default=25, verbose_name="Czas trwania fazy GIL wraz z wyborem kart - trening")

    describtion_phase_5 = models.TextField(max_length=1000, default="", verbose_name="Instrukcja fazy GIL wraz z wyborem kart - pomiar")
    non_activity_time_cards = models.IntegerField(default=10,verbose_name="Dozwolony czas braku aktywności fazy GIL wraz z wyborem kart - pomiar")
    number_of_sets = models.IntegerField(default=25, verbose_name="Liczba zadań fazy GIL wraz z wyborem kart - pomiar")
    number_of_training_sets = models.IntegerField(default=2, verbose_name="Liczba zadań fazy traningowej GIL wraz z wyborem kart - pomiar")

    GROUP_TYPE_1 = '1'
    GROUP_TYPE_2 = '2'
    GROUP_TYPE_3 = '3'
    GROUP_TYPE = (
        (GROUP_TYPE_1, 'Grupa kontrolna'),
        (GROUP_TYPE_2, 'Grupa eksperymentalna pierwsza'),
        (GROUP_TYPE_3, 'Grupa eksperymentalna druga'),
    )
    group_type = models.CharField(
        max_length=1,
        choices=GROUP_TYPE,
        default='1',
    )

    def __str__(self):
        return "Ustawienia eksperymentu "

    class Meta:
        verbose_name = "Ustawienia eksperymentu"
        verbose_name_plural = "Ustawienia eksperymentu"


class CurrentSettings(models.Model):


    settings = models.ForeignKey(ExperimentSettings)

    def __str__(self):
        return "Obecne ustawienia eksperymentu"

    class Meta:
        verbose_name = "Obecne ustawienia eksperymentu"
        verbose_name_plural = "Obecne ustawienia eksperymentu"


class User(models.Model):
    nick = models.CharField(max_length=30, default='anonim')
    age = models.IntegerField(default = 77)
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    )
    sex = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='F',
    )

    def __str__(self):
        return "%s" % ( self.nick)


class Session(models.Model):
    startTime = models.DateTimeField(default=timezone.now)
    endTime = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('User', default=0)
    info = models.ForeignKey(ExperimentSettings)

    def __str__(self):
        return "%s %s %s" % (self.pk, str(self.startTime), self.user.nick)



class Card(models.Model):
    text = models.CharField(max_length=100, default='Karta')

    P = 'P'
    NON_P = 'nP'
    Q = 'Q'
    NON_Q = 'nQ'
    LOGIC_TYPE = (
        (P, 'P'),
        (NON_P , 'NON-P'),
        (Q, 'Q'),
        (NON_Q, 'NON-Q'),
    )

    logic = models.CharField(
        max_length=2,
        choices=LOGIC_TYPE,
        default='P',
    )

    def __str__(self):
        return "%s %s" % ( self.text, self.logic)

class Task(models.Model):
    description = models.TextField(max_length=100000, default='Historyjka')
    additional_description = models.TextField(max_length=100000, default='Dodatkowy opis kart')
    task = models.TextField(max_length=100000, default='Zadanie')
    rule = models.TextField(max_length=100000, default='Reguła')
    used = models.BooleanField(default=0)

    card1 = models.ForeignKey(Card, related_name='%(class)s_requests_created', default='0')
    card2 = models.ForeignKey(Card, related_name='%(class)s_requests_created2', default='0')
    card3 = models.ForeignKey(Card, related_name='%(class)s_requests_created3', default='0')
    card4 = models.ForeignKey(Card, related_name='%(class)s_requests_created4', default='0')

    def __str__(self):
        return "%s" % (self.rule)

    class Meta:
        verbose_name = "Zadanie"
        verbose_name_plural = "Zadania"

class Task_presented(models.Model):
    session = models.ForeignKey(Session, default='0')
    task = models.ForeignKey(Task, default='0')

    overall_time = models.FloatField(default=0.0)
    task_time = models.FloatField(default=0.0)

    card1 = models.ForeignKey(Card, related_name='%(class)s_requests_created', default='0')
    card2 = models.ForeignKey(Card, related_name='%(class)s_requests_created2', default='0')
    card3 = models.ForeignKey(Card, related_name='%(class)s_requests_created3', default='0')
    card4 = models.ForeignKey(Card, related_name='%(class)s_requests_created4', default='0')

    def __str__(self):
        return "%d %s %d" % ((self.session.pk),( self.session.user.nick), (self.task.pk))


class GIL_data(models.Model):
    session = models.ForeignKey(Session, default='0')
    time =  models.FloatField(default=0.0)
    what = models.IntegerField(default = 0)
    task = models.ForeignKey(Task_presented, default = 0)

    def __str__(self):
        return "%d %s %f" % ((self.session.pk),( self.session.user.nick), self.time)


class Task_data(models.Model):
    session = models.ForeignKey(Session, default='0')
    time =  models.FloatField(default=0.0)
    which =  models.IntegerField(default = 0)
    task = models.ForeignKey(Task_presented, default = 0)

    def __str__(self):
        return "%d %s %f %d" % ((self.session.pk),( self.session.user.nick), self.time, (self.which))

class Training(models.Model):
    first = models.ForeignKey(Task, related_name='%(class)s_requests_created', default='0')
    second = models.ForeignKey(Task, related_name='%(class)s_requests_created2', default='0')


    class Meta:
        verbose_name = "Zadanie treningowe"
        verbose_name_plural = "Zadania treningowe"
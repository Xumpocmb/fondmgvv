from django.db.models import Case, When, Value, IntegerField
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from app_club.models import ClubRegion, Club
from app_home.forms import ContactForm
from app_news.models import News


def index(request):
    club_regions = ClubRegion.objects.all().order_by(
        Case(
            When(id=5, then=Value(0)),
            default=Value(1),
            output_field=IntegerField(),
        ), 'id')
    all_clubs = Club.objects.all()
    all_news = News.objects.all()
    context = {
        'all_clubs': all_clubs,
        'club_regions': club_regions,
        'all_news': all_news
    }
    return render(request, 'app_home/index.html', context)


def get_document(request):
    return render(request, 'app_home/document.html')

def custom_404_view(request, exception):
    return render(request, 'app_home/404.html')


def send_question_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                'Вопрос с сайта',
                f'Имя: {name}\nEmail: {email}\n\nСообщение:\n{message}',
                'fondmgvv@yandex.by',  # Отправитель
                ['fondmgvv@yandex.by'],  # Получатель
                fail_silently=False,
            )
            print("Email sent successfully")
            return redirect(request.path)
        else:
            print("Form is not valid")
    return redirect('app_home:home')
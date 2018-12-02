from django.shortcuts import render

def index(request):
    return render(request, 'food/home.html')

def contact(request):
    return render(request, 'food/contact.html', {'content': ["If you would like to order by phone or contact us by email, please", "wsiz@students.pl", "+48111111111"]})
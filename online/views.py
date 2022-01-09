from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request, 'about.html')
def buslist(request):
    return render(request, 'bus-list.html')
def bus(request):
    return render(request, 'bus.html')
def contact(request):
    return render(request, 'contact.html')
def faq(request):
    return render(request, 'faq.html')
def feedback(request):
    return render(request, 'feedback.html')
def icons(request):
    return render(request, 'icons.html')
def movies(request):
    return render(request, 'movies.html')
def pay(request):
    return render(request, 'pay.html')
def plans(request):
    return render(request, 'plans.html')
def selectshow(request):
    return render(request, 'select-show.html')
def shortcodes(request):
    return render(request, 'shortcodes.html')
def sitemap(request):
    return render(request, 'sitemap.html')
def support(request):
    return render(request, 'support.html')
def terms(request):
    return render(request, 'terms.html')
def train(request):
    return render(request, 'train.html')
def trainslist(request):
    return render(request, 'trains-list.html')
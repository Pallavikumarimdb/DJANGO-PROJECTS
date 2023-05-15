from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("This is home Page")
    context={
        "variable" : "this is Pallavi"
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')

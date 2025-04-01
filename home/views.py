from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    peoples = [
        {'name':'Shyam','age':'20'},
        {'name':'Sharman','age':'19'},
        {'name':'Abhi','age':'20'},
        {'name':'John','age':'19'},
    ]
    return render(request, "index.html",context={'peoples':peoples})
def success_page(request):
    print("*"*10)
    return HttpResponse("<h1> Hey this is a success page </h1>")
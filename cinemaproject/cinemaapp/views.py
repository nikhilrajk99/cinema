from django.http import HttpResponse
from django.shortcuts import render

from cinemaapp.models import Cinema


# Create your views here.
def index(request):
    obj=Cinema.objects.all()
    return render(request,"index.html",{'result':obj})

def detail(request, movie_id):
    movie=Cinema.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        movie=Cinema(name=name,desc=desc,year=year,img=img)

    return render(request,"add.html")

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     multi=x*y
#     div=x/y
#     return render(request,"result.html",{'subtraction':sub,'addition':add,'multiplication':multi,'division':div})
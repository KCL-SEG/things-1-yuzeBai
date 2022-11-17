from django.shortcuts import render

def simpleHome(request):
    return render(request,'simpleHome.html')

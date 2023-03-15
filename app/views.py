from django.shortcuts import render
def conditions(request):
    d={'a':9,'b':20,'c':30}
    return render(request,'conditions.html',context=d)

# Create your views here.
def loops(request):
    d={'name':'doremon'}
    return render(request,'loops.html',context=d)

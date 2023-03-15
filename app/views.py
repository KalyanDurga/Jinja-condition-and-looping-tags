from django.shortcuts import render

# Create your views here.
def if_condition(request):
    d={'a':1001,'b':200}
    return render(request,'if_condition.html',d)

def if_else_condition(request):
    d={'a':201,'b':207}
    return render(request,'if_else_condition.html',d)

def elif_condition(request):
    d={'a':201,'b':247,'c':207}
    return render(request,'elif_condition.html',d)

def nested_if_condition(request):
    d={'a':201,'b':247,'c':2070}
    return render(request,'nested_if_condition.html',d)

def for_loop(request):
    d={'name':'i am groot'}
    return render(request,'for_loop.html',d)

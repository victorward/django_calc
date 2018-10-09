from django.shortcuts import render
from django.http import JsonResponse
from calculator.models import Calculations
from calculator.operations import *
import time


# Create your views here.
def index(request):
    return render(request, 'index.html')


def history(request):
    data = Calculations.objects.all()
    return render(request, 'history.html', {'calculations': data})


def equate(request):
    curr = float(request.POST.get("curr", '0'))
    ans = float(request.POST.get("ans", '0'))
    oper = request.POST.get("oper")
    cal = Calculations(timestamp=time.time(), operand1=ans, operator=oper, operand2=curr)
    cal.save()
    if request.POST:
        if oper == '+':
            ans = add(curr, ans)
        elif oper == '-':
            ans = minus(ans, curr)
        elif oper == '*':
            ans = multiplication(curr, ans)
        elif oper == "%":
            ans = mod(ans, curr)
        elif oper == '/':
            if curr != 0:
                ans = division(ans, curr)
            else:
                ans = 'Division by zero is invalid'
        return JsonResponse({'ans': ans})

from django.shortcuts import render, redirect
from django.http import JsonResponse
from calculator.models import Calculations
from calculator.operations import *
from django.utils import timezone, dateparse

current_session_timestamp = None


# Create your views here.
def index(request):
    global current_session_timestamp
    current_session_timestamp = timezone.now()
    return render(request, 'index.html')


def history(request):
    data = Calculations.objects.all()
    print("history data {}".format(data))
    return render(request, 'history.html', {'calculations': data})


def current_session(request):
    data = Calculations.objects.filter(timestamp__gt=current_session_timestamp)
    return render(request, 'history.html', {'calculations': data})


def filter_history_by_date(request, date):
    parsed_date = dateparse.parse_date(date)
    data = Calculations.objects.filter(
        timestamp__year=parsed_date.year,
        timestamp__month=parsed_date.month,
        timestamp__day=parsed_date.day
    )
    print("data {}".format(data))
    return render(request, 'history.html', {'calculations': data})


def equate(request):
    operand1 = float(request.POST.get("ans", '0'))
    operand2 = float(request.POST.get("curr", '0'))
    oper = request.POST.get("oper")
    ans = 0.0
    if request.POST:
        if oper == '+':
            ans = add(operand2, operand1)
        elif oper == '-':
            ans = minus(operand1, operand2)
        elif oper == '*':
            ans = multiplication(operand2, operand1)
        elif oper == "%":
            ans = mod(operand1, operand2)
        elif oper == '/':
            ans = division(operand1, operand2)

        cal = Calculations(timestamp=timezone.now(), operand1=operand1, operator=oper, operand2=operand2, result=ans)
        cal.save()
        return JsonResponse({'ans': ans})

import os
import subprocess
import tempfile
from django.shortcuts import render, redirect
from .models import Autotest
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib import messages
from django.contrib.auth.models import User
from .utils import clean_code

# Create your views here.
def index(request):
    tests = Autotest.objects.all()
    context = {
        'tests': tests,  # Передаем переменную tests в шаблон
    }
    return render(request, 'saveAutotests/index.html', context)


def save_autotests(request):
    if request.method == 'POST':
        test_file = request.FILES.get('testFile')
        test_name = request.POST.get('testName')

        if test_file and test_name:
            try:
                user = User.objects.get(username="testuser")
                test = Autotest(name=test_name, code=test_file.read().decode('utf-8'), author=user)
                test.save()

                messages.success(request, 'Тест успешно сохранен')
            except Exception as e:
                messages.error(request, f'Ошибка сохранения теста: {e}')
        else:
            messages.error(request, 'Заполните все поля')

        return redirect('save_autotests')

    return render(request, 'saveAutotests/uploadAutotests.html')

def run_autotest(request, test_id):
    return render(request, 'saveAutotests/uploadAutotests.html')

def see_autotest(request, test_id):
    return render(request, 'saveAutotests/uploadAutotests.html')
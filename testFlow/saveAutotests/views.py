import os
import subprocess
import tempfile
from django.shortcuts import render, redirect
from .models import Autotest
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'saveAutotests/index.html')


def save_autotests(request):
    if request.method == 'POST':
        test_file = request.FILES.get('testFile')
        test_name = request.POST.get('testName')

        if test_file and test_name:
            try:
                test = Autotest(name=test_name, code=test_file.read().decode('utf-8'))  # Сохраняем сжатые данные
                test.save()

                messages.success(request, 'Тест успешно сохранен')
            except Exception as e:
                messages.error(request, f'Ошибка сохранения теста: {e}')
        else:
            messages.error(request, 'Заполните все поля')

        return redirect('save_autotests')


    return render(request, 'saveAutotests/uploadAutotests.html')
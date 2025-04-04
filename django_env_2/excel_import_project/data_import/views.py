
# data_import/views.py

import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UploadFileForm
from .models import Book
from datetime import datetime

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)
            for _, row in df.iterrows():
                book, created = Book.objects.get_or_create(
                    title=row['Title'],
                    author=row['Author'],
                    publication_date = row['Publication Date'].to_pydatetime()
                )
                if created:
                    messages.success(request, f'Successfully imported {book.title}')
                else:
                    messages.warning(request, f'{book.title} already exists')
            return redirect('upload_file')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})






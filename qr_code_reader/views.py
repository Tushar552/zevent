# qr_code_reader/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import qrcode
import os

@login_required
def read_qr_code(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        # Generate QR code
        qr = qrcode.make(data)
        # Save QR code to media directory
        qr_file_path = 'media/qrcode.png'
        qr.save(qr_file_path)
        # Redirect to view the generated QR code
        return redirect('view_qr_code')
    return render(request, 'qr_code_reader/read_qr_code.html')

@login_required
def view_qr_code(request):
    qr_file_path = 'media/qrcode.png'
    if os.path.exists(qr_file_path):
        with open(qr_file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='image/png')
            response['Content-Disposition'] = 'inline; filename=' + qr_file_path
            return response
    else:
        return HttpResponse("QR code not found.")

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
import qrcode
import os
import json

@login_required(login_url='login')
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

@login_required(login_url='login')
def view_qr_code(request):
    qr_file_path = 'media/qrcode.png'
    if os.path.exists(qr_file_path):
        with open(qr_file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='image/png')
            response['Content-Disposition'] = 'inline; filename=' + qr_file_path
            return response
    else:
        return HttpResponse("QR code not found.")

@login_required(login_url='login')
def qr_code_scanner(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            qr_data = data.get('data')
            # Example processing: just printing the data
            print('QR code data:', qr_data)
            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)
    return render(request, 'qr_code_reader/qr_code_scanner.html')


    
@login_required(login_url='login')
def success_page(request):
    return render(request, 'qr_code_reader/success_page.html')
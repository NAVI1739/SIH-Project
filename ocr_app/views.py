from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import pytesseract
from PIL import Image
import os
import pytesseract

# Example path for Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Example path for Linux (if it's not in your PATH)
# pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'


def upload_and_scan_image(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        
        if not uploaded_file:
            return JsonResponse({'error': 'No file uploaded'}, status=400)

        # Create a path in the media directory
        file_name = uploaded_file.name
        file_path = default_storage.save(f'temp/{file_name}', ContentFile(uploaded_file.read()))

        try:
            # Perform OCR processing on the image
            with default_storage.open(file_path) as image_file:
                text = pytesseract.image_to_string(Image.open(image_file))
            
            # Return the extracted text as a JSON response
            return JsonResponse({'extracted_text': text})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

        finally:
            # Delete the file after processing
            if default_storage.exists(file_path):
                default_storage.delete(file_path)

    # If the request method is GET, render the upload form
    return render(request, 'upload.html')

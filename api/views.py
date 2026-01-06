"""
API Views for ASCII Image Converter
"""

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render
import json
from .ascii_converter import convert_image_to_ascii


def index(request):
    """
    Display the web interface for the ASCII converter.
    """
    return render(request, 'index.html')


@csrf_exempt
@require_http_methods(["POST"])
def convert_to_ascii(request):
    """
    API endpoint to convert an uploaded image to ASCII art.
    
    POST parameters:
        - image: Image file (required)
        - width: Width of ASCII art in characters (optional, default: 100)
        - format: Response format - 'json' or 'text' (optional, default: 'json')
    
    Returns:
        JSON response with ASCII art or plain text
    """
    try:
        # Check if image file is present
        if 'image' not in request.FILES:
            return JsonResponse({
                'error': 'No image file provided',
                'message': 'Please upload an image file using the "image" field'
            }, status=400)
        
        image_file = request.FILES['image']
        
        # Get optional width parameter
        width = request.POST.get('width', '100')
        try:
            width = int(width)
            if width < 10 or width > 500:
                return JsonResponse({
                    'error': 'Invalid width',
                    'message': 'Width must be between 10 and 500'
                }, status=400)
        except ValueError:
            return JsonResponse({
                'error': 'Invalid width',
                'message': 'Width must be an integer'
            }, status=400)
        
        # Get format preference
        response_format = request.POST.get('format', 'json').lower()
        
        # Convert image to ASCII
        try:
            ascii_art = convert_image_to_ascii(image_file, width)
        except Exception as e:
            return JsonResponse({
                'error': 'Image conversion failed',
                'message': str(e)
            }, status=400)
        
        # Return response based on format
        if response_format == 'text':
            return HttpResponse(ascii_art, content_type='text/plain')
        else:
            return JsonResponse({
                'success': True,
                'ascii_art': ascii_art,
                'width': width,
                'lines': len(ascii_art.split('\n'))
            })
    
    except Exception as e:
        return JsonResponse({
            'error': 'Server error',
            'message': str(e)
        }, status=500)


def api_info(request):
    """
    Display API information and usage instructions.
    """
    info = {
        'name': 'ASCII Image Converter API',
        'version': '1.0',
        'endpoints': {
            '/api/convert/': {
                'method': 'POST',
                'description': 'Convert an image to ASCII art',
                'parameters': {
                    'image': {
                        'type': 'file',
                        'required': True,
                        'description': 'Image file to convert'
                    },
                    'width': {
                        'type': 'integer',
                        'required': False,
                        'default': 100,
                        'range': '10-500',
                        'description': 'Width of ASCII art in characters'
                    },
                    'format': {
                        'type': 'string',
                        'required': False,
                        'default': 'json',
                        'options': ['json', 'text'],
                        'description': 'Response format'
                    }
                },
                'example_curl': 'curl -X POST -F "image=@photo.jpg" -F "width=120" http://localhost:8000/api/convert/'
            }
        },
        'usage_examples': [
            {
                'description': 'Basic conversion with default width',
                'curl': 'curl -X POST -F "image=@myimage.jpg" http://localhost:8000/api/convert/'
            },
            {
                'description': 'Custom width (150 characters)',
                'curl': 'curl -X POST -F "image=@myimage.jpg" -F "width=150" http://localhost:8000/api/convert/'
            },
            {
                'description': 'Get plain text response',
                'curl': 'curl -X POST -F "image=@myimage.jpg" -F "format=text" http://localhost:8000/api/convert/'
            }
        ]
    }
    
    return JsonResponse(info, json_dumps_params={'indent': 2})

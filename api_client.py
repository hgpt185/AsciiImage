"""
Sample Python client to test the ASCII Image Converter API
"""

import requests
import sys


def convert_image_via_api(image_path, width=100, format='json', api_url='http://localhost:8000/api/convert/'):
    """
    Convert an image to ASCII art using the API.
    
    Args:
        image_path: Path to the image file
        width: Width of ASCII art in characters
        format: Response format ('json' or 'text')
        api_url: API endpoint URL
    
    Returns:
        ASCII art string or response JSON
    """
    try:
        # Open and send the image file
        with open(image_path, 'rb') as image_file:
            files = {'image': image_file}
            data = {
                'width': str(width),
                'format': format
            }
            
            print(f"Sending request to {api_url}...")
            response = requests.post(api_url, files=files, data=data)
            
            if response.status_code == 200:
                if format == 'text':
                    return response.text
                else:
                    return response.json()
            else:
                error_data = response.json()
                raise Exception(f"API Error: {error_data.get('message', 'Unknown error')}")
    
    except FileNotFoundError:
        raise Exception(f"Image file not found: {image_path}")
    except requests.exceptions.ConnectionError:
        raise Exception("Could not connect to API. Make sure the server is running.")
    except Exception as e:
        raise Exception(f"Error: {str(e)}")


def get_api_info(api_url='http://localhost:8000/api/info/'):
    """
    Get API information and usage details.
    """
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to get API info")
    except requests.exceptions.ConnectionError:
        raise Exception("Could not connect to API. Make sure the server is running.")


def main():
    """
    Example usage of the API client.
    """
    if len(sys.argv) < 2:
        print("Usage: python api_client.py <image_path> [width] [format]")
        print("\nExample:")
        print("  python api_client.py photo.jpg 120 text")
        print("\nOr get API info:")
        print("  python api_client.py --info")
        sys.exit(1)
    
    if sys.argv[1] == '--info':
        print("Fetching API information...\n")
        try:
            info = get_api_info()
            import json
            print(json.dumps(info, indent=2))
        except Exception as e:
            print(f"Error: {e}")
        sys.exit(0)
    
    # Parse command line arguments
    image_path = sys.argv[1]
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    format_type = sys.argv[3] if len(sys.argv) > 3 else 'text'
    
    try:
        # Convert the image
        result = convert_image_via_api(image_path, width, format_type)
        
        if format_type == 'json':
            import json
            print("\n" + "="*50)
            print("API Response (JSON):")
            print("="*50)
            print(json.dumps(result, indent=2))
            print("\n" + "="*50)
            print("ASCII Art:")
            print("="*50)
            print(result.get('ascii_art', ''))
        else:
            print("\n" + "="*50)
            print("ASCII Art:")
            print("="*50)
            print(result)
        
        print("\n✓ Conversion successful!")
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()


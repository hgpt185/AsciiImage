# ASCII Image Converter

A Python application that converts regular images into ASCII art. Now includes both a command-line script and a Django REST API!

## Features

- **Command-line tool**: Convert images to ASCII art from the terminal
- **REST API**: Web server with API endpoints for image conversion
- Customizable output width
- Maintains aspect ratio
- Multiple output formats (JSON or plain text)
- Supports all common image formats (JPEG, PNG, GIF, WebP, etc.)

---

## Installation

1. Clone or download this repository

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Option 1: Command-line Script

#### Basic usage (display in terminal):

```bash
python ascii_image.py your_image.jpg
```

#### Save to a text file:

```bash
python ascii_image.py your_image.jpg -o output.txt
```

#### Customize width (in characters):

```bash
python ascii_image.py your_image.jpg -w 150
```

#### Command-line Options:

- `image` - Path to the input image file (required)
- `-w, --width` - Width of the ASCII art in characters (default: 100)
- `-o, --output` - Output file path (if not specified, prints to console)

---

### Option 2: Django REST API

#### Starting the Server

1. Run Django migrations (first time only):

```bash
python manage.py migrate
```

2. Start the development server:

```bash
python manage.py runserver
```

The server will start at `http://localhost:8000`

#### API Endpoints

##### GET `/api/`
Returns API information and usage instructions.

**Example:**
```bash
curl http://localhost:8000/api/
```

##### POST `/api/convert/`
Convert an uploaded image to ASCII art.

**Parameters:**
- `image` (file, required) - The image file to convert
- `width` (integer, optional) - Width of ASCII art in characters (default: 100, range: 10-500)
- `format` (string, optional) - Response format: `json` or `text` (default: json)

**Examples:**

1. Basic conversion (returns JSON):
```bash
curl -X POST -F "image=@photo.jpg" http://localhost:8000/api/convert/
```

2. Custom width:
```bash
curl -X POST -F "image=@photo.jpg" -F "width=150" http://localhost:8000/api/convert/
```

3. Get plain text response:
```bash
curl -X POST -F "image=@photo.jpg" -F "format=text" http://localhost:8000/api/convert/
```

4. Save output to file:
```bash
curl -X POST -F "image=@photo.jpg" -F "format=text" http://localhost:8000/api/convert/ > ascii_art.txt
```

**JSON Response Format:**
```json
{
  "success": true,
  "ascii_art": "@@@###SSS%%%...",
  "width": 100,
  "lines": 56
}
```

**Error Response Format:**
```json
{
  "error": "Error type",
  "message": "Detailed error message"
}
```

#### Using with Python requests library:

```python
import requests

# Convert image
with open('myimage.jpg', 'rb') as f:
    files = {'image': f}
    data = {'width': 120}
    response = requests.post('http://localhost:8000/api/convert/', files=files, data=data)

result = response.json()
if result.get('success'):
    print(result['ascii_art'])
```

#### Using with JavaScript (browser):

```javascript
const formData = new FormData();
formData.append('image', fileInput.files[0]);
formData.append('width', '120');

fetch('http://localhost:8000/api/convert/', {
    method: 'POST',
    body: formData
})
.then(response => response.json())
.then(data => {
    if (data.success) {
        console.log(data.ascii_art);
    }
});
```

---

## Project Structure

```
AsciiImage/
├── ascii_image.py          # Command-line script
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── asciiserver/          # Django project settings
│   ├── __init__.py
│   ├── settings.py       # Django settings
│   ├── urls.py          # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
└── api/                  # API application
    ├── __init__.py
    ├── views.py          # API endpoints
    ├── urls.py          # API URL routes
    ├── ascii_converter.py # Core conversion logic
    ├── models.py
    ├── apps.py
    └── migrations/
```

---

## How It Works

1. **Load Image**: Opens the input image using PIL/Pillow
2. **Convert to Grayscale**: Simplifies the image to brightness values
3. **Resize**: Adjusts the image size to match the desired character width
4. **Map to ASCII**: Each pixel's brightness is mapped to an ASCII character
   - Darker pixels → denser characters (`@`, `#`, `S`)
   - Lighter pixels → sparse characters (`.`, `,`, ` `)
5. **Output**: Returns or displays the resulting ASCII art

---

## ASCII Character Set

The script uses the following characters from darkest to lightest:

```
@ # S % ? * + ; : , .
```

---

## Tips for Best Results

- **Image contrast**: Use images with good contrast for better results
- **Width settings**:
  - Start with 100-150 characters for most images
  - Use 50-80 for simple images or icons
  - Use 150-200 for detailed images
- **Image selection**: Portrait-style images and images with clear subjects work best
- **Terminal display**: Some terminals may not display all characters with equal spacing

---

## API Rate Limiting & Production

This is a development server. For production use:

1. Set `DEBUG = False` in `settings.py`
2. Configure `ALLOWED_HOSTS` in `settings.py`
3. Use a production WSGI server (gunicorn, uWSGI)
4. Set up proper file upload limits
5. Implement rate limiting
6. Use environment variables for secret keys

---

## Dependencies

- **Pillow** (>=10.0.0) - Image processing library
- **Django** (>=4.2.0) - Web framework

---

## License

Free to use and modify.

---

## Examples

### Command Line:
```bash
$ python ascii_image.py monaLisa.webp -w 80
Converting 'monaLisa.webp' to ASCII art...

@@@@@@###SSSS%%%???***+++;;;:::,,,...
@@@@###SSS%%%???***+++;;;:::,,,....
...
```

### API:
```bash
$ curl -X POST -F "image=@monaLisa.webp" -F "width=80" http://localhost:8000/api/convert/
{
  "success": true,
  "ascii_art": "@@@@@@###SSSS...",
  "width": 80,
  "lines": 60
}
```

# Quick Start Guide - ASCII Image Converter API

## 🚀 Getting Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run Database Migrations (First Time Only)
```bash
python manage.py migrate
```

### Step 3: Start the Server
```bash
python manage.py runserver
```

The server will start at `http://localhost:8000`

---

## 🎯 Using the API

### Option 1: Web Interface (Easiest)

Open your browser and go to:
```
http://localhost:8000/api/
```

You'll see a beautiful web interface where you can:
- Upload an image
- Adjust the ASCII width
- View the result instantly
- Copy to clipboard

### Option 2: Command Line with curl

**Basic conversion:**
```bash
curl -X POST -F "image=@myimage.jpg" http://localhost:8000/api/convert/
```

**With custom width:**
```bash
curl -X POST -F "image=@myimage.jpg" -F "width=150" http://localhost:8000/api/convert/
```

**Get plain text output:**
```bash
curl -X POST -F "image=@myimage.jpg" -F "format=text" http://localhost:8000/api/convert/
```

**Save to file:**
```bash
curl -X POST -F "image=@myimage.jpg" -F "format=text" http://localhost:8000/api/convert/ > ascii_art.txt
```

### Option 3: Python Client Script

Use the included Python client:

```bash
# Basic usage (displays ASCII art)
python api_client.py myimage.jpg

# Custom width
python api_client.py myimage.jpg 150

# Get JSON response
python api_client.py myimage.jpg 100 json

# Get API info
python api_client.py --info
```

### Option 4: Python Code

```python
import requests

# Open and convert image
with open('myimage.jpg', 'rb') as f:
    files = {'image': f}
    data = {'width': 120, 'format': 'text'}
    response = requests.post('http://localhost:8000/api/convert/', files=files, data=data)

# Display result
if response.status_code == 200:
    print(response.text)
```

---

## 📝 API Endpoints

### `GET /api/`
Web interface for interactive conversion

### `GET /api/info/`
Get API documentation in JSON format

### `POST /api/convert/`
Convert an image to ASCII art

**Parameters:**
- `image` (file, required) - Image file to convert
- `width` (integer, optional) - ASCII width (10-500, default: 100)
- `format` (string, optional) - Response format: 'json' or 'text' (default: 'json')

**Response (JSON format):**
```json
{
  "success": true,
  "ascii_art": "@@@###SSS%%%...",
  "width": 100,
  "lines": 56
}
```

**Response (text format):**
```
@@@@@###SSSS%%%%????
###SSS%%%???***+++;;
...
```

---

## 🧪 Testing the API

### Test with the included sample image:
```bash
# If you have monaLisa.webp
curl -X POST -F "image=@monaLisa.webp" -F "width=80" -F "format=text" http://localhost:8000/api/convert/
```

### Test with Python client:
```bash
python api_client.py monaLisa.webp 80 text
```

### Test with browser:
Open `http://localhost:8000/api/` and upload any image

---

## ⚠️ Common Issues

### "Connection refused"
**Problem:** Server is not running
**Solution:** Run `python manage.py runserver` first

### "Module not found"
**Problem:** Dependencies not installed
**Solution:** Run `pip install -r requirements.txt`

### "Port already in use"
**Problem:** Port 8000 is already in use
**Solution:** Run on a different port: `python manage.py runserver 8001`

---

## 💡 Tips

1. **Image Size**: The API handles large images, but smaller images convert faster
2. **Width Settings**: 
   - 50-80: Good for small images or terminal display
   - 100-150: Default, works for most images
   - 150-300: For large displays or detailed images
3. **Best Results**: Use images with good contrast and clear subjects
4. **Output**: Text format is best for saving to files, JSON for programmatic use

---

## 📚 More Examples

### JavaScript/Fetch API:
```javascript
const formData = new FormData();
formData.append('image', fileInput.files[0]);
formData.append('width', '120');

fetch('http://localhost:8000/api/convert/', {
    method: 'POST',
    body: formData
})
.then(response => response.json())
.then(data => console.log(data.ascii_art));
```

### With error handling:
```bash
curl -X POST -F "image=@test.jpg" -F "width=150" \
  http://localhost:8000/api/convert/ | python -m json.tool
```

---

## 🎨 Standalone Script (No Server Required)

Don't need the API? Use the standalone script:

```bash
python ascii_image.py myimage.jpg -w 120 -o output.txt
```

---

## 🛑 Stopping the Server

Press `Ctrl+C` in the terminal where the server is running.

---

For more details, see the main [README.md](README.md)


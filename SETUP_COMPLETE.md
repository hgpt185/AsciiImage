# 🎉 ASCII Image Converter - Setup Complete!

## ✅ What's Been Created

### 1. Command-Line Tool
- **File**: `ascii_image.py`
- **Purpose**: Standalone script to convert images to ASCII art
- **Usage**: `python ascii_image.py image.jpg -w 100 -o output.txt`

### 2. Django REST API
- **Project**: `asciiserver/` - Django project configuration
- **App**: `api/` - API application with endpoints
- **Features**:
  - POST `/api/convert/` - Convert images to ASCII
  - GET `/api/info/` - API documentation
  - GET `/api/` - Web interface for testing

### 3. Web Interface
- **File**: `api/templates/index.html`
- **Features**: Beautiful, modern UI with:
  - Drag-and-drop image upload
  - Image preview
  - Width adjustment slider
  - Live ASCII art display
  - Copy to clipboard
  - Modern gradient design

### 4. Python API Client
- **File**: `api_client.py`
- **Purpose**: Example client to interact with the API
- **Usage**: `python api_client.py image.jpg 120 text`

### 5. Documentation
- **README.md** - Comprehensive documentation
- **QUICKSTART.md** - Quick start guide for beginners
- **requirements.txt** - Python dependencies

---

## 🚀 Server Status

✅ **Django server is running on http://localhost:8000**

### Available URLs:
- **Web Interface**: http://localhost:8000/api/
- **API Info**: http://localhost:8000/api/info/
- **Convert Endpoint**: http://localhost:8000/api/convert/ (POST)

---

## 🧪 Tested & Working

✅ Server starts successfully
✅ API endpoints respond correctly
✅ Image conversion works perfectly
✅ Web interface loads properly
✅ curl commands work as expected

Example output from monaLisa.webp:
```
?******?*******??????****????*******?*????????*?????********
?**************?????***************************************?
***++++++++++**************++++++*****++++********+++******?
**++++++++++++++++**+++++++++**++++++++++++**+**+++++++*****
*++;;+++++++++++++++++++*?%S#####S%?*+++++++*+++++++++++****
```

---

## 📦 Project Structure

```
AsciiImage/
├── ascii_image.py          # Standalone CLI tool
├── api_client.py           # Python API client
├── manage.py              # Django management
├── requirements.txt       # Dependencies
├── README.md             # Full documentation
├── QUICKSTART.md         # Quick start guide
├── db.sqlite3            # Database (auto-generated)
│
├── asciiserver/          # Django project
│   ├── settings.py       # Configuration
│   ├── urls.py          # Main URL routing
│   └── ...
│
└── api/                  # API application
    ├── views.py          # API endpoints & web interface
    ├── urls.py          # API URL routing
    ├── ascii_converter.py # Core conversion logic
    └── templates/
        └── index.html    # Web UI

```

---

## 💻 How to Use

### Option 1: Web Interface (Easiest!)
1. Open browser: http://localhost:8000/api/
2. Upload an image
3. Adjust width
4. Click "Convert to ASCII"
5. Copy or save the result

### Option 2: Command Line (curl)
```bash
curl -X POST -F "image=@photo.jpg" -F "width=100" -F "format=text" \
  http://localhost:8000/api/convert/
```

### Option 3: Python Client
```bash
python api_client.py photo.jpg 120 text
```

### Option 4: Standalone Script (No Server)
```bash
python ascii_image.py photo.jpg -w 120 -o ascii_art.txt
```

---

## 🔧 Server Management

### Start Server:
```bash
python manage.py runserver
```

### Stop Server:
Press `Ctrl+C` in the terminal

### Run on Different Port:
```bash
python manage.py runserver 8001
```

---

## 📋 API Parameters

### POST /api/convert/

**Parameters:**
- `image` (file, required) - Image to convert (JPG, PNG, GIF, WebP, etc.)
- `width` (integer, optional) - ASCII width in characters (10-500, default: 100)
- `format` (string, optional) - Response format: 'json' or 'text' (default: 'json')

**Response (JSON):**
```json
{
  "success": true,
  "ascii_art": "@@##SS%%??...",
  "width": 100,
  "lines": 56
}
```

**Response (Text):**
```
@@@@###SSSS%%%%
###SSS%%%???***
...
```

---

## 🎨 Tips for Best Results

1. **Image Quality**: Use images with good contrast
2. **Subject**: Clear subjects work better than busy scenes
3. **Width Settings**:
   - 50-80: Terminal display, small images
   - 100-150: Standard (recommended)
   - 150-300: Large displays, detailed images
4. **File Formats**: All common formats supported (JPG, PNG, GIF, WebP, BMP, etc.)

---

## 🐛 Troubleshooting

### "Connection refused"
→ Start the server: `python manage.py runserver`

### "Module not found"
→ Install dependencies: `pip install -r requirements.txt`

### "Port already in use"
→ Use different port: `python manage.py runserver 8001`

### Web interface CORS issues
→ Access directly at http://localhost:8000/api/ (same origin)

---

## 📚 Dependencies

- **Pillow** (>=10.0.0) - Image processing
- **Django** (>=4.2.0) - Web framework
- **requests** (>=2.31.0) - HTTP library (for client)

Install all: `pip install -r requirements.txt`

---

## 🎯 Next Steps

1. **Try the web interface**: http://localhost:8000/api/
2. **Test with your own images**: Upload any photo
3. **Experiment with width settings**: Find what works best
4. **Use the API**: Integrate into your own applications
5. **Customize**: Modify the ASCII character set in `api/ascii_converter.py`

---

## ⭐ Features

✅ Multiple interfaces (Web, API, CLI)
✅ Beautiful modern web UI
✅ RESTful API with JSON/text responses
✅ Customizable ASCII width
✅ Maintains aspect ratio
✅ Error handling & validation
✅ Copy to clipboard support
✅ Image preview
✅ Comprehensive documentation
✅ Example client code
✅ CSRF exemption for easy API testing

---

## 🔗 Quick Links

- **Web Interface**: http://localhost:8000/api/
- **API Docs**: http://localhost:8000/api/info/
- **Full README**: [README.md](README.md)
- **Quick Start**: [QUICKSTART.md](QUICKSTART.md)

---

**Everything is ready to use! Have fun creating ASCII art! 🎨**


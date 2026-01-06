# Deploy to Render

This guide explains how to deploy your ASCII Image Converter to Render.com for free.

## 📋 Prerequisites

1. A GitHub account
2. A Render account (free) - sign up at https://render.com
3. Your code pushed to a GitHub repository

## 🚀 Deployment Steps

### Step 1: Push to GitHub

If you haven't already, push your code to GitHub:

```bash
cd /Users/hemesh.gupta/Desktop/personal/AsciiImage

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Ready for Render deployment"

# Create a new repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Render

1. **Go to Render Dashboard**
   - Visit https://dashboard.render.com
   - Click "New +" button
   - Select "Web Service"

2. **Connect Your Repository**
   - Connect your GitHub account if not already connected
   - Select your ASCII Image Converter repository
   - Click "Connect"

3. **Configure the Service**
   
   Render will auto-detect the `render.yaml` file and configure everything automatically!
   
   But if you need to configure manually:
   
   - **Name**: `ascii-image-converter` (or any name you prefer)
   - **Runtime**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn asciiserver.wsgi:application`
   - **Plan**: `Free`

4. **Add Environment Variables**
   
   Click "Advanced" and add these environment variables:
   
   - `SECRET_KEY`: (Render will auto-generate this)
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: Your Render URL (e.g., `ascii-image-converter.onrender.com`)
   - `PYTHON_VERSION`: `3.9.16`

5. **Deploy!**
   - Click "Create Web Service"
   - Wait 5-10 minutes for the first build
   - Your app will be live at: `https://YOUR-APP-NAME.onrender.com`

### Step 3: Access Your App

Once deployed, visit:
- **Web Interface**: `https://YOUR-APP-NAME.onrender.com/api/`
- **API Info**: `https://YOUR-APP-NAME.onrender.com/api/info/`
- **Convert Endpoint**: `https://YOUR-APP-NAME.onrender.com/api/convert/`

## 🔧 What the Deployment Files Do

### `render.yaml`
- Defines your service configuration
- Specifies Python runtime and build commands
- Sets up environment variables
- Configures health checks

### `build.sh`
- Installs Python dependencies
- Collects static files for production
- Runs database migrations
- Prepares the app for deployment

### Updated `settings.py`
- Reads environment variables for security
- Enables WhiteNoise for static file serving
- Configures allowed hosts dynamically
- Production-ready settings

### Updated `requirements.txt`
- Added `gunicorn` - production WSGI server
- Added `whitenoise` - static file serving

## 🎯 Testing Your Deployment

### Using curl:
```bash
# Test API info
curl https://YOUR-APP-NAME.onrender.com/api/info/

# Convert an image
curl -X POST -F "image=@photo.jpg" -F "width=100" \
  https://YOUR-APP-NAME.onrender.com/api/convert/
```

### Using Python:
```python
import requests

url = "https://YOUR-APP-NAME.onrender.com/api/convert/"

with open('myimage.jpg', 'rb') as f:
    files = {'image': f}
    data = {'width': 120, 'format': 'json'}
    response = requests.post(url, files=files, data=data)
    
print(response.json()['ascii_art'])
```

## 🆓 Free Tier Limitations

Render's free tier includes:
- ✅ 750 hours/month (enough for one app running 24/7)
- ✅ Automatic HTTPS
- ✅ Continuous deployment from Git
- ⚠️ App spins down after 15 minutes of inactivity
- ⚠️ First request after spin-down takes ~30 seconds

## 🔄 Automatic Deployments

Every time you push to your GitHub repository:
1. Render automatically detects the changes
2. Rebuilds your application
3. Deploys the new version
4. Zero downtime!

## 🐛 Troubleshooting

### Build fails
- Check the build logs in Render dashboard
- Ensure all dependencies are in `requirements.txt`
- Verify `build.sh` has execute permissions

### App won't start
- Check the logs in Render dashboard
- Verify environment variables are set correctly
- Make sure `ALLOWED_HOSTS` includes your Render URL

### Static files not loading
- Ensure `collectstatic` ran in build.sh
- Check WhiteNoise is in MIDDLEWARE
- Verify STATIC_ROOT is set correctly

### 404 errors
- Make sure you're accessing `/api/` not just `/`
- Check your URL configuration in Django

## 📝 Environment Variables to Set

After deployment, add these in Render dashboard:

| Variable | Value | Description |
|----------|-------|-------------|
| `SECRET_KEY` | (auto-generated) | Django secret key |
| `DEBUG` | `False` | Disable debug mode |
| `ALLOWED_HOSTS` | `your-app.onrender.com` | Your Render domain |
| `PYTHON_VERSION` | `3.9.16` | Python version |

## 🎉 Success!

Once deployed, share your ASCII art converter with the world!

Your live URLs:
- Web Interface: `https://your-app.onrender.com/api/`
- API Docs: `https://your-app.onrender.com/api/info/`

## 💡 Pro Tips

1. **Custom Domain**: Add your own domain in Render settings
2. **Monitoring**: Check logs regularly in Render dashboard
3. **Updates**: Just push to GitHub and Render auto-deploys
4. **Keep Alive**: Use a service like UptimeRobot to ping your app and prevent spin-down

---

**Need help?** Check Render's documentation: https://render.com/docs


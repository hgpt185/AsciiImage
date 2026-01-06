# Deploy to Render - Fixed and Working Guide

This guide has been updated with all fixes for successful deployment.

## 🔧 What Was Fixed

1. **Gunicorn binding** - Now binds to `0.0.0.0:$PORT` (Render's dynamic port)
2. **ALLOWED_HOSTS** - Properly configured for Render domain
3. **CSRF trusted origins** - Added for Render domains
4. **Health check** - Points to `/api/info/` which returns JSON
5. **Static files** - WhiteNoise configured correctly

---

## 📋 Prerequisites

1. A GitHub account
2. A Render account (free) - sign up at https://render.com
3. Your code pushed to a GitHub repository

---

## 🚀 Deployment Steps

### Step 1: Push to GitHub

```bash
cd /Users/hemesh.gupta/Desktop/personal/AsciiImage

# Add all files
git add .

# Commit with message
git commit -m "Fixed Render deployment configuration"

# Push to GitHub
git push origin main
```

### Step 2: Deploy on Render

#### Option A: Using render.yaml (Automatic)

1. Go to https://dashboard.render.com
2. Click "New +" → "Blueprint"
3. Connect your GitHub repository
4. Render will detect `render.yaml` automatically
5. Click "Apply" - it will configure everything!

#### Option B: Manual Setup

1. Go to https://dashboard.render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:

**Basic Settings:**
- **Name**: `ascii-image-converter`
- **Runtime**: `Python 3`
- **Branch**: `main`

**Build & Deploy:**
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn asciiserver.wsgi:application --bind 0.0.0.0:$PORT`

**Environment Variables:**
- `PYTHON_VERSION` = `3.9.16`
- `SECRET_KEY` = (click "Generate" to create a secure key)
- `DEBUG` = `False`
- `ALLOWED_HOSTS` = `ascii-image-converter.onrender.com`

**Advanced:**
- **Health Check Path**: `/api/info/`
- **Plan**: Free

5. Click "Create Web Service"

### Step 3: Wait for Deployment

- First build takes 5-10 minutes
- Watch the build logs for any errors
- Once you see "Your service is live 🎉", it's ready!

### Step 4: Test Your Deployment

Visit your app at:
```
https://ascii-image-converter.onrender.com/api/
```

Test the API:
```bash
curl https://ascii-image-converter.onrender.com/api/info/
```

---

## 🎯 Key Configuration Files

### 1. `render.yaml` (Blueprint Configuration)
```yaml
services:
  - type: web
    name: ascii-image-converter
    runtime: python
    plan: free
    buildCommand: "./build.sh"
    startCommand: "gunicorn asciiserver.wsgi:application --bind 0.0.0.0:$PORT"
    envVars:
      - key: PYTHON_VERSION
        value: 3.9.16
      - key: SECRET_KEY
        generateValue: true
      - key: DEBUG
        value: False
      - key: ALLOWED_HOSTS
        value: ascii-image-converter.onrender.com
    healthCheckPath: /api/info/
```

**Key Points:**
- `--bind 0.0.0.0:$PORT` - Critical! Binds to Render's dynamic port
- `healthCheckPath` - Render checks this endpoint to verify app is running
- `ALLOWED_HOSTS` - Must include your Render domain

### 2. `build.sh` (Build Script)
```bash
#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

**What it does:**
1. Updates pip
2. Installs all dependencies
3. Collects static files (CSS, JS)
4. Runs database migrations

### 3. `Procfile` (Alternative Start Command)
```
web: gunicorn asciiserver.wsgi:application --bind 0.0.0.0:$PORT
```

Backup method if render.yaml isn't used.

---

## 🔍 Troubleshooting

### Error: "Timed out after waiting for internal health check"

**Causes:**
1. App not binding to correct port
2. Health check endpoint not responding
3. App crashed during startup

**Solutions:**
✅ **Fixed in this version:**
- Start command now includes `--bind 0.0.0.0:$PORT`
- Health check points to working endpoint `/api/info/`
- ALLOWED_HOSTS properly configured

**Check build logs:**
1. Go to Render dashboard
2. Click your service
3. View "Logs" tab
4. Look for errors

### Error: "DisallowedHost at /"

**Problem:** ALLOWED_HOSTS not configured

**Solution:**
Add environment variable:
```
ALLOWED_HOSTS = your-app-name.onrender.com
```

### Error: "Bad Request (400)"

**Problem:** CSRF issues

**Solution:**
Already fixed in `settings.py`:
```python
CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
]
```

### Error: "Static files not loading"

**Problem:** Static files not collected

**Solution:**
Verify `build.sh` runs:
```bash
python manage.py collectstatic --no-input
```

### App works but health check fails

**Problem:** Wrong health check path

**Solution:**
Change to `/api/info/` (returns JSON, easy for Render to check)

---

## 📊 Monitoring Your Deployment

### Check Logs:
```bash
# In Render dashboard, go to Logs tab
# You'll see:
- Build logs
- Deploy logs  
- Application logs
```

### Test Endpoints:
```bash
# Health check
curl https://your-app.onrender.com/api/info/

# Convert image
curl -X POST -F "image=@photo.jpg" \
  https://your-app.onrender.com/api/convert/
```

---

## 🎨 Using Your Deployed App

### Web Interface:
```
https://your-app.onrender.com/api/
```

### API Calls:
```python
import requests

url = "https://your-app.onrender.com/api/convert/"

with open('image.jpg', 'rb') as f:
    response = requests.post(url, files={'image': f}, data={'width': 120})
    print(response.json()['ascii_art'])
```

---

## 🆓 Free Tier Info

**Render Free Tier:**
- ✅ 750 hours/month
- ✅ Automatic HTTPS
- ✅ Auto-deploy from Git
- ⚠️ Spins down after 15 min inactivity
- ⚠️ 30-50s cold start time

**Keep it alive:**
Use UptimeRobot or similar to ping every 10 minutes.

---

## ✅ Deployment Checklist

Before deploying, ensure:

- [ ] All code pushed to GitHub
- [ ] `render.yaml` has correct domain
- [ ] `build.sh` is executable (`chmod +x build.sh`)
- [ ] `requirements.txt` includes all dependencies
- [ ] Environment variables configured in Render
- [ ] Health check path is `/api/info/`
- [ ] Start command includes `--bind 0.0.0.0:$PORT`

---

## 🔄 Updating Your Deployment

```bash
# Make changes locally
git add .
git commit -m "Update description"
git push origin main

# Render automatically:
# 1. Detects push
# 2. Rebuilds app
# 3. Deploys new version
# (Takes 2-5 minutes)
```

---

## 📝 Common Commands

```bash
# Check if service is running
curl https://your-app.onrender.com/api/info/

# Test image conversion
curl -X POST -F "image=@test.jpg" \
  https://your-app.onrender.com/api/convert/ \
  -o output.txt

# View app in browser
open https://your-app.onrender.com/api/
```

---

## 🎉 Success Indicators

Your deployment is successful when you see:

1. ✅ Build completes without errors
2. ✅ "Your service is live 🎉" message
3. ✅ Health check passes (green checkmark)
4. ✅ Web interface loads in browser
5. ✅ Image conversion works

---

## 💡 Pro Tips

1. **First deployment:** Takes 5-10 minutes, be patient
2. **Cold starts:** First request after inactivity takes 30s
3. **Logs:** Always check logs if something fails
4. **Environment vars:** Change them in Render dashboard, not in code
5. **Custom domain:** Can add your own domain in Render settings

---

## 🆘 Still Having Issues?

1. Check Render status: https://status.render.com
2. View build logs in dashboard
3. Verify all environment variables are set
4. Test health check endpoint manually
5. Ensure GitHub repo is up to date

---

**This configuration has been tested and works!** Just follow the steps and your app will deploy successfully. 🚀

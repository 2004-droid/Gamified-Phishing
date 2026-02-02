# Gamified Phishing Awareness Training

A Flask web application for phishing awareness training and security simulations.

## Deployment Instructions (Render)

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

### Step 2: Deploy on Render
1. Go to [render.com](https://render.com)
2. Click **"New +"** → **"Web Service"**
3. Click **"Connect a repository"** and select your GitHub repo
4. Fill in these settings:
   - **Name:** `gamified-phishing` (or your choice)
   - **Region:** `Ohio` or closest to you
   - **Branch:** `main`
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click **"Create Web Service"**

### Step 3: Your site will be live!
Render will provide you with a URL like: `https://gamified-phishing.onrender.com`

## Files Ready for Deployment
✅ `requirements.txt` - All dependencies  
✅ `Procfile` - Render startup command  
✅ `.gitignore` - Excludes unnecessary files  
✅ `app.py` - Configured for production (host 0.0.0.0, PORT env var)

## Local Testing
```bash
pip install -r requirements.txt
python app.py
```
Visit: `http://localhost:5000`

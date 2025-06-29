# Free Deployment Guide

## Option 1: Railway (Recommended - Easiest)

### Steps:
1. **Sign up for Railway** (free): https://railway.app
2. **Connect your GitHub repo** to Railway
3. **Deploy automatically** - Railway will detect the Dockerfile and deploy

### Commands to run:
```bash
# Push your code to GitHub first
git add .
git commit -m "Ready for deployment"
git push origin main

# Then go to Railway and connect your repo
```

## Option 2: Render (Alternative)

### Steps:
1. **Sign up for Render** (free): https://render.com
2. **Create a new Web Service**
3. **Connect your GitHub repo**
4. **Set build command**: `pip install -r orchestrator/requirements.txt`
5. **Set start command**: `cd orchestrator && uvicorn main:app --host 0.0.0.0 --port $PORT`

## Option 3: Heroku (Alternative)

### Steps:
1. **Sign up for Heroku** (free tier available)
2. **Install Heroku CLI**
3. **Run these commands**:
```bash
heroku create your-app-name
git push heroku main
```

## Option 4: Google Cloud Run (Free Tier)

### Steps:
1. **Sign up for Google Cloud** (free credits)
2. **Enable Cloud Run**
3. **Deploy with gcloud CLI**:
```bash
gcloud run deploy --source .
```

## Your Deployed Link
After deployment, you'll get a URL like:
- Railway: `https://your-app-name.railway.app`
- Render: `https://your-app-name.onrender.com`
- Heroku: `https://your-app-name.herokuapp.com`

## API Endpoints
- **Schedule a job**: `POST /schedule` with JSON: `{"task": "your task here"}`
- **Check status**: `GET /status/{job_id}`
- **Download output**: Link provided in status response 
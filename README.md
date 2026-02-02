# 🎯 Gamified Phishing Awareness Training

An interactive Flask web application that simulates phishing attacks to educate users about cybersecurity threats. Users experience a realistic attack, get caught, then progress through 3 training levels to learn how to identify and prevent phishing.

## 🚀 Features

- **Realistic Phishing Simulation** - Mimics a real RTA (Roads & Transport Authority) portal to catch users
- **Interactive Training Levels:**
  - Level 1: Spot fake vs real URLs
  - Level 2: Identify suspicious email domains
  - Level 3: Recognize social engineering tactics
- **Admin Panel** - Secret dashboard to launch simulations and track metrics
- **Data Analytics** - `analyzer.py` generates campaign reports
- **Gamification** - XP rewards and progression system

## 📁 Project Structure

```
├── app.py                    # Main Flask application
├── analyzer.py               # Campaign analysis & reporting
├── requirements.txt          # Python dependencies
├── Procfile                  # Render deployment config
├── static/
│   └── rta_dubai.png        # RTA logo branding
└── templates/
    ├── index.html           # Phishing target page (RTA login)
    ├── intercept.html       # "Caught!" reveal page
    ├── training.html        # Level 1 training
    ├── training_level2.html # Level 2 training
    └── training_level3.html # Level 3 training
```

## 🔧 Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/2004-droid/Gamified-Phishing.git
   cd Gamified-Phishing
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run locally:**
   ```bash
   python app.py
   ```
   Visit: `http://localhost:5000`

## 📊 Usage

### Public Routes:
- `/` - RTA Portal login (phishing target)
- `/training-dojo` - Level 1 training
- `/training_level2` - Level 2 training
- `/training_level3` - Level 3 training
- `/submit` - Capture credentials (called after login)

### Admin Panel (Secret):
- `/562025` - Admin dashboard to launch simulations

### Analytics:
```bash
python analyzer.py
```
Shows total emails sent, capture rate, and risk percentage.

## 🌐 Live Deployment

### Deploy on Render (Free)

1. Push code to GitHub (already done!)
2. Go to [render.com](https://render.com)
3. Create new **Web Service**
4. Connect your GitHub repo: `2004-droid/Gamified-Phishing`
5. Use these settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
6. Click **Create Web Service**

Your site will be live at: `https://gamified-phishing.onrender.com`

## 📝 Data Files

- `data.csv` - Logs of compromised user credentials
- `emails_sent.csv` - Email simulation campaign records

## ⚙️ Environment Variables

- `PORT` - Server port (default: 5000)

## 🔐 Security Note

This is an educational phishing simulation tool designed for authorized security training only. Use responsibly and with proper consent.

## 👨‍💻 Author

amrna (amrnafea338@gmail.com)

## 📄 License

Open source for educational purposes.

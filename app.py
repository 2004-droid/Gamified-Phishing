from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime
import os
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

app = Flask(__name__)

# ---------------------------------------------------------
# 1. THE "EMAIL BRAIN" (Hidden logic)
# ---------------------------------------------------------
def send_simulation_email(target_email, public_url):
    brevo_api_key = os.environ.get("BREVO_API_KEY")
    sender_email = os.environ.get("SMTP_USER", "amrnafea338@gmail.com")
    
    if not brevo_api_key:
        print("BREVO_API_KEY not set")
        return False

    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = brevo_api_key
    
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    html_body = f"""
    <html>
      <body style="font-family: Arial, sans-serif;">
        <p>Dear Valued Customer,</p>
        <p>Suspicious login detected on your nol card account. Verify your account to avoid suspension:</p>
        <a href="{public_url}" style="background-color: #ee2e24; color: white; padding: 12px; text-decoration: none; border-radius: 5px;">Verify Now</a>
      </body>
    </html>
    """

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": target_email}],
        sender={"email": sender_email, "name": "RTA Security Support"},
        subject="Urgent: nol Card Account Verification Required",
        html_content=html_body
    )

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        print(f"Brevo response: {api_response}")
        return True
    except ApiException as e:
        print(f"Brevo Error: {e}")
        return False

# ---------------------------------------------------------
# 2. THE BACKDOOR (Secret Admin Page)
# ---------------------------------------------------------
@app.route('/562025', methods=['GET', 'POST'])
def admin():
    status = ""
    status_color = "#4CAF50"
    if request.method == 'POST':
        email_to_phish = request.form.get('target_email')
        # Use the public URL from environment variable or fallback to request.host_url
        my_link = os.environ.get('PUBLIC_URL', request.host_url) 
        
        if send_simulation_email(email_to_phish, my_link):
            status = "✓ Success! Phishing email sent."
            status_color = "#4CAF50"
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open('emails_sent.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([email_to_phish, timestamp])
        else:
            status = "✗ Error! Check your App Password."
            status_color = "#ee2e24"
            
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Secret Admin Panel</title>
        <style>
            body {{
                font-family: 'Segoe UI', sans-serif;
                background: #1a1a1a;
                color: white;
                text-align: center;
                padding: 50px;
                margin: 0;
            }}
            .admin-card {{
                background: #2d2d2d;
                padding: 40px;
                border-radius: 15px;
                max-width: 500px;
                margin: 0 auto;
                border-bottom: 5px solid #ee2e24;
                box-shadow: 0 4px 20px rgba(0,0,0,0.5);
            }}
            h2 {{
                color: #ee2e24;
                font-size: 2em;
                margin-bottom: 10px;
            }}
            .subtitle {{
                color: #999;
                margin-bottom: 30px;
                font-size: 0.9em;
            }}
            input[type="email"] {{
                width: 90%;
                padding: 15px;
                margin: 20px 0;
                background: #3d3d3d;
                border: 1px solid #555;
                color: white;
                border-radius: 5px;
                font-size: 1em;
            }}
            input[type="email"]:focus {{
                outline: none;
                border-color: #ee2e24;
            }}
            button {{
                width: 95%;
                padding: 15px;
                background: #ee2e24;
                border: none;
                color: white;
                border-radius: 5px;
                font-size: 1.1em;
                cursor: pointer;
                font-weight: bold;
                transition: background 0.3s;
            }}
            button:hover {{
                background: #d42719;
            }}
            .status {{
                margin-top: 25px;
                padding: 15px;
                border-radius: 5px;
                background: #3d3d3d;
                color: {status_color};
                font-weight: bold;
                font-size: 1.1em;
            }}
            .lock-icon {{
                font-size: 3em;
                margin-bottom: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="admin-card">
            <div class="lock-icon">🔐</div>
            <h2>Phish Launcher</h2>
            <p class="subtitle">Security Awareness Training Control Panel</p>
            <p style="color: #4CAF50; font-size: 1.1em; margin: 20px 0;">Welcome back Mr.Robot, who are we phishing now?</p>
            <form method="post">
                <input type="email" name="target_email" placeholder="Enter target email address" required>
                <button type="submit">🎯 Launch Simulation</button>
            </form>
            {f'<div class="status">{status}</div>' if status else ''}
        </div>
    </body>
    </html>
    '''

# ---------------------------------------------------------
# 3. THE FRONT DOOR (Public RTA Page)
# ---------------------------------------------------------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open('data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([username, "COMPROMISED", timestamp])

    return render_template('intercept.html')

@app.route('/training-dojo')
def training_dojo():
    return render_template('training.html')

@app.route('/training_level2')
def training_level2():
    return render_template('training_level2.html')

@app.route('/training_level3')
def training_level3():
    return render_template('training_level3.html')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
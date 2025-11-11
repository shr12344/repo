#Generate a temporary download link that expires after a set time (e.g., 30 seconds). If a
#user tries to use it later, it wont work.

from flask import Flask, send_file, request, abort
from datetime import datetime, timedelta
import secrets

app = Flask(__name__)
TOKENS = {} 

@app.route("/generate_link")
def generate_link():
    token = secrets.token_urlsafe(16)
    expiry = datetime.now() + timedelta(seconds=60) 
    TOKENS[token] = expiry
    return f"""
        Temporary link created. Use it within 60 seconds:&lt;br&gt;&lt;br&gt;
        &lt;a href="/download?token={token}"&gt;Download Link&lt;/a&gt;
        """

@app.route("/download")
def download():
    token = request.args.get("token")
    if token in TOKENS:

        if datetime.now() < TOKENS[token]:
            return send_file("sample.txt", as_attachment=True)
    else:
        return " Link expired. Please generate a new one."
    abort(403) 

if __name__ == "__main__":
    app.run(debug=True)

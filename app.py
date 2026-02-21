from flask import Flask, request, render_template_string, redirect, url_for, flash
import os
import time

app = Flask(__name__)
app.secret_key = "super_secret_key_change_this"

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>⚜️INSTA SARVAR YAMDHUD⚜️</title>
<style>
body{
    margin:0;
    padding:0;
    font-family:Arial;
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    background:url("https://i.postimg.cc/bvmpS7tS/IMG-20260222-WA0030.jpg") no-repeat center center;
    background-size:cover;
}
.box{
    background:rgba(255,255,255,0.85);
    padding:25px;
    border-radius:12px;
    width:95%;
    max-width:400px;
    box-shadow:0 10px 30px rgba(0,0,0,0.4);
}
input,button{
    width:100%;
    padding:10px;
    margin-bottom:12px;
    border-radius:6px;
    border:1px solid #ccc;
}
button{
    background:#007bff;
    color:white;
    border:none;
    cursor:pointer;
}
button:hover{
    background:#0056b3;
}
.message{
    text-align:center;
    font-size:14px;
}
.success{color:green;}
.error{color:red;}
</style>
</head>
<body>
<div class="box">
<h2 style="text-align:center;">Message Processor</h2>

{% with messages = get_flashed_messages(with_categories=true) %}
  {% for category, message in messages %}
    <div class="message {{category}}">{{message}}</div>
  {% endfor %}
{% endwith %}

<form method="POST" enctype="multipart/form-data">
<input type="text" name="group_id" placeholder="Enter Group ID" required>
<input type="number" name="delay" placeholder="Delay in seconds" required>
<input type="file" name="message_file" required>
<button type="submit">Process File</button>
</form>
</div>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            group_id = request.form["group_id"]
            delay = int(request.form["delay"])
            file = request.files["message_file"]

            if not file:
                flash("No file uploaded", "error")
                return redirect(url_for("home"))

            lines = file.read().decode("utf-8").splitlines()

            if not lines:
                flash("File is empty", "error")
                return redirect(url_for("home"))

            # SAFE DEMO LOGIC (no automation)
            for line in lines:
                print(f"[Group {group_id}] {line}")
                time.sleep(delay)

            flash("File processed successfully!", "success")

        except Exception as e:
            flash(f"Error: {e}", "error")

        return redirect(url_for("home"))

    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()

    return f"""
    <html>
        <head>
            <title>NLB Auto Scaling Project</title>
        </head>
        <body>
            <h1>Scalable Web Application</h1>
            <h2>Application is Running!</h2>
            <p>Server Hostname: {hostname}</p>
            <p>This application is running behind an AWS Network Load Balancer.</p>
        </body>
    </html>
    """

app.run(host="0.0.0.0", port=80)
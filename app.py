from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def display_headers():
    headers = request.headers
    
    # Create HTML response
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>HTTP Headers Display</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                max-width: 800px; 
                margin: 0 auto; 
                padding: 20px; 
            }
            h1 { 
                color: #f6821f; 
            }
            .header-container { 
                background-color: #f5f5f5; 
                padding: 15px; 
                border-radius: 5px; 
                margin-top: 20px;
            }
            .header-item { 
                margin-bottom: 8px; 
                border-bottom: 1px solid #ddd; 
                padding-bottom: 8px; 
            }
            .key { 
                font-weight: bold; 
                color: #2c7cb0; 
            }
        </style>
    </head>
    <body>
        <h1>HTTP Headers Display</h1>
        <p>This page displays all HTTP request headers received by the server:</p>
        <div class="header-container">
    """
    
    for key, value in headers.items():
        html += f'<div class="header-item"><span class="key">{key}:</span> {value}</div>'
    
    html += """
        </div>
        <p><em>This site was created for the Cloudflare Associate Solutions Engineer Technical Project.</em></p>
    </body>
    </html>
    """
    
    return html

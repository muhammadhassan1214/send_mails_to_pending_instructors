
def generate_email(instructor_name: str) -> str:
    html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    color: #333333;
                    line-height: 1.6;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    max-width: 600px;
                    margin: 20px auto;
                    padding: 20px;
                }}
                .important-notice {{
                    color: #d9534f; /* A subtle red to draw attention */
                    font-weight: bold;
                }}
                .signature {{
                    margin-top: 30px;
                    font-size: 0.95em;
                }}
                a {{
                    color: #0056b3;
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <p>Dear {instructor_name},</p>

                <p>Please take a moment to log in to <a href="https://atlas.heart.org" target="_blank">atlas.heart.org</a> and confirm your pending Alignment Request, which is currently listed under <strong>"Tasks to Complete."</strong></p>

                <p>Our records show that your alignment is not yet fully completed. This confirmation is required in order to activate you under our Training Center / Training Site within the American Heart Association system.</p>
                
                <span class="important-notice">Important: If this alignment request is not confirmed within 10 business days, your alignment with our company will be withdrawn.</span>

                <p>Please complete this as soon as possible to avoid any interruption in your instructor status.</p>

                <p>If you experience any issues locating or confirming the request, please reach out to us right away and we will assist you.</p>

                <p>Thank you for your prompt attention to this matter.</p>

                <div class="signature">
                    <p>Many Blessings,<br><br>
                    <strong>Nathaniel Shell, NREMT</strong><br>
                    Training Center Coordinator<br>
                    Code Blue CPR Services, LLC<br>
                    Office: <a href="tel:6895007044">689-500-7044</a><br>
                    Email: <a href="mailto:training@codebluecprservices.com">training@codebluecprservices.com</a><br>
                    <a href="https://atlas.heart.org" target="_blank">atlas.heart.org</a></p>
                </div>
            </div>
        </body>
        </html>
        """

    return html_content

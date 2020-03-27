"""
    Title: Flask Login/Signup with Email-Verification
    Module Name: mailer
    Author: Daljeet Singh Chhabra
    Language: Python
    Date Created: 27-03-2020
    Date Modified: 27-03-2020
    Description:
        ###############################################################
        ##  Controls the mailing functionality of server.
        ###############################################################
"""
from mailjet_rest import Client
from proj_constants import MAILJET_API_KEY, MAILJET_API_SECRET, MAILJET_SENDER_NAME, MAILJET_SENDER_EMAIL

mailjet = Client(auth=(MAILJET_API_KEY, MAILJET_API_SECRET), version='v3.1')


def send_email_verification_mail(email, name, link):
    data = {
        'Messages': [
            {
                "From": {
                    "Email": MAILJET_SENDER_EMAIL,
                    "Name": MAILJET_SENDER_NAME
                },
                "To": [
                    {
                        "Email": email,
                        "Name": name
                    }
                ],
                "Subject": f"Email Verification for <<INSERT-YOUR-APP_NAME-HERE>>.",
                "TextPart": "Verification",
                "HTMLPart": f'Dear {name}, we received a new sign-up request from this email address. <br> Please '
                            f'verify your account by clicking on the link. '
                            f'<br> Link: {link}<br> Thanks.',
                "CustomID": "emlverification"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    # print(result.json())

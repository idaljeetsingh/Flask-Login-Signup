# Flask Login/Signup with Email-Verification.

Base project repository with basic functionality of Login, Signup, Email Verification, Database Connectivity.
This can be also be used as a headstart for starting your project.
 
# Libraries
    * Flask
    * Mailjet_Rest
    * PyMongo

# Database

This repository uses MongoDB for the backend. If you want to use some other database, modify the following modules accordingly:
    
    * backend.py
    * proj_constants.py

# Setup

1. Create account on [Mailjet](https://app.mailjet.com/signup?lang=en_US) and obtain your API Key and API secret.
2. Create a new MongoDB "Database & User" if you haven't already.
3. Clone this repository and cd into the cloned directory.
4. Modify the `proj_constants.py` file and update the constants there. 
5. Open a new Command Prompt or Terminal & run the command `pip install -r requirements.txt` to install the python dependencies.
5. Run `python server.py` to start the server.



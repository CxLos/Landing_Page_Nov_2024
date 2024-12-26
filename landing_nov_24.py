# =================================== IMPORTS ================================= #

import os
import dash
from dash import html
# 'data/~$bmhc_data_2024_cleaned.xlsx'
# print('System Version:', sys.version)
# =================================== DATA ==================================== #

current_dir = os.getcwd()
current_file = os.path.basename(__file__)
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = 'data/Navigation.xlsx'
data_path1 = 'data/fh_q1_2025_cleaned.xlsx'
file_path = os.path.join(script_dir, data_path)
file_path1 = os.path.join(script_dir, data_path1)

# ============================== Dash Application ========================== #

app = dash.Dash(__name__)
server= app.server

app.layout = html.Div(children=[ 

    html.Div(className='divv', children=[ 
        
        html.H1('November 2024 Impact Reports', 
        className='title'),

        html.Div(
            className='btn-box', 
            children=[
                html.A(
                'MarCom',
                href='https://mc-nov-2024.onrender.com',
                className='btn'),
                html.A(
                'Client Navigation',
                href='https://nav-nov-24.onrender.com/',
                className='btn'),
                html.A(
                'Partner Engagement',
                href='https://partner-engagement-report-nov-24.onrender.com',
                className='btn'),
                html.A(
                'IT',
                href='https://it-report-nov-24.onrender.com',
                className='btn')
            ])
    ])    
])    

if __name__ == '__main__':
    app.run_server(debug=
                #    True)
                   False)

print(f"Serving Flask app '{current_file}'! 🚀")

# --------------------------------- KILL PORT -----------------------------------

# netstat -ano | findstr :8050
# taskkill /PID 24772 /F
# npx kill-port 8050

# ------------------------------ Host Application ----------------------------------

# 1. pip freeze > requirements.txt
# 2. add this to procfile: 'web: gunicorn my_app_name:server'
# 3. heroku login
# 4. heroku create
# 5. git push heroku main

# Create venv 
# virtualenv venv 
# source venv/bin/activate # uses the virtualenv

# Update PIP Setup Tools:
# pip install --upgrade pip setuptools

# Install all dependencies in the requirements file:
# pip install -r requirements.txt

# Check dependency tree:
# pipdeptree
# pip show package-name

# Remove
# pypiwin32
# pywin32
# jupytercore

# ----------------------------------------------------

# Name must start with a letter, end with a letter or digit and can only contain lowercase letters, digits, and dashes.

# Heroku Setup:
# heroku login
# heroku create landing-nov-2024
# heroku git:remote -a landing-nov-2024
# git push heroku main

# Clear Heroku Cache:
# heroku plugins:install heroku-repo
# heroku repo:purge_cache -a nav-nov-2024

# Set buildpack for heroku
# heroku buildpacks:set heroku/python
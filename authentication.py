import os
import numpy as np
import pandas as pd
import dotenv
import tekore as tk

# Load ID and Secret
dotenv.load_dotenv()
client_id = os.getenv('ClientID')
client_secret=os.getenv('ClientSecret')
redirect_uri='http://localhost:8888/callback'

#generate app token
app_token = tk.request_client_token(client_id, client_secret)

#connect to api
spotify = tk.Spotify(app_token,chunked_on=True,max_limits_on=False)

#generate a user token to access user data
user_token = tk.prompt_for_user_token(
    client_id,
    client_secret,
    redirect_uri,
    scope=tk.scope.every
)

spotify.token = user_token
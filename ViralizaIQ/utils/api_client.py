import requests
import pandas as pd
from app.config import config

class InstagramAPI:
    def __init__(self, access_token=None):
        self.access_token = access_token or config.ACCESS_TOKEN

    def get_user_profile(self):
        url = f"https://graph.instagram.com/me"
        params = {
            "fields": "id,username,media_count,followers_count",
            "access_token": self.access_token
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()  # Returns user profile data
        else:
            print("Error fetching user profile:", response.status_code, response.json())
            return None

    def get_user_media(self):
        url = f"https://graph.instagram.com/me/media"
        params = {
            "fields": "id,caption,media_type,media_url,thumbnail_url,timestamp",
            "access_token": self.access_token
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json().get("data", [])
            return pd.DataFrame(data)  # Returns data as a DataFrame
        else:
            print("Error fetching user media:", response.status_code, response.json())
            return None

def save_raw_data(df, file_path):
    """Saves raw Instagram data to CSV in the data/raw directory."""
    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")

def fetch_and_save_data(access_token):
    """Fetches Instagram user media data and saves to CSV."""
    instagram_api = InstagramAPI(access_token=access_token)
    df = instagram_api.get_user_media()
    if df is not None:
        save_raw_data(df, "data/raw/instagram_data.csv")
        print("Data fetching and saving completed successfully.")
    else:
        print("No data fetched from Instagram.")

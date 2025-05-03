import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

# Path to OneDrive folder
onedrive_base = r'C:\Users\sunil\OneDrive - ipu.ac.in\Daily Data'

# Load the list of artist names and their IDs from your CSV file
artist_names_file = os.path.join(onedrive_base, 'Artists_Data.csv')
artist_names_df = pd.read_csv(artist_names_file, encoding='latin1')

# Get artist names and IDs
artist_names_to_keep = artist_names_df.iloc[:, 0].tolist()
artist_ids = artist_names_df.iloc[:, 1].tolist()
artist_id_map = dict(zip(artist_names_to_keep, artist_ids))

# Fetch Spotify listener data
url = 'https://kworb.net/spotify/listeners.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table')

# Initialize storage
artists = []
artist_ids_output = []
listeners = []
daily_change = []

# Today's date
current_date = datetime.now().strftime('%Y-%m-%d')

# Parse table
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    if len(cols) > 1:
        artist_name = cols[1].text.strip()
        monthly_listeners = int(cols[2].text.strip().replace(',', ''))
        daily_change_value = cols[3].text.strip()

        if artist_name in artist_names_to_keep:
            artists.append(artist_name)
            artist_ids_output.append(artist_id_map.get(artist_name, None))
            listeners.append(monthly_listeners)
            daily_change.append(daily_change_value)

# Create new DataFrame
df_new = pd.DataFrame({
    'Artist': artists,
    'Artist ID': artist_ids_output,
    'Monthly Listeners': listeners,
    'Date': current_date,
    'Daily Listeners': daily_change
})

# File path for saving data
daily_output_file = os.path.join(onedrive_base, 'Daily_Listeners.csv')

# Append to the file, or create it if it doesn't exist
if not os.path.exists(daily_output_file):
    df_new.to_csv(daily_output_file, index=False)  # Write header if the file doesn't exist
else:
    df_new.to_csv(daily_output_file, mode='a', header=False, index=False)  # Append without header

print(f"Daily data saved to '{daily_output_file}'")

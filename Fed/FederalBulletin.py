import os
import requests
from google.colab import files

# Base URL for the PDFs
base_url = "https://fraser.stlouisfed.org/files/docs/publications/FRB/1910s"

# Directory to save the downloaded files in Colab
save_directory = "/content/veridelisi"

# Create the directory if it doesn't exist
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Function to download a file from a URL
def download_file(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {url} to {save_path}")
    else:
        print(f"Failed to download {url}. Status code: {response.status_code}")

# Loop through years and months to generate URLs
for year in range(1915, 1920):  # From 1915 to 1919
    for month in range(1, 13):   # From January (1) to December (12)
        # Format the month and year into the filename
        month_str = f"{month:02d}"  # Ensure two digits (e.g., 01 for January)
        url = f"{base_url}/frb_{month_str}{year}.pdf"
        
        # Extract the file name from the URL
        file_name = url.split('/')[-1]
        save_path = os.path.join(save_directory, file_name)
        
        # Download the file
        download_file(url, save_path)

print("All files have been downloaded to Colab.")

# Compress the downloaded files into a ZIP archive
zip_path = "/content/veridelisi.zip"
os.system(f"zip -r {zip_path} {save_directory}")

# Download the ZIP file to your local machine
files.download(zip_path)

print("ZIP file has been downloaded to your local machine.")

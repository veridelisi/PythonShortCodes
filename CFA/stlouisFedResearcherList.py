import requests
from bs4 import BeautifulSoup

def get_all_links(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Parse the content of the request with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all <a> tags, which define hyperlinks
    links = soup.find_all('a', href=True)
    # Extract the href attribute (the URL) from each link
    hrefs = [link['href'] for link in links]
    return hrefs

# The URL we're scraping
url = 'https://research.stlouisfed.org/econ/'

# Fetch all links
all_links = get_all_links(url)

# Print all the clickable links
for link in all_links:
    print(link)
...........................................................................
TAKE THE NAMES

import requests
from bs4 import BeautifulSoup
import re

# Base URL of the economists section
base_url = 'https://research.stlouisfed.org/econ/'

# List to store all economist names
economist_names = [
     'garriga', 'bick', 'kalyani', 'majerovitz', 'marto',
    'ozkan', 'rose', 'wright', 'anderson', 'andolfatto',
    'babus', 'bandyopadhyay', 'berentsen', 'bick',
    'birinci', 'buera', 'chiang', 'chien', 'coughlin',
    'dellas', 'dicecio', 'dupor', 'dvorkin', 'faria-e-castro',
    'gascon', 'gavin', 'gayle', 'gilbert', 'golan', 'gregory',
    'hedlund', 'jefferson', 'kahn', 'kalyani', 'kliesen',
    'kozlowski', 'leibovici', 'leukhina', 'levine', 'majerovitz',
    'manuelli', 'martin', 'marto', 'mccracken', 'monge-naranjo',
    'cneely', 'owyang', 'ozkan', 'ravikumar', 'restrepo-echavarria',
    'rose', 'rubinton', 'sanchez', 'santacreu', 'shin', 'thornton',
    'vandenbroucke', 'waller', 'wang', 'wheelock', 'wright', 'zimmermann'
]

# The email address to exclude
exclude_email = 'mediainquiries@stls.frb.org'

# Function to scrape emails from a given URL
def scrape_emails(profile_url):
    response = requests.get(profile_url)
    if response.ok:
        # Look for email addresses on the page
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', response.text)
        # Exclude the unwanted email address
        return [email for email in emails if email.lower() != exclude_email.lower()]
    else:
        print(f'Failed to retrieve {profile_url}')
        return []

# Set to hold all unique emails
unique_emails = set()

# Go through all economist profile URLs and scrape emails
for name in economist_names:
    profile_url = f'{base_url}{name}'
    emails = scrape_emails(profile_url)
    unique_emails.update(emails)

# Print the unique email addresses
for email in unique_emails:
    print(email)

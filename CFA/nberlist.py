from bs4 import BeautifulSoup

# Sample HTML content
html_content = """
<div class="promo-grid__promos">  

"""

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all div elements with class 'digest-card__title'
title_divs = soup.find_all('div', class_='digest-card__title')

# Extract href attributes from the 'a' tags
href_list = [div.a['href'] for div in title_divs]

# Print the list of href attributes
print(href_list)
............................................................to 57

import requests
from bs4 import BeautifulSoup

def get_emails_from_subroutes(base_url, subroutes):
    email_addresses = {}
    
    for subroute in subroutes:
        # Construct the full URL to the person's profile
        profile_url = f"{base_url}{subroute}"
        
        # Send a GET request to the profile URL
        response = requests.get(profile_url)
        
        # If the request was successful, parse the HTML
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all <a> tags and filter for those with 'mailto:' in the href
            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                if href.startswith('mailto:'):
                    email = href.split('mailto:')[-1]
                    # Store the email against the profile subroute
                    email_addresses[subroute] = email
                    break  # Assume there is only one email per profile
                    
        else:
            print(f"Failed to load page: {profile_url}")
            
    return email_addresses

# Base URL
base_url = 'https://www.nber.org'

# List of subroutes (truncated for example)
subroutes = []

# Get emails from subroutes
emails = get_emails_from_subroutes(base_url, subroutes)

# Print the email addresses
for subroute, email in emails.items():
    print(f" {email},")

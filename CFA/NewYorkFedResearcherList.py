import requests
from bs4 import BeautifulSoup
import re

def find_emails_in_page(url):
    """
    Fetches and parses a webpage at the given URL, then extracts and returns
    email addresses found on the page.
    """
    try:
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()
            emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
            return set(emails)
        else:
            print(f"Unable to load page: {url}")
            return set()
    except Exception as e:
        print(f"Error: {e}")
        return set()

def find_profile_links(base_url):
    """
    Scrapes the given base URL for profile links and returns a set of these links.
    """
    try:
        response = requests.get(base_url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            profile_links = set()
            for link in soup.find_all('a', href=True):
                href = link.get('href')
                if href and href.startswith('/research/economists/'):
                    full_link = f"https://www.newyorkfed.org{href}"
                    profile_links.add(full_link)
            return profile_links
        else:
            print(f"Unable to load page: {base_url}")
            return set()
    except Exception as e:
        print(f"Error: {e}")
        return set()

def extract_emails_from_profiles(base_url):
    """
    Extracts email addresses from the profiles listed on the webpage of the given base URL.
    """
    profile_links = find_profile_links(base_url)
    emails = set()
    for link in profile_links:
        emails.update(find_emails_in_page(link))
    return emails

# Base URL of the site to scrape
base_url = 'https://www.newyorkfed.org/research/economists'
all_emails = extract_emails_from_profiles(base_url)

# Convert the set of emails into a sorted list
email_list = list(all_emails)
email_list.sort()

# Join the emails into a single string with each email on a new line
email_string = '\n'.join(email_list)

# Print the result
print(email_string)

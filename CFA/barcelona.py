import requests
from bs4 import BeautifulSoup

def get_researcher_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Adjust the selector to match the URL pattern of the researcher profiles
    links = soup.find_all('a', href=True)
    researcher_links = [link['href'] for link in links if link['href'].startswith('/people/')]
    return researcher_links

def extract_emails(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    mailto_links = soup.find_all('a', href=lambda href: href and 'mailto:' in href)
    emails = [link['href'].split(':')[1] for link in mailto_links]
    return emails

base_url = "https://bse.eu/researchers?page=2"
researcher_links = get_researcher_links(base_url)
all_emails = []
for link in researcher_links:
    # Prepend the domain to make the URL absolute if necessary
    full_url = f"https://bse.eu{link}" if not link.startswith('http') else link
    email_list = extract_emails(full_url)
    all_emails.extend(email_list)

# Output all collected emails
print(all_emails)

# Remove empty strings, strings with only spaces, and duplicates before printing
cleaned_emails = list(set(email for email in all_emails if email.strip()))

# Output all collected emails as a comma-separated string without single quotes
print(", ".join(cleaned_emails))

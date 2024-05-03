import requests
from bs4 import BeautifulSoup

def get_researcher_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all links that lead to researcher profiles
        links = soup.find_all('a', href=True)
        researcher_links = [link['href'] for link in links if '/Research/Researcher-CV/Author/' in link['href']]
        return researcher_links
    except requests.RequestException as e:
        print(f"Error fetching researcher links: {e}")
        return []

def extract_emails(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        mailto_links = soup.find_all('a', href=lambda href: href and 'mailto:' in href)
        emails = [link['href'].split(':')[1] for link in mailto_links]
        return emails
    except requests.RequestException as e:
        print(f"Error fetching emails from {url}: {e}")
        return []

def main(base_url):
    researcher_links = get_researcher_links(base_url)
    all_emails = []
    for link in researcher_links:
        # Ensure the URL is absolute
        full_url = f"https://www.imf.org{link}" if not link.startswith('http') else link
        email_list = extract_emails(full_url)
        all_emails.extend(email_list)

    # Remove empty strings and duplicates before printing
    cleaned_emails = set(email.strip() for email in all_emails if email.strip())
    # Output all collected emails as a comma-separated string
    print(", ".join(cleaned_emails))

if __name__ == "__main__":
    main("https://www.imf.org/en/Research/Researcher-CV#Name")

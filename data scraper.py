import requests
from bs4 import BeautifulSoup
import csv

# Objective 1: Use the requests library to retrieve web page content
def get_webpage_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching the webpage: {e}")
        return None

# Objective 2: Parse the HTML using BeautifulSoup
def parse_html(content):
    soup = BeautifulSoup(content, 'html.parser')
    return soup

# Objective 3: Extract specific data (e.g., article titles and links)
def extract_data(soup):
    data_list = []
    
    # Example: Scrape BBC News headlines
    articles = soup.find_all('a', class_='gs-c-promo-heading')
    
    for article in articles:
        title = article.get_text(strip=True)
        link = article.get('href')
        if link and not link.startswith('http'):
            link = 'https://www.bbc.com' + link  # Convert relative links to absolute
        data_list.append({'Title': title, 'Link': link})
    
    return data_list

# Objective 4: Save the scraped data into a CSV file
def save_to_csv(data_list, filename="scraped_data.csv"):
    if not data_list:
        print("⚠️ No data found to save.")
        return

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Link"])
        writer.writeheader()
        for item in data_list:
            writer.writerow(item)
    print(f"✅ Data successfully saved to {filename}")

# Main function
def main():
    print("🌐 Welcome to the Data Scraper!")
    url = input("🔗 Enter a website URL to scrape (e.g., https://www.bbc.com/news): ").strip()

    html_content = get_webpage_content(url)
    if html_content is None:
        return

    soup = parse_html(html_content)
    data_list = extract_data(soup)
    
    if data_list:
        print(f"📰 Found {len(data_list)} items. Saving to CSV...")
        save_to_csv(data_list)
    else:
        print("⚠️ No matching articles found. Try another website or selector.")

if __name__ == "__main__":
    main()

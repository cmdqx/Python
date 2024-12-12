import requests
from bs4 import BeautifulSoup

def find_external_links():
    url = "https://www.py4e.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = set()
    for tag in soup.find_all('a', href=True):
        href = tag['href']
        if href.startswith('http'):  # External links only
            links.add(href)

    print(f"Task 1: Found {len(links)} unique external links.")
    return links

def count_comments():
    url = "https://py4e-data.dr-chuck.net/comments_42.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    comments = [int(tag.text) for tag in soup.find_all('span', class_='comments')]
    total_comments = sum(comments)

    print(f"Task 2: Total comments = {total_comments}")
    return total_comments

def find_cities():
    url = "https://stackoverflow.com/jobs/companies"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    cities = set()
    for tag in soup.find_all('span', class_='fc-black-500'):  # Adjust class if necessary
        city = tag.text.strip()
        if city:
            cities.add(city)

    sorted_cities = sorted(cities)
    print(f"Task 3: Found {len(sorted_cities)} unique cities:")
    print(sorted_cities)
    return sorted_cities

def search_stackoverflow(word, pages=5):
    base_url = "https://stackoverflow.com/questions"
    results = []

    for page in range(1, pages + 1):
        response = requests.get(base_url, params={"tab": "newest", "page": page})
        soup = BeautifulSoup(response.text, 'html.parser')

        for question in soup.find_all('div', class_='question-summary'):
            title_tag = question.find('a', class_='question-hyperlink')
            if title_tag and word.lower() in title_tag.text.lower():
                title = title_tag.text.strip()
                link = "https://stackoverflow.com" + title_tag['href']
                results.append((title, link))

    print(f"Task 4: Found {len(results)} questions containing the word '{word}':")
    for title, link in results:
        print(f"- {title}: {link}")
    return results

if __name__ == "__main__":
    print("Starting data scraping tasks...")

    external_links = find_external_links()

    total_comments = count_comments()

    unique_cities = find_cities()

    search_word = input("Enter a word to search on StackOverflow: ")
    stackoverflow_results = search_stackoverflow(search_word, pages=5)
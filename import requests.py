import requests
from bs4 import BeautifulSoup

def find_external_links():
    url = "https://www.py4e.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = set()
    for tag in soup.find_all('a', href=True):
        href = tag['href']
        if href.startswith('http'): 
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
    for tag in soup.find_all('span', class_='fc-black-500'): 
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
        print(f"Fetching page {page}...")
        response = requests.get(f"{base_url}?tab=newest&page={page}")
        
        if response.status_code != 200:
            print(f"Failed to fetch page {page}: HTTP {response.status_code}")
            continue
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ищем вопросы по их заголовкам
        questions = soup.find_all('a', class_='s-link')  # Обновлённый класс для заголовков
        print(f"Found {len(questions)} questions on page {page}.")
        
        for question in questions:
            title = question.text.strip()
            link = "https://stackoverflow.com" + question['href']
            if word.lower() in title.lower():
                results.append((title, link))

    print(f"Task 4: Found {len(results)} questions containing the word '{word}':")
    for title, link in results:
        print(f"- {title}: {link}")
    return results

if __name__ == "__main__":
    print("Starting data scraping tasks...\n")

    external_links = find_external_links()
    print("\n")

    total_comments = count_comments()
    print("\n")

    unique_cities = find_cities()
    print("\n")

    search_word = input("Enter a word to search on StackOverflow: ")
    stackoverflow_results = search_stackoverflow(search_word, pages=5)
    print("\n")
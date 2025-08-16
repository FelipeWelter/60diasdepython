from bs4 import BeautifulSoup
import requests

url = "https://pt.wikipedia.org/wiki/Star_Wars"

response = requests.get(url)

if response.status_code == 200:
    print("Conexão bem-sucedida!")

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string
    print(title)

    paragraphs = soup.find("p").text

    print(paragraphs)

    todos_paragraphs = soup.find_all("p")
    
    if len(todos_paragraphs) > 1:
        print(todos_paragraphs[1].text)

    links = soup.find_all("a", href=True)[:5]
    for link in links:
        print(link['href'])

    print(links)
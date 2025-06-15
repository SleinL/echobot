import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        headers = requests.utils.default_headers()
        headers.update(
            {
                'User-Agent': 'My User Agent 1.0',
            }
        )
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Вызывает ошибку - {e}")


def parse_html(html_content):
    if html_content:
        try:
            return BeautifulSoup(html_content, 'html.parser')
        except Exception as e:
            print(f"ошибка - {e}")



if __name__ == "__main__":
    Url = "https://www.gismeteo.ru/weather-omsk-4578/now/"
    html = get_html(Url)
    soup = parse_html(html)
    soup = soup.find("temperature-value")
    print(soup['value'])
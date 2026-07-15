import requests

dataset = 'open-cross-ref';
book = 'GEN';
chapter = 1;
chapter_endpoint = f"https://bible.helloao.org/api/c/open-cross-ref/GEN/1.json"

response = requests.get(chapter_endpoint)

if response.status_code == 200:
    print(response.json())  
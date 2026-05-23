from pathlib import Path

import requests
from bs4 import BeautifulSoup

from ptt_utils import (
    extract_article,
    gen_article_file_name,
    HEADERS,
)

export_path = Path("./ptt_joke/")
export_path.mkdir(exist_ok=True)

url = "https://www.ptt.cc/bbs/joke/index.html"

for _ in range(5):
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text)

    for a_tag in soup.select('div[class="title"] a'):
        title = a_tag.text
        article_url = "https://www.ptt.cc" + a_tag["href"]

        # Extract article content
        article_content = extract_article(article_url)

        export_txt_file_path = export_path / gen_article_file_name(title)

        with export_txt_file_path.open("w", encoding="utf-8") as f:
            f.write(article_content)

        print(title)
        print(article_url)
        print(export_txt_file_path)
        print("=====")

    url = "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]["href"]
    print(url)

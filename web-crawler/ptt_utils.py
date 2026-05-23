import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
}

COOKIES = {
    "over18": "1",
}

def extract_article(article_url: str) -> str:
    """Input article URL, return article content string."""
    article_res = requests.get(
        article_url,
        headers=HEADERS,
        cookies=COOKIES,
    )
    article_soup = BeautifulSoup(article_res.text, "html.parser")
    article_content_tag = article_soup.select_one('div[id="main-content"]')

    for extract_target_tag in ["div", "span"]:
        for extract_tag in article_content_tag.select(extract_target_tag):
            extract_tag.extract()

    return article_content_tag.text

def gen_article_file_name(title: str) -> str:
    """Input article title, deal with illegal characters."""
    article_file_name = f"{title}.txt"

    ill_chr_list = ["*", '"', "/", "\\", "<", ">", ":", "|", "?"]
    for ill_chr in ill_chr_list:
        article_file_name = article_file_name.replace(ill_chr, "_")

    return article_file_name
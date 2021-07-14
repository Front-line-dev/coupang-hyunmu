import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
NUMBER_OF_REVIEWERS = 10
NUMBER_OF_HISTORIES = 10

def generate_review_list_url(product_id):
    return f'https://www.coupang.com/vp/product/reviews?productId={product_id}&page=1&size={NUMBER_OF_REVIEWERS}&sortBy=ORDER_SCORE_ASC&ratings=&q=&viRoleCode=2&ratingSummary=true'

def generate_history_url(reviewer_id):
    return f'https://www.coupang.com/vp/product/reviews/profile/{reviewer_id}/reviews?page=0&size={NUMBER_OF_HISTORIES}'

def get_reviewers(product_url):
    product_id = urlparse(product_url).path.split('/')[-1]
    product_html = requests.get(generate_review_list_url(product_id), headers=HEADERS).text
    soup = BeautifulSoup(product_html, 'html.parser')
    reviewer_id_list = [elem['data-member-id'] for elem in soup.find_all() if 'data-member-id' in elem.attrs]
    return set(reviewer_id_list)

def get_review_history(reviewer_id):
    history_html = requests.get(generate_history_url(reviewer_id), headers=HEADERS).text
    soup = BeautifulSoup(history_html, 'html.parser')
    history_list = [elem.text for elem in soup.find_all('div', 'sdp-review__profile__article__list__reviews__product__name')]
    return history_list
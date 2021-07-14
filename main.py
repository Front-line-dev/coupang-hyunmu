from library.review import get_reviewers, get_review_history
from library.group import compare_histories

if __name__ == '__main__':
    product_url = input('상품 url을 입력해주세요')
    # product_url = 'https://www.coupang.com/vp/products/5844178878?itemId=10150907528&vendorItemId=71097207459&q=couyor+%EB%AF%B8%EB%8B%88+%EB%B3%B4%EC%A1%B0%EB%B0%B0%ED%84%B0%EB%A6%AC+20000mah&itemsCount=36&searchId=1edaaf467629475aa5f70a6caa5452e3&rank=7&isAddedCart='
    reviewers = get_reviewers(product_url)
    history_list = [get_review_history(reviewer) for reviewer in reviewers]
    similarity = compare_histories(history_list)
    print('유사도', similarity)
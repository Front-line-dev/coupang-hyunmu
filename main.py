from library.review import get_reviewers, get_review_history
from library.group import compare_histories

if __name__ == '__main__':
    product_url = input('상품 url을 입력해주세요')
    reviewers = get_reviewers(product_url)
    history_list = [get_review_history(reviewer) for reviewer in reviewers]
    similarity = compare_histories(history_list)
    print('유사도', similarity)
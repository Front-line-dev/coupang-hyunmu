if __name__ == '__main__':
    product_url = input('상품 url을 입력해주세요')
    reviewers = get_reviewers(product_url)
    review_groups = [get_review_group(reviewer) for reviewer in reviewers]
    similarity = compare_review_groups(review_groups)
    print('유사도', similarity)
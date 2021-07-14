def compare_histories(history_list):
    product_set = set()
    total_products = 0

    for history in history_list:
        product_set.update(tuple(history))
        total_products += len(history)
    
    return (total_products - len(product_set)) / total_products
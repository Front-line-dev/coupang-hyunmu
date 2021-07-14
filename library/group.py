product_set = set()

def compare_histories(history_list):
    for history in history_list:
        product_set.update(tuple(history))
    
    total_products = len(history_list) * len(history_list[0])
    return (total_products - len(product_set)) / total_products
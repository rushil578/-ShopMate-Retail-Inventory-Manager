def create_product(prod_name, initial_qty):
    new_item = {
        'name': prod_name,
        'qty': initial_qty
    }
    return new_item

def sale(item_obj, sold_count):
    current_stock = item_obj['qty']
    
    if sold_count > current_stock:
        return False
    else:
        item_obj['qty'] = current_stock - sold_count
        return True

def get_stock_warning(item_obj):
    limit = 10
    
    if item_obj['qty'] < limit:
        return f"LOW STOCK: Only {item_obj['qty']} left!"
    else:
        return "Stock Level: Good"

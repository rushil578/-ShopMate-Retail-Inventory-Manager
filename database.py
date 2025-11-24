def save(stock_list):
    with open("shop_data.txt", "w") as f:
        for item in stock_list:

            line = item['name'] + "|" + str(item['qty']) + "\n"
            f.write(line)

def load():
    current_stock = []
    
    try:
        with open("shop_data.txt", "r") as f:
            lines = f.readlines()
            
            for line in lines:
                clean_line = line.strip()
                
                if not clean_line:
                    continue
                
                parts = clean_line.split("|")

                product = {'name': parts[0], 'qty': int(parts[1])}
                
                current_stock.append(product)
                
    except FileNotFoundError:
        return []

    return current_stock

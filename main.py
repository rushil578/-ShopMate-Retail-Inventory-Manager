import database
import inventory

def show_options():
    print("\n--- ShopMate: Retail Manager ---")
    print("1. Add New Stock")
    print("2. Sell Item")
    print("3. View Inventory & Warnings")
    print("4. Save & Exit")

def main():
    shop_inventory = database.load()
    print(f"System Loaded. Tracking {len(shop_inventory)} unique items")

    while True:
        show_options()
        choice = input("Select Action (1-4): ")

        if choice == "1":
            try:
                p_name = input("Enter Product Name: ")
                p_qty = int(input("Enter Initial Quantity: "))

                new_entry = inventory.create_product(p_name, p_qty)
                
                shop_inventory.append(new_entry)
                print(f"{p_name} added to shelves")
            except ValueError:
                print("Error: Quantity must be a number")

        elif choice == "2":
            target = input("What item is being sold? ")
            found = False
            
            for item in shop_inventory:
                if item['name'] == target:
                    found = True
                    try:
                        qty_sold = int(input(f"How many {target}s to sell? "))
                        
                        success = inventory.sale(item, qty_sold)
                        
                        if success:
                            print("Sale successful! Inventory updated")
                        else:
                            print("Error: Not enough stock to complete sale")
                    except ValueError:
                        print("Invalid number entered")
                    
                    break
            
            if not found:
                print("Item not found in database")

        elif choice == "3":
            print("\n--- Current Stock Levels ---")
            for item in shop_inventory:
                status = inventory.get_stock_warning(item)
                print(f"{item['name']} : {item['qty']} units [{status}]")

        elif choice == "4":
            database.save(shop_inventory)
            print("Inventory saved to file. Closing shop...")
            break
        
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()

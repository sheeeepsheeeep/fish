# Empty list cart 
cart = []

# Model Kits 
mk = [
    {'code': 'M1', 'name': 'Bandai PG 1/60 Strike Freedom Gundam (5063056)', 'price': 899.00},
    {'code': 'M2', 'name': 'Bandai PG 1/60 Unicorn Gundam 02 Banshee Norn (5064232)', 'price': 799.00},
    {'code': 'M3', 'name': 'Bandai PG 1/60 RX-0 Unicorn Gundam (5063513)', 'price': 749.00},
    {'code': 'M4', 'name': 'Bandai PG 1/60 Strike Rouge + Sky Grasper (5064234)', 'price': 699.00},
    {'code': 'M5', 'name': 'Bandai PG 1/60 Zeta Gundam (5064233) / Z Gundam', 'price': 699.00}
]

# Model Figurines 
mf = [
    {'code': 'F1', 'name': 'GSC Freeing Hatsune Miku : My Dear Bunny Ver. Figurine', 'price': 1599.00},
    {'code': 'F2', 'name': 'GSC Star Guardian Ahri Action Figure', 'price': 1049.00},
    {'code': 'F3', 'name': 'Bandai Tamashii Nations Figuarts Zero Monkey.D.Luffy -Red Roc- ', 'price': 1199.00},
    {'code': 'F4', 'name': 'GSC Asuka Langley Figurine - Rebuild of Evangelion', 'price': 810.00},
    {'code': 'F5', 'name': 'Kotobukiya Aether / Lumine with Bonus Face Parts ', 'price': 699.00}
]

# Main Menu 
def menu():
    print(" \n 1 - View Bandai Model Kits Section")
    print(" 2 - View Figurines Section")
    print(" 3 - View Shopping Cart")
    print(" 4 - Checkout")
    print(" 5 - Exit")

# User Choices loop 
while True:
    print("Welcome to the Sheeeps Toy Store")
    menu()
    option = int(input("Please choose an action: "))

    # exit 
    if option == 5:
        print("Thank you for using the Sheeeps Toy Store POS System")
        break

    # view model kits - mk
    elif option == 1:
        while True:
            print(" ")
            for item in mk:
                print(f"{item['code']} {item['name']} RM {item['price']:.2f}")
            print(" ")
            
            choice = input("Enter the code of the item you want to add to the cart or type 'quit' to return to the main menu: ")
            
            if choice.lower() == 'quit':
                break
            
            for item in mk:
                if item['code'] == choice:
                    cart.append(item)
                    print(f"\n{item['name']} has been added to your cart.")
                    break
            else:
                print("\nInvalid code. Please try again.")

    # view model figurines - mf 
    elif option == 2:
        print(" ")
        while True:
            for item in mf:
                print(f"{item['code']} {item['name']} RM {item['price']:.2f}")
            print("")
            
            choice = input("Enter the code of the item you want to add to the cart or type 'quit' to return to the main menu.: ")
            
            if choice.lower() == 'quit':
                break
            
            for item in mf:
                if item['code'] == choice:
                    cart.append(item)
                    print(f"\n{item['name']} has been added to your cart.")
                    break
            else:
                print("\nInvalid code. Please try again.")

    # view shopping cart - view items in list 
    elif option == 3:
        print(" ")
        print("The items in your shopping cart are: ")
        print(" ")
        for item in cart:
            print(f"{item['name']} RM {item['price']:.2f}")

    # checkout 
    elif option == 4:
        
        if len(cart) == 0:
            print("Your shopping cart is empty.")
            print(" ")
            print("Thank You for visiting Sheeeps Toy Store, Please come again")
            
        
        else:
            print(" ")
            subtotal = sum(item['price'] for item in cart)
            print(f"Subtotal: RM {subtotal:.2f}")
        
            
            tax = float(input("Please enter the Tax Percentage: "))
            disc = float(input("Please enter the Discount Percentage: "))
            
            tax1 = subtotal * (tax / 100)
            disc1 = subtotal * (disc / 100)
                
            
            final = subtotal + tax1 - disc1
                
            
            print(f"Total after tax and discount: RM {final:.2f}")
        
            
            payment = float(input("Please enter the amount paid: "))
        
             
            change = payment - final
                
            if change == 0:
                print("Payment done")
            elif change > 0:
                print(f"Change Amount: RM {change:.2f}")
        
            elif change < 0:
                left = -change
                print(f"Please pay the remaining amount of: RM {left:.2f}")
        
            else:
                print("Invalid amount.")
                
            
            print("1 - Yes")
            print("2 - No")
            receipt = int(input("Do you want the receipt?: "))
    
    
            if receipt != 1 and receipt != 2:
                print("Invalid Option")
    
            elif receipt == 2:
                print("\nThank You for visiting Sheeeps Toy Store")
    
            elif receipt == 1:
                print("--------------------------------")
                print("       SHEEEPS TOY STORE        ")
                print("--------------------------------")
    
                print("Item                              Unit Price")
                for item in cart:
                    print(f"{item['name']} RM {item['price']:.2f}") 
    
                print(f"Subtotal:               {subtotal:.2f}")
                print(f"Tax Amount:               {tax1:.2f}")
                print(f"Discount Amount:         {disc1:.2f}")
                print(f"Final Total:             {final:.2f}")
    
                print(f"\nChange Amount:            {change:.2f}")
    
                print("Thank You for visiting Sheeeps Toy Store, Please come again")
                break

    else:
        print("Invalid option. Please choose again.")
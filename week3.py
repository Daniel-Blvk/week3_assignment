price = int(input("Enter the price: "))
discount_percent = int(input("Enter the discount percent: "))
def calculate_discount(price, discount_percent):
    
    if discount_percent < 0 or discount_percent > 100:
        print("Discount percent must be between 0 and 100")
        print ("original price = ", price, "ksh")
    elif discount_percent <20:
        print("discount cannot be less than 20%")
        print ("original price = ", price, "ksh")
    
    else:
        discount=price*(discount_percent/100)
        price_after_discount=price-discount
        print(f"final price is: {price_after_discount} ksh")
    

    

calculate_discount(price, discount_percent)




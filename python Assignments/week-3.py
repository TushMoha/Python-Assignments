
# Question 1: Discount Calculator

# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Ask user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Discount applied! Final price: {final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: {final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.") 

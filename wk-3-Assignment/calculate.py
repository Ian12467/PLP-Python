def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to apply.

    Returns:
    float: The final price after applying the discount, or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Prompt the user for input
original_price = input("Enter the original price of the item: ")
discount_percentage = input("Enter the discount percentage: ")

# Validate inputs
if original_price.replace('.', '', 1).isdigit() and discount_percentage.replace('.', '', 1).isdigit():
    original_price = float(original_price)
    discount_percentage = float(discount_percentage)

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result
    if discount_percentage >= 20:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
else:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
# Assignment: Calculate Discount

## Task Description

Create a function named `calculate_discount(price, discount_percent)` that calculates the final price after applying a discount. 

### Function Requirements:
- The function should take the following parameters:
    - `price`: The original price of the item.
    - `discount_percent`: The discount percentage to be applied.
- If the discount is **20% or higher**, apply the discount and return the final price.
- If the discount is less than 20%, return the original price.

### User Interaction:
1. Use the `calculate_discount` function to:
     - Prompt the user to enter the original price of an item.
     - Prompt the user to enter the discount percentage.
2. Print the final price after applying the discount.
3. If no discount was applied, print the original price.

### Example:
```python
# Example usage of the function
final_price = calculate_discount(100, 25)
print(final_price)  # Output: 75.0
```
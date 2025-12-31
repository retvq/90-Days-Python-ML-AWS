# NOTE Shopping Bill Calculator
print("=" * 55)
print("         🛒 SHOPPING BILL CALCULATOR")
print("=" * 55)
items = int(input("Enter the number of items: ").strip())
print(f"\nEnter details for {items} items to generate your bill.\n")
item_name = []
item_price = []
item_quantity = []
total_price = []
coupons = ['NEW', 'FIRST', 'SAVE10']
item_category = []
tax_amount = 0
TAX_RATES = {
    "grocery": 0.02,
    "electronics": 0.18,
    "clothing": 0.05,
    "books": 0.00,
    "default": 0.08
}
for i in range(0, items):
    print(f"ITEM {i+1}:\n")
    item_name.append(input(f" Item{i+1} name: ").strip())
    item_price.append(float(input(f" Item{i+1} Price ($): ").strip()))
    item_quantity.append(int(input(f" Item{i+1} Quantity: ").strip()))
    item_category.append(input(" Item category (grocery/electronics/clothing/books): ").strip().lower())
    total_price.append(item_price[i] * item_quantity[i])
    tax_amount += total_price[i] * TAX_RATES.get(item_category[i], TAX_RATES["default"])
    print(f"Total Bill (without Tax): ${total_price[i]:.2f}")
    
subtotal = sum(total_price)
tax_amount = subtotal * TAX_RATE
total = subtotal + tax_amount



# Calculate discount (let's add a simple discount rule)
DISCOUNT_THRESHOLD = 100.00
DISCOUNT_RATE = 0.10  # 10% discount for orders over $100

if subtotal >= DISCOUNT_THRESHOLD:
    discount = subtotal * DISCOUNT_RATE
    total = subtotal - discount + tax_amount
    discount_applied = True
else:
    discount = 0
    discount_applied = False

# --------------------------------------------------
# STEP 5: Generate receipt
# --------------------------------------------------
print("\n")
print("=" * 55)
print("                  📃 RECEIPT")
print("=" * 55)

# Print items with aligned formatting
# The :30 means 30 character width, < means left-align
# The :>10 means 10 character width, > means right-align
print(f"  {'ITEM':<10}  {'QUANTITY':>10} {'PRICE':>10} {'TOTAL':>10}")
print("-" * 55)
for i in range (0, items):
    print(f"  {item_name[i]:<10} {item_quantity[i]:>10} {item_price[i]:>10.2f} {total_price[i]:>10.2f}")
print("-" * 55)

# Subtotal and tax
print(f"  {'Subtotal:':<30} ${subtotal:>9.2f}")

# Show discount if applicable
if discount_applied:
    print(f"  {'Discount (10%):':<30} -${discount:>8.2f}")

print(f"  {'Tax (8%):':<30} ${tax_amount:>9.2f}")
print("=" * 55)
print(f"  {'TOTAL:':<30} ${total:>9.2f}")
print("=" * 55)

# --------------------------------------------------
# STEP 6: Payment information
# --------------------------------------------------
print("\n💳 PAYMENT OPTIONS:")
print("-" * 55)
print(f"  Pay in 3 installments: ${total/3:.2f}/month")
print(f"  Pay in 6 installments: ${total/6:.2f}/month")
print(f"  Pay in 12 installments: ${total/12:.2f}/month")

# Savings message
if discount_applied:
    print(f"\n🎉 You saved ${discount:.2f} with our 10% discount!")
else:
    remaining_for_discount = DISCOUNT_THRESHOLD - subtotal
    print(f"\n💡 Spend ${remaining_for_discount:.2f} more for 10% off!")

print("\n" + "=" * 55)
print("        Thank you for shopping with us! 🛍️")
print("=" * 55)

Coupon_available = input("Do you have a coupon code? (yes/no): ").strip().lower()
if Coupon_available == 'yes':
    coupon_code = input("Enter your coupon code: ").strip().upper()
    if coupon_code == 'NEW':
        discount = total * 0.10
        total -= discount
    elif coupon_code == 'FIRST':
        discount = total * 0.20
        total -= discount
    elif coupon_code == 'SAVE10':
        discount = total * 0.10
        total -= discount
    else:
        print("Invalid coupon code. No discount applied.")
if coupon_code == 'NEW' or coupon_code == 'FIRST' or coupon_code == 'SAVE10':
    print(f"\n🎉 You saved ${discount:.2f}")
    print("\n")
    print("=" * 55)
    print("                  📃 RECEIPT")
    print("=" * 55)

    # Print items with aligned formatting
    # The :30 means 30 character width, < means left-align
    # The :>10 means 10 character width, > means right-align
    print(f"  {'ITEM':<10}  {'QUANTITY':>10} {'PRICE':>10} {'TOTAL':>10}")
    print("-" * 55)
    for i in range (0, items):
        print(f"  {item_name[i]:<10} {item_quantity[i]:>10} {item_price[i]:>10.2f} {total_price[i]:>10.2f}")
    print("-" * 55)

    # Subtotal and tax
    print(f"  {'Subtotal:':<30} ${subtotal:>9.2f}")

    # Show discount if applicable
    if discount_applied:
        print(f"  {'Discount (10%):':<30} -${discount:>8.2f}")

    print(f"  {'Tax (8%):':<30} ${tax_amount:>9.2f}")
    print("=" * 55)
    print(f"  {'TOTAL after discount:':<30} ${total:>9.2f}")
    print("=" * 55)

    # --------------------------------------------------
    # STEP 6: Payment information
    # --------------------------------------------------
    print("\n💳 PAYMENT OPTIONS:")
    print("-" * 55)
    print(f"  Pay in 3 installments: ${total/3:.2f}/month")
    print(f"  Pay in 6 installments: ${total/6:.2f}/month")
    print(f"  Pay in 12 installments: ${total/12:.2f}/month")

    # Savings message
    if discount_applied:
        print(f"\n🎉 You saved ${discount:.2f} with our 10% discount!")
    else:
        remaining_for_discount = DISCOUNT_THRESHOLD - subtotal
        print(f"\n💡 Spend ${remaining_for_discount:.2f} more for 10% off!")

    print("\n" + "=" * 55)
    print("        Thank you for shopping with us! 🛍️")
    print("=" * 55)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
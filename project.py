print("Ronny Joel Illicachi")
shares = 1000
selling_price = 33.92
purchase_price = 33.87
commission_rate = 0.02

amount_paid_for_stock = shares * purchase_price
purchase_commission = amount_paid_for_stock * commission_rate

amount_received_from_sale = shares * selling_price
sale_commission = amount_received_from_sale * commission_rate

net = (amount_received_from_sale - sale_commission) - (amount_paid_for_stock + purchase_commission)

print("Amount paid for the stock: $", format(amount_paid_for_stock, ",.2f"))
print("Commission paid on purchase: $", format(purchase_commission, ",.2f"))
print("Amount received from the sale: $", format(amount_received_from_sale, ",.2f"))
print("Commission paid on sale: $", format(sale_commission, ",.2f"))
print("Net amount left over after everything: $", format(net, ",.2f"))

if net > 0:
    print("Joe made a profit.")
elif net < 0:
    print("Joe lost money.")
else:
    print("Joe broke even.")

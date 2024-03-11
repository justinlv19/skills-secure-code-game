'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

# Over/Underflow protection
# Validate user inputs (amount/quantity)
# Sanity check (maximum total)

from collections import namedtuple
from decimal import *

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_ITEM_AMOUNT = 100000 # maximum price of item in the shop
MIN_ITEM_AMOUNT = 0 # minimum price of an item in the shop
MAX_QUANTITY = 100 # maximum quantity of an item in the shop
MIN_QUANTITY = 0 # minimum quantity of an item in the shop
MAX_TOTAL = 1000000 # maximum total amount accepted for an order

def validorder(order: Order):
    net = Decimal(0)
    payment = Decimal(0)
    purchase = Decimal(0)

    for item in order.items:

        if item.type == 'payment':
            payment += Decimal(str(item.amount)) * item.quantity
        elif item.type == 'product':
            if item.quantity < MIN_QUANTITY or item.quantity > MAX_QUANTITY:
                return "Total amount payable for an order exceeded"
            elif item.amount < MIN_ITEM_AMOUNT or item.amount > MAX_ITEM_AMOUNT:
                return "Total amount payable for an order exceeded"
            elif item.quantity != int(item.quantity):
                return "Invalid quantity"
            
            purchase += Decimal(str(item.amount)) * item.quantity
        else:
            return "Invalid item type: %s" % item.type

    if purchase > MAX_TOTAL:
        return "Total amount payable for an order exceeded"

    net = payment - purchase
    if net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id
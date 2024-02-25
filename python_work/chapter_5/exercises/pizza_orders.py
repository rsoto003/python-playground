'''
    creating an exercise modified based upon page 76's example.
        basically, plan is to create a function that will determine the order queue
        at a pizza shop. customers can pay extra to get their orders first.
        we need to filter the inputted orders and create a new list that puts the 
        urgent orders first in the list.
        the non-urgent orders need to go after those orders.
'''
delivery_order_queue = []
submitted_orders = [
    ['medium', 'pepperoni', 'cheese', 'tomato sauce', 'regular'],
    ['large', 'pepperoni', 'sausage', 'cheese', 'tomato sauce', 'regular'],
    ['small', 'veggie', 'urgent']
]

def order_queue(submitted_orders_list, delivery_order_list):
    print(f"delivery order list at beginning of loop: {delivery_order_list}")
    for order in submitted_orders_list:
        print('outter loop: \n')
        print(order)
        for order_trait in order:
            if order_trait == 'urgent':
                delivery_order_list.insert(0, order)
            else:
                delivery_order_list.append(order)
    print(f"delivery order list at end of loop: {delivery_order_list}\n")

order_queue(submitted_orders, delivery_order_queue)

for item in delivery_order_queue:
    print(f"item index: {delivery_order_queue.index(item)}\n\t items: {item}")
# will return once more educated...



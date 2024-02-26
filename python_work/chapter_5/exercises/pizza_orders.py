'''
    creating an exercise modified based upon page 76's example.
        basically, plan is to create a function that will determine the order queue
        at a pizza shop. customers can pay extra to get their orders first.
        we need to filter the inputted orders and create a new list that puts the 
        urgent orders first in the list.
        the non-urgent orders need to go after those orders.

    precondition: 3 orders are submitted

    expected result: 3 orders are returned, organized by priority.
'''
delivery_order_queue = []
submitted_orders = [
    ['medium', 'pepperoni', 'cheese', 'tomato sauce', 'regular'],
    ['large', 'pepperoni', 'sausage', 'cheese', 'tomato sauce', 'regular'],
    ['small', 'veggie', 'urgent']
]

def order_queue(submitted_orders_list, delivery_order_list):
    for order in submitted_orders_list:
        if 'urgent' not in order:
            delivery_order_list.append(order)
        else:
            delivery_order_list.insert(0, order)

    print('delivery orders finalizing...\n')
    for delivery_order in delivery_order_list:
        print(f"{delivery_order}")



order_queue(submitted_orders, delivery_order_queue)




from tabulate import tabulate

class Transaction:
    # Declaration of dict named cart (as in shopping cart)
    def __init__(self):
        self._cart = {}
    
    # Adding new item to the cart
    def add_item(self, item_list):
        name = item_list[0]
        if name in self._cart:
            print(f'Can\'t add item. Item "{name}" is already in the cart')
        elif len(item_list) == 3 and isinstance(item_list, list):
            qty = item_list[1]
            price = item_list[2]
            self._cart[name] = [qty, price]
            print('List of items:', self._cart)
        else:
            print('Can\'t add item. Please refer to the format : add_item([name, quantity, price per item])')    
    
    # Update item name
    def update_item_name(self, old_name, new_name):
        if isinstance(old_name, str) and isinstance(new_name, str):
            if not self._cart[old_name]:
                print(f'Can\'t update name. Item "{old_name}" does not exist')
            elif self._cart[new_name]:
                print(f'Can\'t update name. Item "{new_name}" already exists')
            else:
                self._cart[new_name] = self._cart[old_name]
                self._cart.pop(old_name)
                print('Item name has been updated!')
                print(old_name, '=>', new_name)
        else:
            print('Can\'t update name. Please refer to the format : update_item_name(old name, new name)')  

    # Update item quantity
    def update_item_qty(self, name, new_qty):
        if isinstance(name, str) and isinstance(new_qty, int):
            if name in self._cart:
                old_qty = self._cart[name][0]
                self._cart[name][0] = new_qty
                print('Item quantity has been updated!')
                print(old_qty, '=>', new_qty)
            else:
                print(f'Can\'t update quantity. Item "{name}" does not exist')
        else:
            print('Can\'t update quantity. Please refer to the format : update_item_qty(name, new quantity)')

    # Update item price
    def update_item_price(self, name, new_price):
        if isinstance(name, str) and isinstance(new_price):
            if name in self._cart:
                old_price = self._cart[name][1]
                self._cart[name][1] = new_price
                print('Item price has been updated!')
                print(old_price, '=>', new_price)
            else:
                print(f'Can\'t update price. Item {name} does not exist.')
        else:
            print('Can\'t update price. Please refer to the format : update_item_price(name, new price)')

    # Delete an item from the cart
    def delete_item(self, name):
        if self._cart[name]:
            self._cart.pop(name)
            print(self._cart)
        else:
            print(f'Item "{name}" does not exist')
    
    # Delete all items from the cart
    def reset_transaction(self):
        self._cart.clear()
        print('Cart is emptied!')

    # Display order status and summary
    def check_order(self):
        print('Order format is correct!')
        table = []
        counter = 1
        for name, qty_price in self._cart.items():
            temp_list = []
            qty, price = qty_price
            temp_list.extend([counter, name, qty, price, qty * price])
            table.append(temp_list)
            counter += 1
        cols_name = ['No', 'Item Name', 'Quantity', 'Price/Item', 'Total Price']
        print(tabulate(table, headers = cols_name, tablefmt='github'))
    
    # Determine the discount (if any)
    def _count_discount(self):
        total = 0
        discount = 0
        for _, qty_price in self._cart.items():
            qty, price = qty_price
            total += qty * price
        if total > 200_000:
            discount = 5
        elif total > 300_000:
            discount = 8
        elif total > 500_000:
            discount = 10
        return total, discount

    # Display the total price with discount (if any)
    def total_price(self):
        total, discount = self._count_discount()
        if discount > 0:
            print(f'Total transaction price Rp. {total}')
            print(f'You received a {discount}% discount')
            total *= (100 - discount) / 100
        print(f'Total transaction price to be paid Rp. {total}')

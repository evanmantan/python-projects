from transaction import Transaction


if __name__ == '__main__':
    trnsct_123 = Transaction()
    trnsct_123.add_item(['Fried Chicken', 2, 20000])
    trnsct_123.add_item(['Toothpaste', 3, 15000])
    print()
    trnsct_123.delete_item('Toothpaste')
    print()
    trnsct_123.reset_transaction()
    print()
    trnsct_123.add_item(['Fried Chicken', 2, 20000])
    trnsct_123.add_item(['Toothpaste', 3, 15000])
    trnsct_123.add_item(['Toy Car', 1, 200000])
    trnsct_123.add_item(['Instant Noodle', 5, 3000])
    trnsct_123.total_price()
    
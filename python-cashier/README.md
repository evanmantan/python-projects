# Simple Cashier Program :dollar:
To run the program, simply type `python main.py` in your terminal  
  
For now, outputs can only be modified by directly changing the code inside `main.py`  

# Learning Objectives  
1. Practice Object-Oriented Programming
2. Learn Modular Programming  

# Project Overview  
We are going to make a simple cashier program where user can add item the cart, remove it, update its details and count the total price of the transaction.  

# Project Requirements  
1. Create `Class` named `Transaction()` which we will use to track ongoing transaction
2. Create `__init__()` function that will initialize a local dictionary named `cart` that will store all items inputted by the user.
3. Create `add_item()` function that can take in user input consisting of item name, quantity and price per item and add the item to the cart.
4. Create `update_item_name()`, `update_item_qty()` and `update_item_price()` functions that can update the details of item inside the cart.
5. Create `delete_item()` function that can remove item from the cart.
6. Create `reset_transaction()` function that can remove all items from the cart.
7. Create `check_order()` function that can be used to check the status of the transaction and details of item(s) inside the cart.
8. Create `total_price()` function that can calculate the total price of the transaction.

# Test Case
We are going to use these test cases to see if our code's working properly or not.  
## Test 1: User wants to add 2 new items
code :  
![Screenshot 2023-04-16 210345](https://user-images.githubusercontent.com/96830567/232338310-9899fbdc-b000-4c4b-af87-b090228e3458.png)  
output :  
![Screenshot 2023-04-16 210410](https://user-images.githubusercontent.com/96830567/232338331-d7cb3160-a2bc-4fee-8aa1-ddadbdf3e2c8.png)  

## Test 2: User wants to remove 1 item from the cart
code :  
![Screenshot 2023-04-16 210516](https://user-images.githubusercontent.com/96830567/232338419-9296e41a-cf85-4a41-9122-e54e3487244e.png)  
output :  
![Screenshot 2023-04-16 210559](https://user-images.githubusercontent.com/96830567/232338444-81f700a9-f786-4f0c-b56a-e0a541a114da.png)


## Test 3: User wants to reset/restart the transaction
code :  
![Screenshot 2023-04-16 210533](https://user-images.githubusercontent.com/96830567/232338437-8d6b03f9-d9d4-4d65-b664-4c64f531c924.png)  
output :  
![Screenshot 2023-04-16 210607](https://user-images.githubusercontent.com/96830567/232338477-d2ae2899-9797-4bf0-b126-323e85b6ff78.png)

## Test 4: User wants to calculate the total price
code :  
![Screenshot 2023-04-16 210544](https://user-images.githubusercontent.com/96830567/232338500-b87bea49-78f1-47d9-b931-a013b2e99974.png)  
output :  
![Screenshot 2023-04-16 210617](https://user-images.githubusercontent.com/96830567/232338506-473e3857-019f-4deb-99bc-3c470b358744.png)  

# Room For Improvements
You can take this to the next level by making an interface in the terminal (or even a GUI) rather than having to change the code in main.py to modify the output or to actually operate the program.

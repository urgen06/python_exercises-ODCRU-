""""
Build a simple inventory using a list of dictionaries. Each item has a name, quantity, and price.
Support: add item, remove item, update quantity, show total inventory value.
"""
products = [
    {"name": "Apple",  "quantity": 10, "price": 150},
    {"name": "Banana", "quantity": 25, "price": 100},
    {"name": "Mango",  "quantity": 15, "price": 80},
    {"name": "Orange", "quantity": 20, "price": 120},
    {"name": "Grapes", "quantity": 8,  "price": 180}
]


def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    products.append({"name": name,"quantity": quantity,"price": price})
    print(products)

def update_product():
    ref_name = input("Enter name of the product you want to update: ").lower()

    for product in products:
        if product["name"].lower() == ref_name:
            product["quantity"] = int(input("Enter new quantity: "))
            product["price"] = float(input("Enter new price: "))
            print("Updated Successfully!!")
            print(products)
            break

    else:
        print("Product not found")

def delete_product():
    ref_name = input("Enter name of the product you want to delete: ").lower()

    for product in products:
        if product["name"].lower() == ref_name:
            products.remove(product)
            print(products)
            break
    else:
        print("Product not found")


print("--Available Operations--")
print("1. Add Product")
print("2. Update Product")
print("3. Delete Product")
print("4. Exit")

choice = input("Choose Operation: ")
if choice not in ["1","2","3","4"]:
    print("Invalid Choice")
    exit()

if choice == "1":
    add_product()
elif choice == "2":
    update_product()
elif choice == "3":
    delete_product()
elif choice == "4":
    print("GoodBye!!")
    exit()




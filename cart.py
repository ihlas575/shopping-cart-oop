import time


class Cart:
    def __init__(self):
        self.items = [
            {
                'title': "Demo Item 1",
                'price': 200,
                'units': 2,
            },

            {
                'title': "Demo Item 2",
                'price': 100,
                'units': 2,
            }
        ]

    def add_item(self):
        item_title = input("Name your item: ").lower()
        unit_price = input("Unit Price: ")
        units = input("Bought Units: ")

        if item_title != "" and unit_price != "" and units != "":
            try:
                self.items.append({
                    'title': item_title,
                    'price': int(unit_price),
                    'units': int(units),
                })

                time.sleep(1)
                print("\nItem added to cart successfully!")

            except ValueError:
                print("Price / Units must be a number")

        else:
            print("Fields cannot be empty.")

    def remove_item(self):
        if len(self.items) != 0:
            try:
                x = 1

                for item in self.items:
                    print(f"{x:0>2}. {item}")
                    x += 1

                key = int(input("Which one do you want to delete? "))

                self.items.remove(self.items[key - 1])

                time.sleep(1)
                print("\nItem removed successfully...")

            except IndexError:
                print("There's no such thing.")

            except ValueError:
                print("Keys are only acceptable. (Try to write the key)")

        else:
            print("There is no items in the cart to delete.")

    def clear_cart(self):
        if len(self.items) != 0:
            self.items.clear()
            print("\nCart cleared successfully!")

        else:
            print("There is no items in the cart to clear.")

    def check_out(self):
        total = 0

        if len(self.items) != 0:
            for i in self.items:
                total += i.get("price") * i.get("units")

            print(f"\nYour total bill is {total}")

        else:
            print("There is no items in the cart.")

    def show_cart(self):
        if len(self.items) != 0:
            for item in self.items:
                print("{title:-^30} \n".format(title=item.get("title").title()))

                for key, value in item.items():
                    print("{} - {}".format(key.title(), value))

                print("\n----------------------------\n")

        else:
            print("There is no items in the cart.")


cart = Cart()

while True:
    command = input("> ").lower()

    if command == "add":
        cart.add_item()

    elif command == "show":
        cart.show_cart()

    elif command == "clear":
        cart.clear_cart()

    elif command == "remove":
        cart.remove_item()

    elif command == "help":
        print('\n"add" - to add item to the cart \n"remove" - to remove an item from cart \n"show" - to see the all items in the cart \n"clear" - to clear the cart \n"out" - to check out \n')

    elif command == "out":
        cart.check_out()
        break

    else:
        print("Write a valid command. to get help type 'help'.")

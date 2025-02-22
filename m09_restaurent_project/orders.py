class Order:
    def __init__(self) -> None:
        self.items ={}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity # jodi item cart e thake
        else:
            self.items[item] = item.quantity # jodii item cart e na thake


    # def find_item_in_cart(self, item):
    #     """Helper method to check if the item is already in the cart"""
    #     if item in self.items:
    #         return item
    #     return None
    
    def remove(self,item):
        if item in self.items:
            del self.items[item]

    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items() )

    def clear(self):
        self.items = {}
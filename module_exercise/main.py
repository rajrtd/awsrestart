from dto import InventoryItem
from dto import ItemOrigin

def main():
    item_origin = ItemOrigin(country = "Ethiopia", production_date = "02/12/2023")
    my_item1 = InventoryItem(name = "printer", quantity = 5, serial_num = "HDOUHKJN", origin = item_origin)
    
    my_serialized_object1 = my_item1.__dict__
    print(my_serialized_object1)

    my_item2 = InventoryItem(**my_serialized_object1)
    print(my_item2.__dict__)

if __name__ == "__main__":
    main()
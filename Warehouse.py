from Product import Product


class Warehouse:

    def __init__(self, products=[]):
        self.products = products

    def __str__(self):
        for i in range(len(self.products)):
            print(self.products[i])

    def __repr__(self):
        return self.__str__()

    def add_product(self, name, description, quantity, location):
        product = Product(name, description, quantity, location)
        self.products.append(product)
        return True

    def remove_product(self, sku):
        was_removed = False
        for i in range(len(self.products)):
            if sku == self.products[i].sku:
                self.products.pop(i)
                was_removed = True
        return True if was_removed is True else False

    def get_all_location(self):
        location_list = []
        for i in range(len(self.products)):
            if self.products[i].location not in location_list:
                location_list.append(self.products[i].location)
        return location_list

    def print_products_order_by_location(self, ):
        location_dict = self.get_products_dict()
        for n in range(len(location_dict.keys())):
            print(f'Location {list(location_dict.keys())[n]}:')
            for j in range(len(location_dict.get(list(location_dict.keys())[n]))):
                print(location_dict.get(list(location_dict.keys())[n])[j])

    def get_products_dict(self):
        location_dict = {}
        for i in range(len(self.products)):
            if self.products[i].location not in location_dict.keys():
                location_dict.update(
                    {self.products[i].location: [f'{self.products[i].sku},{self.products[i].name},{self.products[i].quantity}']})
            else:
                location_dict.get(self.products[i].location).append(
                    f'{self.products[i].sku},{self.products[i].name},{self.products[i].quantity}')
        return dict(sorted(location_dict.items(), key=lambda k: len(k[1]), reverse=True))

    def print_product_by_location(self, location):
        location_dict = self.get_products_dict()
        return list(location_dict.get(location))


    def get_max_item_quantity(self):
        item = self.products[0]
        for i in range(len(self.products)):
            if int(self.products[i].quantity) > int(item.quantity):
                item = self.products[i]
        return item

    def get_location_total_quantity(self):
        location_dict = {}
        for i in range(len(self.products)):
            if self.products[i].location not in location_dict.keys():
                location_dict.update({self.products[i].location: int(self.products[i].quantity)})
            else:
                location_dict[self.products[i].location] += int(self.products[i].quantity)
        return location_dict

    def find_location_with_least_items(self):
        location_dict = self.get_location_total_quantity()
        list1 = list(location_dict.values()).copy()
        return f'location {list(location_dict.keys())[list1.index(min(list1))]} with minimum quantity of {min(list1)} products'

    def all_location_quantity(self):
        location_dict = self.get_location_total_quantity()
        for i in range(len(list(location_dict.keys()))):
            print(f'{list(location_dict.keys())[i]}: {list(location_dict.values())[i]}')

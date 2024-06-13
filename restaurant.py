class Table:
    def __init__(self,table_number):
        self.table_number=table_number
        self.bill=[]
    def order(self,item, price, quantity=1):
        found = False

        for order in self.bill:
            if order['item'] == item and order['price'] == price:
                # If item with same name and price is found, update the quantity
                order['quantity'] += quantity
                found = True
                break  # Exit the loop once the item is found and updated

        # If the item was not found, add it to the bill
        if not found:
            self.bill.append({
                'item': item,
                'price': price,
                'quantity': quantity
            })

        return self.bill
    def remove(self, item, price, quantity=1):
        for order in self.bill:
            if order['item'] == item and order['price'] == price:
                if order['quantity'] > quantity:
                    order['quantity'] -= quantity
                else:
                    self.bill.remove(order)
                return True

        return False

    def get_subtotal(self):
        return sum(order['price']*order['quantity'] for order in self.bill)


    def get_total(self,service_charge_rate):
        sub_total=self.get_subtotal()
        service_cahrge=sub_total *service_charge_rate
        total=sub_total+service_cahrge

        return {
            'Sub Total': f'£{sub_total:.2f}',
            'Service Charge': f'£{service_cahrge:.2f}',
            'Total': f'£{total:.2f}'
        }

    def split_bill(self):
        subtotal = self.get_subtotal()
        return round(subtotal / self.table_number, 2)

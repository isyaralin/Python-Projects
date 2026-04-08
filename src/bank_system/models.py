class Customer:
    def __init__(self, customer_id, name, address, phone):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone = phone

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "address": self.address,
            "phone": self.phone
        }

    @staticmethod
    def from_dict(data):
        return Customer(
            data["customer_id"],
            data["name"],
            data["address"],
            data["phone"]
        )


class Bank:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer):
        if customer.customer_id in self.customers:
            return False
        self.customers[customer.customer_id] = customer
        return True

    def get_customer(self, cid):
        return self.customers.get(cid)

    def delete_customer(self, cid):
        if cid in self.customers:
            del self.customers[cid]
            return True
        return False

    def update_customer(self, cid, name, address, phone):
        if cid not in self.customers:
            return False
        c = self.customers[cid]
        c.name = name
        c.address = address
        c.phone = phone
        return True

    def get_all(self):
        return list(self.customers.values())

    def load(self, customers):
        self.customers = {c.customer_id: c for c in customers}

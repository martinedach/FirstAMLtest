class Parcels:
    def __init__(self, parcels, speedy_shipping=False):
        self.parcels = parcels
        self.speedy_shipping = speedy_shipping
        self.delivery_costs = {'small': 3, 'medium': 8, 'large': 15, 'xl': 25}

    def calculate_size_cost(self, parcel):
        if all(dim < 10 for dim in parcel.values()):
            return self.delivery_costs['small']
        elif all(dim < 50 for dim in parcel.values()):
            return self.delivery_costs['medium']
        elif all(dim < 100 for dim in parcel.values()):
            return self.delivery_costs['large']
        else:
            return self.delivery_costs['xl']

    def calculate_cost(self):
        total_cost = 0
        items = []

        for parcel in self.parcels:
            cost = self.calculate_size_cost(parcel)
            total_cost += cost
            items.append({'item': parcel, 'cost': cost})
        if self.speedy_shipping:
            speedy_shipping_cost = total_cost
            total_cost *= 2
            items.append({'type': 'speedy_shipping', 'cost': speedy_shipping_cost})
        return {'total_cost': total_cost, 'items': items}
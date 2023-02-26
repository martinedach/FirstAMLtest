class Parcels:
    def __init__(self, parcels, speedy_shipping=False):
        self.parcels = parcels
        self.speedy_shipping = speedy_shipping
        self.delivery_costs = {'small': 3, 'medium': 8, 'large': 15, 'xl': 25}
        self.weight_limits = {'small': 1, 'medium': 3, 'large': 6, 'xl': 10}
        self.weight_charges = 2


    def calculate_size_cost(self, parcel):
        size = None
        for dim in parcel.values():
            if dim >= 200:
                size = 'xl'
                break
            elif dim >= 100:
                size = 'large'
            elif dim >= 50:
                size = 'medium'
            else:
                size = 'small'

        weight = parcel['weight']
        weight_limit = self.weight_limits[size]
        if weight > weight_limit:
            weight_charge = (weight - weight_limit) * self.weight_charges
            size_cost = self.delivery_costs[size] + weight_charge
        else:
            size_cost = self.delivery_costs[size]
        
        return size_cost

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
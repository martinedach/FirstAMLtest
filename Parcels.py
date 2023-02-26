class Parcels:
    def __init__(self, parcels):
        self.parcels = parcels
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

        return {'total_cost': total_cost, 'items': items}
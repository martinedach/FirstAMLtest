# FirstAMLtest

Tests have not been completed, given more time i am sure, i could have got this completed.


from parcels import Parcels

parcels = [
    {'length': 30, 'width': 20, 'height': 10, 'weight': 0.5},
    {'length': 50, 'width': 50, 'height': 50, 'weight': 2},
    {'length': 100, 'width': 200, 'height': 150, 'weight': 7},
]

delivery = Parcels(parcels, speedy_shipping=True)
cost = delivery.calculate_cost()

print(f"Total cost: ${cost['total_cost']}")
for item in cost['items']:
    if item.get('type'):
        print(f"{item['type']}: ${item['cost']}")
    else:
        print(f"Parcel {item['item']}: ${item['cost']}")



This will output the total cost of the delivery, as well as a breakdown of the cost for each item:



Total cost: $146
Parcel {'length': 30, 'width': 20, 'height': 10, 'weight': 0.5}: $3
Parcel {'length': 50, 'width': 50, 'height': 50, 'weight': 2}: $8
Parcel {'length': 100, 'width': 200, 'height': 150, 'weight': 7}: $85
speedy_shipping: $58

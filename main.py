from Parcels import Parcels

parcels_list = [
    {'length': 8, 'width': 7, 'height': 2, 'weight': 1.2},
    {'length': 35, 'width': 40, 'height': 30, 'weight': 7},
    {'length': 110, 'width': 80, 'height': 60, 'weight': 20},
    {'length': 200, 'width': 150, 'height': 100, 'weight': 50}
    ]

#Implementation step 1

parcels_obj = Parcels(parcels_list)
results = parcels_obj.calculate_cost()
print("-------------------------------------------------------------**************************************---------------------------------------------")
print("Total cost of parcels:", results['total_cost'])
print("Items:")
for item in results['items']:
     print(item)


#Implementation step 2

parcels_obj = Parcels(parcels_list,speedy_shipping=True)
results = parcels_obj.calculate_cost()
print("-------------------------------------------------------------**************************************---------------------------------------------")
print("Total cost of parcels:", results['total_cost'])
print("Items:")
for item in results['items']:
     print(item)



#Implementation step 3

parcels_obj = Parcels(parcels_list,speedy_shipping=True)
results = parcels_obj.calculate_cost()
print("-------------------------------------------------------------**************************************---------------------------------------------")
print("Total cost of parcels:", results['total_cost'])
print("Items:")
for item in results['items']:
     print(item)
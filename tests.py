import unittest
from Parcels import Parcels

class TestParcels(unittest.TestCase):

    def test_calculate_size_cost_small_parcel_within_weight_limit(self):
     parcels = [{'length': 10, 'width': 10, 'height': 10, 'weight': 0.5}]
     delivery = Parcels(parcels)
     self.assertEqual(delivery.calculate_size_cost(parcels[0]), 3)
    
    def test_calculate_size_cost_small_parcel_over_weight_limit(self):
     parcels = [{'length': 10, 'width': 10, 'height': 10, 'weight': 2}]
     delivery = Parcels(parcels)
     self.assertEqual(delivery.calculate_size_cost(parcels[0]), 7)
    
    def test_calculate_size_cost_medium_parcel_within_weight_limit(self):
     parcels = [{'length': 60, 'width': 60, 'height': 60, 'weight': 2}]
     delivery = Parcels(parcels)
     self.assertEqual(delivery.calculate_size_cost(parcels[0]), 8)
    
    def test_calculate_size_cost_medium_parcel_over_weight_limit(self):
     parcels = [{'length': 60, 'width': 60, 'height': 60, 'weight': 5}]
     delivery = Parcels(parcels)
     self.assertEqual(delivery.calculate_size_cost(parcels[0]), 18)
    
    def test_calculate_size_cost_large_parcel_within_weight_limit(self):
     parcels = [{'length': 110, 'width': 110, 'height': 110, 'weight': 4}]
     delivery = Parcels(parcels)
     self.assertEqual(delivery.calculate_size_cost(parcels[0]), 15)
    
    def test_calculate_size_cost_large_parcel_over_weight_limit(self):
      parcels = [{'length': 110, 'width': 110, 'height': 110, 'weight': 10}]
      delivery = Parcels(parcels)
      self.assertEqual(delivery.calculate_size_cost(parcels[0]), 35)
    
    def test_calculate_size_cost_xl_parcel_within_weight_limit(self):
      parcels = [{'length': 210, 'width': 210, 'height': 210, 'weight': 6}]
      delivery = Parcels(parcels)
      self.assertEqual(delivery.calculate_size_cost(parcels[0]), 25)
    
    def test_calculate_size_cost_xl_parcel_over_weight_limit(self):
     parcels = [{'length': 210, 'width': 210, 'height': 210, 'weight': 15}]
     delivery = Parcels(parcels)
     self.assertEqual(delivery.calculate_size_cost(parcels[0]), 55)
    
    def test_calculate_size_cost_heavy_parcel_within_weight_limit(self):
     parcels = [{'length': 100, 'width': 100, 'height': 100, 'weight': 20}]
     delivery = Parcels(parcels)
     self.assertEqual(delivery.calculate_size_cost(parcels[0]), 50)

    def test_calculate_size_cost_heavy_parcel_over_weight_limit(self):
     parcels = [{'length': 100, 'width': 100, 'height': 100, 'weight': 60}]
     delivery = Parcels(parcels)
     self.assertEqual(delivery.calculate_size_cost(parcels[0]), 110)
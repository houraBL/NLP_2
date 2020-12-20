import unittest
from nataly.address_extractor import NERAddressModel


class TestStreet(unittest.TestCase):
    def setUp(self):
        self.AddresParser = NERAddressModel()

    def test_shkolnaya(self):
        testing_address = 'санкт-петербург школьная 20'
        res = self.AddresParser.predict(testing_address)
        self.assertEqual('санкт-петербург', res['city'])
        self.assertEqual(('школьная', None), (res['street'], res['street_type']))
        self.assertEqual(('20', None),  (res['house_number'], res['house_number_2']))

    def test_full_gagarina(self):
        testing_address = 'санкт-петербург юрия гагарина 22 к2'
        res = self.AddresParser.predict(testing_address)
        self.assertEqual('санкт-петербург', res['city'])
        self.assertEqual(('юрия гагарина', None), (res['street'], res['street_type']))
        self.assertEqual(('22', '2'),  (res['house_number'], res['house_number_2']))

    def test_short_gagarina(self):
        testing_address = 'питер гагарина 22 к2'
        res = self.AddresParser.predict(testing_address)
        print(str(res))
        self.assertEqual('санкт-петербург', res['city'])
        self.assertEqual(('гагарина', None), (res['street'], res['street_type']))
        self.assertEqual(('22', '2'), (res['house_number'], res['house_number_2']))

    def test_untolovsky(self):
        testing_address = "санкт-петербург;юнтоловский 43 корпус 1"
        res = self.AddresParser.predict(testing_address)
        print(str(res))
        self.assertEqual('санкт-петербург', res['city'])
        self.assertEqual(('юнтоловский', None), (res['street'], res['street_type']))
        self.assertEqual(('43', '1'),  (res['house_number'], res['house_number_2']))

    def test_untolovsky_spb_str(self):
        testing_address = "санкт-петербург;юнтоловский 43 строение 1"
        res = self.AddresParser.predict(testing_address)
        self.assertEqual('санкт-петербург', res['city'])
        self.assertEqual(('юнтоловский', None), (res['street'], res['street_type']))
        self.assertEqual(('43', '1'),  (res['house_number'], res['house_number_2']))

    def test_untolovsky_str(self):
        testing_address = "юнтоловский 43 ст 1"
        res = self.AddresParser.predict(testing_address)
        self.assertEqual(('юнтоловский', None), (res['street'], res['street_type']))
        self.assertEqual(('43', '1'),  (res['house_number'], res['house_number_2']))

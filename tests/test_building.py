import unittest

from nataly.address_extractor import NERAddressModel


class TestHome(unittest.TestCase):
    def setUp(self):
        self.NERInstance = NERAddressModel()

    def test_1(self):
        testing_address = 'проспект комсомольский 50'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual((res['house_number'], res['house_number_2']), ('50', None))

    def test_2(self):
        testing_address = 'город липецк улица катукова 36 а'
        res = self.NERInstance.predict(testing_address)
        print(str(res))
        self.assertEqual((res['house_number'], res['house_number_2']), ('36 а', None))

    def test_3(self):
        testing_address = 'сургут улица рабочая дом 31а'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual((res['house_number'], res['house_number_2']), ('31а', None))

    def test_4(self):
        testing_address = 'город липецк доватора 18'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual((res['house_number'], res['house_number_2']), ('18', None))

    def test_5(self):
        testing_address = 'ну бехтеева 9 квартира 310'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual((res['house_number'], res['house_number_2']), ('9', None))

    def test_6(self):
        testing_address = 'артема 32 квартира 8'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual((res['house_number'], res['house_number_2']), ('32', None))

    def test_7(self):
        testing_address = 'город липецк полиграфическая дом 4'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual((res['house_number'], res['house_number_2']), ('4', None))

    def test_8(self):
        testing_address = 'сколько стоит нет arkadata у нас есть москва каширское шоссе 55 корпус 1'
        res = self.NERInstance.predict(testing_address)
        print(str(res))
        self.assertEqual((res['house_number'], res['house_number_2']), ('55', '1'))

    def test_9(self):
        testing_address = 'люберцы октябрьский проспект 10 корпус 1'
        res = self.NERInstance.predict(testing_address)
        print(str(res))
        self.assertEqual((res['house_number'], res['house_number_2']), ('10', '1'))

    def test_10(self):
        testing_address = 'бульвар миттова 24'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual((res['house_number'], res['house_number_2']), ('24', None))

    def test_11(self):
        testing_address = 'стол вы знаете москва алтуфьевское 78'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual((res['house_number'], res['house_number_2']), ('78', None))


if __name__ == '__main__':
    unittest.main()

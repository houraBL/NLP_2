import unittest

from nataly.address_extractor import NERAddressModel


class TestStreet(unittest.TestCase):
    def setUp(self):
        self.NERInstance = NERAddressModel()

    def test_one(self):
        testing_address = 'проспект комсомольский 50'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(('комсомольский', 'проспект'), (res['street'], res['street_type']))
        self.assertEqual(('50', None), (res['house_number'], res['house_number_2']))

    def test_second(self):
        testing_address = 'город липецк улица катукова 36 а'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual('липецк', res['city'])
        self.assertEqual(('катукова', 'улица'), (res['street'], res['street_type']))
        self.assertEqual(('36 а', None), (res['house_number'], res['house_number_2']))

    def test_third(self):
        testing_address = 'сургут улица рабочая дом 31а'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual('сургут', res['city'])
        self.assertEqual(('рабочая', 'улица'), (res['street'], res['street_type']))
        self.assertEqual(('31а', None), (res['house_number'], res['house_number_2']))

    def test_fouth(self):
        testing_address = 'город липецк доватора 18'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual('липецк', res['city'])
        self.assertEqual(('доватора', None), (res['street'], res['street_type']))
        self.assertEqual(('18', None), (res['house_number'], res['house_number_2']))

    def test_behtereva(self):
        testing_address = 'ну бехтеева 9 квартира 310'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(None, res['city'])
        self.assertEqual(('бехтеева', None), (res['street'], res['street_type']))
        self.assertEqual(('9', None), (res['house_number'], res['house_number_2']))
        self.assertEqual('310', res['apartment'])

    def test_moskovskaya(self):
        testing_address = 'московская 34б'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(None, res['city'])
        self.assertEqual(('московская', None), (res['street'], res['street_type']),)
        self.assertEqual(('34б', None), (res['house_number'], res['house_number_2']))
        self.assertEqual(None, res['apartment'])

    def test_minina(self):
        testing_address = 'улица минина дом 1'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(None, res['city'])
        self.assertEqual(('минина', 'улица'), (res['street'], res['street_type']))
        self.assertEqual(('1', None), (res['house_number'], res['house_number_2']))
        self.assertEqual(None, res['apartment'])

    def test_30_let_victory(self):
        testing_address = 'сколько улица 30 лет победы 50 46'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(None, res['city'])
        self.assertEqual(('30 лет победы', 'улица'), (res['street'], res['street_type']))
        self.assertEqual(('50', None), (res['house_number'], res['house_number_2']))
        self.assertEqual('46', res['apartment'])

    def test_tract(self):
        testing_address = 'тюменский тракт 10'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(None, res['city'])
        self.assertEqual(('тюменский', 'тракт'), (res['street'], res['street_type']))
        self.assertEqual(('10', None), (res['house_number'], res['house_number_2']))
        self.assertEqual(None, res['apartment'])

    def test_beregovaya(self):
        testing_address = 'береговая 43 береговая 43 сургут'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual('сургут', res['city'])
        self.assertEqual(('береговая', None), (res['street'], res['street_type']))
        self.assertEqual(('43', None), (res['house_number'], res['house_number_2']))
        self.assertEqual(None, res['apartment'])

    def test_yuogorskaya(self):
        testing_address = 'сургут югорская 30/2'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual('сургут', res['city'])
        self.assertEqual(('югорская', None), (res['street'], res['street_type']))
        self.assertEqual(('30/2', None), (res['house_number'], res['house_number_2']))
        self.assertEqual(None, res['apartment'])

    def test_index(self):
        testing_address = 'индекс 12 мне вот этого не надо'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(None, res['city'])
        self.assertEqual((None, None), (res['street'], res['street_type']))
        self.assertEqual((None,  None), (res['house_number'], res['house_number_2']))
        self.assertEqual(None, res['apartment'])

    def test_salmanova(self):
        testing_address = 'город сургут улица фармана салманова 4'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual('сургут', res['city'])
        self.assertEqual(('фармана салманова', 'улица'), (res['street'], res['street_type']), )
        self.assertEqual(('4', None), (res['house_number'], res['house_number_2']))
        self.assertEqual(None, res['apartment'])

    def test_vidnoe(self):
        testing_address = 'зеленые аллеи город видное дом 8'
        res = self.NERInstance.predict(testing_address)
        print(str(res))
        self.assertEqual('видное', res['city'])
        self.assertEqual(('зеленые', 'аллеи'), (res['street'], res['street_type']),)
        self.assertEqual(('8', None), (res['house_number'], res['house_number_2']))
        self.assertEqual(None, res['apartment'])

    def test_zelinskogo(self):
        testing_address = 'зелинского улица зелинского дом 2'
        res = self.NERInstance.predict(testing_address)
        print(str(res))
        self.assertEqual(None, res['city'])
        self.assertEqual(('зелинского', 'улица'), (res['street'], res['street_type']))
        self.assertEqual(('2', None), (res['house_number'], res['house_number_2']))
        self.assertEqual(None, res['apartment'])

    def test_kuskovaya_corpus(self):
        testing_address = 'Кусковская 19 корпус 1 '
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(None, res['city'])
        self.assertEqual(('Кусковская', None), (res['street'], res['street_type']), )
        self.assertEqual(('19', '1'), (res['house_number'], res['house_number_2']))
        self.assertEqual(None, res['apartment'])

    def test_shosse(self):
        testing_address = 'москва щелковское шоссе 35'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual('москва', res['city'])
        self.assertEqual(('щелковское', 'шоссе'), (res['street'], res['street_type']), )
        self.assertEqual(('35', None), (res['house_number'], res['house_number_2']))
        self.assertEqual(None, res['apartment'])

    def test_park(self):
        testing_address = 'город москва марьинский парк дом 25 корпус 2'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual('москва', res['city'])
        self.assertEqual(('марьинский парк', None), (res['street'], res['street_type']),)
        self.assertEqual(('25', '2'), (res['house_number'], res['house_number_2']))
        self.assertEqual(None, res['apartment'])

    def test_gai(self):
        testing_address = 'Старый Гай 1 корпус 2'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(('Старый Гай', None), (res['street'], res['street_type']))
        self.assertEqual(('1', '2'), (res['house_number'], res['house_number_2']))
        self.assertEqual(None, res['apartment'])

    def test_third_post(self):
        testing_address = 'улица 3 почтовое отделение дом 62'
        res = self.NERInstance.predict(testing_address)
        print(str(res))
        self.assertEqual(None, res['city'])
        self.assertEqual(('3 почтовое отделение', 'улица'), (res['street'], res['street_type']), )
        self.assertEqual(('62', None), (res['house_number'], res['house_number_2']))
        self.assertEqual(None, res['apartment'])

    def test_july_street(self):
        testing_address = 'нижний новгород улица июльских дней 19'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual('нижний новгород', res['city'])
        self.assertEqual(('июльских дней', 'улица'), (res['street'], res['street_type']), )
        self.assertEqual(('19', None), (res['house_number'], res['house_number_2']))
        self.assertEqual(None, res['apartment'])

    def test_val(self):
        testing_address = 'так москва хамовнический вал но я думаю что я еще обсужу со своими домашними то есть вот у нас цифровое телевидение есть но акадо вот вы не спешите я тогда вам наберу но либо в приложения'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual('москва', res['city'])
        self.assertEqual(('хамовнический вал', None), (res['street'], res['street_type']), )
        self.assertEqual((None, None), (res['house_number'], res['house_number_2']))
        self.assertEqual(None, res['apartment'])

    def test_semen_bilecky(self):
        testing_address = 'город сургут улица семена билецкого 1'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual('сургут', res['city'])
        self.assertEqual(('семена билецкого', 'улица'), (res['street'], res['street_type']), )
        self.assertEqual(('1', None), (res['house_number'], res['house_number_2']))
        self.assertEqual(None, res['apartment'])

    def test_critical(self):
        testing_address = 'улица значит антонова овсиенко дом 19/2'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual('антонова овсиенко', (res['street']))
        self.assertEqual(('19/2', None), (res['house_number'], res['house_number_2']))

    def test_critical0(self):
        testing_address = 'улица генерала армии епишева дом 9'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(('генерала армии епишева', 'улица'), (res['street'], res['street_type']))
        self.assertEqual(('9', None), (res['house_number'], res['house_number_2']))

    def test_critical1(self):
        testing_address = 'улица академика байкова дом 9'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(('9', None), (res['house_number'], res['house_number_2']))
        self.assertEqual(('академика байкова', 'улица'), (res['street'], res['street_type']))

    def test_critical2(self):
        testing_address = 'улица академика байкова дом дом дом 9'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(('9', None), (res['house_number'], res['house_number_2']))
        self.assertEqual(('академика байкова', 'улица'), (res['street'], res['street_type']))

    def test_critical2_3(self):
        testing_address = 'улица подзаборного байкова дом дом дом 9'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(('9', None), (res['house_number'], res['house_number_2']))
        self.assertEqual(('подзаборного байкова', 'улица'), (res['street'], res['street_type']))

    def test_critical2_4(self):
        testing_address = 'улица монтажника байкова дом дом дом 9'
        res = self.NERInstance.predict(testing_address)
        self.assertEqual(('9', None), (res['house_number'], res['house_number_2']))
        self.assertEqual(('монтажника байкова', 'улица'), (res['street'], res['street_type']))

    def test_critical3(self):
        testing_address = 'так значит у меня дом номер 12 а улица джона рида'
        res = self.NERInstance.predict(testing_address)
        print(str(res))
        self.assertEqual(('джона рида', 'улица'), (res['street'], res['street_type']))
        self.assertEqual(('12', None), (res['house_number'], res['house_number_2']))


if __name__ == '__main__':
    unittest.main()

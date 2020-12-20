from collections import OrderedDict
from rules.address import ADDR_PART
from yargy import Parser


class NERAddressModel:
    def __init__(self):
        self.address_extractor = Parser(ADDR_PART)
        keys = ['city', 'street', 'street_type', 'house_number', 'house_number_2', 'house_type', 'apartment', ]
        items = [(key, None) for key in keys]
        self.empty_dict = OrderedDict(items)
        self.overall_dict = {}

    def predict(self, text):
        matches = [match for match in self.address_extractor.findall(text)]
        facts = [_.fact.as_json for _ in matches]
        self.overall_dict = self.empty_dict
        if facts:
            p = facts[0]
            for key in list(p.keys()):
                self.overall_dict[str(key)] = p[str(key)]

        return self.overall_dict

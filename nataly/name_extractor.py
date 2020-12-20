from collections import OrderedDict
from rules.name import NAME
from yargy import Parser


class NERNameModel:
    def __init__(self):
        self.name_extractor = Parser(NAME)
        keys = ['first', 'last', 'middle']
        items = [(key, None) for key in keys]
        self.empty_dict = OrderedDict(items)
        self.overall_dict = {}

    def predict(self, text):
        matches = [match for match in self.name_extractor.findall(text)]
        facts = [_.fact.as_json for _ in matches]
        self.overall_dict = self.empty_dict
        if facts:
            p = facts[0]
            for key in list(p.keys()):
                self.overall_dict[str(key)] = p[str(key)]

        return self.overall_dict

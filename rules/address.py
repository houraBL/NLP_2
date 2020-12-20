from pymorphy2.lang import ru
from yargy import (
    rule,
    or_, and_,
    not_)
from yargy.predicates import (
    eq, gram, type,
    in_, in_caseless, dictionary,
    normalized, length_eq)
from yargy.interpretation import fact
from yargy.pipelines import morph_pipeline
from yargy.relations import gnc_relation
from yargy.tokenizer import QUOTES

Address = fact(
    'Address',
    ['city', 'street', 'street_type', 'house_number', 'house_number_2', 'house_type', 'apartment', ])

DASH = eq('-')
DOT = eq('.')
ADJF = gram('ADJF')
NOUN = gram('NOUN')
INT = type('INT')
APRO = gram('Apro')
GEOX = gram('Geox')
NAME = and_(gram('Name'))
SURN = and_(gram('Surn'))
ABBR = and_(gram('Abbr'))

gnc = gnc_relation()

ANUM = rule(INT, DASH.optional(), in_caseless({'я', 'й', 'е', 'ое', 'ая', 'ий', 'ой'}))

# region CITY
# Top 200 Russia cities, cover 75% of population
GOROD_WORDS = rule(normalized('город'))
CITY_COMPLEX = ([
    'санкт-петербург', 'санкт петербург', 'нижний новгород', 'н.новгород', 'ростов-на-дону', 'ростов на дону',
    'набережные челны', 'улан удэ', 'комсомольск на амуре', 'йошкар ола', 'орехово зуево', 'южно сахалинск',
    'улан-удэ', 'нижний тагил', 'комсомольск-на-амуре', 'йошкар-ола', 'старый оскол', 'великий новгород',
    'южно-сахалинск', 'петропавловск-камчатский', 'каменск-уральский', 'орехово-зуево', 'сергиев посад',
    'петропавловск камчатский', 'каменск уральский', 'ленинск кузнецкий', 'каменск шахтинский', 'усть илимск',
    'усолье сибирский', 'новый уренгой', 'ленинск-кузнецкий', 'великие луки', 'каменск-шахтинский', 'усть-илимск',
    'усолье-сибирский', 'кирово-чепецк'])
CITY_SIMPLE = dictionary([
    'москва', 'новосибирск', 'екатеринбург', 'казань', 'самара', 'омск', 'челябинск', 'уфа',
    'волгоград', 'пермь', 'красноярск', 'воронеж', 'саратов', 'краснодар', 'тольятти', 'барнаул', 'ижевск', 'ульяновск',
    'владивосток', 'ярославль', 'иркутск', 'тюмень', 'махачкала', 'хабаровск', 'оренбург', 'новокузнецк', 'кемерово',
    'рязань', 'томск', 'астрахань', 'пенза', 'липецк', 'тула', 'киров', 'чебоксары', 'калининград', 'брянск', 'курск',
    'иваново', 'магнитогорск', 'тверь', 'ставрополь', 'симферополь', 'белгород', 'архангельск', 'владимир',
    'севастополь', 'сочи', 'курган', 'смоленск', 'калуга', 'чита', 'орёл', 'волжский', 'череповец', 'владикавказ',
    'мурманск', 'сургут', 'вологда', 'саранск', 'тамбов', 'стерлитамак', 'грозный', 'якутск', 'кострома',
    'петрозаводск', 'таганрог', 'нижневартовск', 'братск', 'новороссийск', 'дзержинск', 'шахта', 'нальчик', 'орск',
    'сыктывкар', 'нижнекамск', 'ангарск', 'балашиха', 'благовещенск', 'прокопьевск', 'химки', 'псков', 'бийск',
    'энгельс', 'рыбинск', 'балаково', 'северодвинск', 'армавир', 'подольск', 'королёв', 'сызрань', 'норильск',
    'златоуст', 'мытищи', 'люберцы', 'волгодонск', 'новочеркасск', 'абакан', 'находка', 'уссурийск', 'березники',
    'салават', 'электросталь', 'миасс', 'первоуральск', 'рубцовск', 'альметьевск', 'ковровый', 'коломна', 'керчь',
    'майкоп', 'пятигорск', 'одинцово', 'копейск', 'хасавюрт', 'новомосковск', 'кисловодск', 'серпухов',
    'новочебоксарск', 'нефтеюганск', 'димитровград', 'нефтекамск', 'черкесск', 'дербент', 'камышин', 'невинномысск',
    'красногорск', 'мур', 'батайск', 'новошахтинск', 'ноябрьск', 'кызыл', 'октябрьский', 'ачинск', 'северск',
    'новокуйбышевск', 'елец', 'евпатория', 'арзамас', 'обнинск', 'каспийск', 'элиста', 'пушкино', 'жуковский',
    'междуреченск', 'сарапул', 'ессентуки', 'воткинск', 'ногинск', 'тобольск', 'ухта', 'серов', 'бердск', 'мичуринск',
    'киселёвск', 'новотроицк', 'зеленодольск', 'соликамск', 'раменский', 'домодедово', 'магадан', 'глазов',
    'железногорск', 'канск', 'назрань', 'гатчина', 'саров', 'новоуральск', 'воскресенск', 'долгопрудный', 'бугульма',
    'кузнецк', 'губкин', 'кинешма', 'ейск', 'реутов', 'железногорск', 'чайковский', 'азов', 'бузулук', 'озёрск',
    'балашов', 'юрга', 'кропоткин', 'клин', 'видное'])
CITY_ABBR = rule((normalized('питер')).interpretation(Address.city.const('санкт-петербург')))
GOROD_NAME = rule(or_(rule(CITY_SIMPLE), morph_pipeline(CITY_COMPLEX), CITY_ABBR)).interpretation(Address.city)
CITY = rule(GOROD_WORDS.optional(), GOROD_NAME, GOROD_WORDS.optional())
# endregion

# region STREET
POSITION_WORDS_DICT = or_(
    rule(
        dictionary({
            'мичман',
            'геолог',
            'подводник',
            'краевед',
            'снайпер',
            'штурман',
            'бригадир',
            'учитель',
            'политрук',
            'военком',
            'ветеран',
            'историк',
            'пулемётчик',
            'авиаконструктор',
            'адмирал',
            'академик',
            'актер',
            'актриса',
            'архитектор',
            'атаман',
            'врач',
            'воевода',
            'генерал',
            'губернатор',
            'хирург',
            'декабрист',
            'разведчик',
            'граф',
            'десантник',
            'конструктор',
            'скульптор',
            'писатель',
            'поэт',
            'капитан',
            'князь',
            'комиссар',
            'композитор',
            'космонавт',
            'купец',
            'лейтенант',
            'лётчик',
            'майор',
            'маршал',
            'матрос',
            'подполковник',
            'полковник',
            'профессор',
            'сержант',
            'старшина',
            'танкист',
            'художник',
            'герой',
            'княгиня',
            'строитель',
            'дружинник',
            'диктор',
            'прапорщик',
            'артиллерист',
            'графиня',
            'большевик',
            'патриарх',
            'сварщик',
            'офицер',
            'рыбак',
            'брат',
        })
    ),
    rule(normalized('генерал'), normalized('армия')),
    rule(normalized('герой'), normalized('россия')),
    rule(
        normalized('герой'),
        normalized('российский'), normalized('федерация')),
    rule(
        normalized('герой'),
        normalized('советский'), normalized('союз')
    ),
)
LET_NAME = in_caseless({
    'влксм',
    'ссср',
    'алтая',
    'башкирии',
    'бурятии',
    'дагестана',
    'калмыкии',
    'колхоза',
    'комсомола',
    'космонавтики',
    'москвы',
    'октября',
    'пионерии',
    'победы',
    'приморья',
    'района',
    'совхоза',
    'совхозу',
    'татарстана',
    'тувы',
    'удмуртии',
    'улуса',
    'хакасии',
    'целины',
    'чувашии',
    'якутии',
})

# modifiers
MODIFIER_WORDS_ = rule(dictionary({
    'большой',
    'малый',
    'средний',

    'верхний',
    'центральный',
    'нижний',
    'северный',
    'дальний',

    'первый',
    'второй',

    'старый',
    'новый',

    'красный',
    'лесной',
    'тихий',
}), DASH.optional())
SHORT_MODIFIER_WORDS = rule(in_caseless({
    'больше',
    'мало',
    'средне',

    'верх',
    'верхне',
    'центрально',
    'нижне',
    'северо',
    'дальне',
    'восточно',
    'западно',

    'перво',
    'второ',

    'старо',
    'ново',

    'красно',
    'тихо',
    'горно',
}), DASH.optional())

# address name
SIMPLE = and_(or_(and_(ADJF, not_(APRO), not_(normalized('домашний')), not_(normalized('дорогая'))),
                  and_(NOUN, gram('gent'), not_(normalized('дом')), not_(normalized('и'))),
                  SURN, NAME),
              not_(normalized('из')), not_(normalized('свидания')))  # (одно слово(прилаг. или сущ в род падеже))

COMPLEX = or_(
    rule(INT, normalized('лет'), SIMPLE),  # 30 лет победы
    rule(INT, and_(ADJF, not_(APRO)), normalized('отделение')),
    rule(SIMPLE.match(gnc), SIMPLE.match(gnc)),
    rule(POSITION_WORDS_DICT, SIMPLE),
    rule(SIMPLE, SURN),
    rule(SIMPLE.match(gnc), and_(NOUN, not_(APRO)).match(gnc)),
    rule(and_(NOUN, not_(normalized('дом'))), and_(ADJF, not_(APRO))))

EXCEPTION = dictionary({'арбат', 'варварка', 'печерка', 'покровка'})

ADDR_NAME = rule(or_(rule(SIMPLE), COMPLEX, rule(EXCEPTION), rule(SURN)))
STREET_NAME = ADDR_NAME.interpretation(Address.street)

# street
STREET_WORDS = rule((normalized('улица')).interpretation(Address.street_type.const('улица')))
PROEZD_WORDS = rule((normalized('проезд')).interpretation(Address.street_type.const('проезд')))
PROSPEKT_WORDS = rule((normalized('проспект')).interpretation(Address.street_type.const('проспект')))
SHOSSE_WORDS = rule((normalized('шоссе')).interpretation(Address.street_type.const('шоссе')))
NABEREG_WORDS = rule((normalized('набережная')).interpretation(Address.street_type.const('набережная')))
TRAKT_WORDS = rule((normalized('тракт')).interpretation(Address.street_type.const('тракт')))
MICRORAION_WORDS = rule((normalized('микрорайон')).interpretation(Address.street_type.const('микрорайон')))
ALLEY_WORDS = rule((normalized('аллеи')).interpretation(Address.street_type.const('аллеи')))

STREET_TYPE = rule(or_(STREET_WORDS, PROEZD_WORDS, PROSPEKT_WORDS, SHOSSE_WORDS, NABEREG_WORDS, TRAKT_WORDS,
                       MICRORAION_WORDS, ALLEY_WORDS))

STREET = or_(rule(STREET_NAME, STREET_TYPE, STREET_NAME.optional()), rule(STREET_TYPE, STREET_NAME), STREET_NAME).interpretation(Address)
# endregion

# region HOUSE
# region house value ADDR_VALUE
LETTER = in_caseless(set('абвгдежзилмнопрстуфхшщэюя'))
QUOTE = in_(QUOTES)
LETTER = or_(rule(LETTER), rule(QUOTE, LETTER, QUOTE), )
SEP = in_(r'/\-;')
VALUE = rule(INT, LETTER.optional())
VALUE = or_(
    rule(VALUE, SEP, VALUE),
    rule(VALUE, SEP, LETTER),
    rule(VALUE),
)
# endregion
ADDR_VALUE = rule(VALUE)

DOM_WORDS = rule(normalized('дом'))
DOM = ADDR_VALUE.interpretation(Address.house_number)

# korpus
KORPUS_WORDS = rule(or_(normalized('корпус'), normalized('к'))).interpretation(Address.house_type.const('корпус'))
STROENIE_WORDS = rule(or_(normalized('строение'), normalized('ст'), normalized('стр'))).interpretation(Address.house_type.const('строение'))

BUILDING = rule(or_(KORPUS_WORDS, STROENIE_WORDS)).interpretation(Address.house_type)

DOM_2 = rule(ADDR_VALUE).interpretation(Address.house_number_2)

FULL_DOM = rule(rule(DOM_WORDS.optional(), DOM_WORDS.optional(), DOM_WORDS.optional(), DOM_WORDS.optional(),
                     DOM, rule(BUILDING, DOM_2).optional()))

# endregion

# region kvartira
KVARTIRA_WORDS = rule(normalized('квартира'))
KVARTIRA_VALUE = rule(INT).interpretation(Address.apartment)
KVARTIRA = rule(KVARTIRA_WORDS.optional(), KVARTIRA_VALUE).interpretation(Address)
# endregion

# address
ADDR_PART = or_(
    rule(CITY, SEP.optional(), STREET, FULL_DOM, KVARTIRA),
    rule(CITY, SEP.optional(), STREET, FULL_DOM),
    rule(STREET, FULL_DOM, rule(STREET, FULL_DOM).optional(), CITY),
    rule(STREET, CITY, FULL_DOM),
    rule(STREET, FULL_DOM, KVARTIRA),
    rule(FULL_DOM, STREET),
    rule(FULL_DOM, KVARTIRA),
    rule(STREET, FULL_DOM),
    rule(STREET, CITY),
    rule(CITY, STREET),
    rule(STREET),
    rule(CITY),
).interpretation(Address)

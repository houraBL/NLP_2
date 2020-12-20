from yargy import (
    rule,
    and_, or_, not_
)
from yargy.relations import gnc_relation
from yargy.interpretation import fact
from yargy.predicates import gram


gnc = gnc_relation()

Name = fact(
    'Name',
    ['first', 'last', 'middle']
)

NAME = and_(gram('Name'))

PATR = and_(gram('Patr'))

SURN = and_(gram('Surn'))

ABBR = and_(gram('Abbr'))

FIRST = NAME.interpretation(Name.first).match(gnc)

LAST = and_(SURN, not_(ABBR)).interpretation(Name.last).match(gnc)

MIDDLE = PATR.interpretation(Name.middle).match(gnc)

FIRST_LAST = rule(FIRST, LAST)

LAST_FIRST = rule(LAST, FIRST)

FIRST_MIDDLE = rule(FIRST, MIDDLE)

FIRST_MIDDLE_LAST = rule(FIRST, MIDDLE, LAST)

LAST_FIRST_MIDDLE = rule(LAST, FIRST, MIDDLE)

NAME = or_(
    FIRST,
    LAST,
    MIDDLE,
    FIRST_MIDDLE,
    FIRST_LAST,
    FIRST_MIDDLE_LAST,
    LAST_FIRST,
    LAST_FIRST_MIDDLE
).interpretation(
    Name
)

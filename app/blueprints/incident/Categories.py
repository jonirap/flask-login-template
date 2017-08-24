# coding=utf-8

CATEGORIES_SET = set()


class CategoryMetaclass(type):
    def __new__(mcs, name, bases, dct):
        cls = super(CategoryMetaclass, mcs).__new__(mcs, name, bases, dct)
        if name != 'Category':
            CATEGORIES_SET.add(cls)
        return cls


class Category(object):
    __metaclass__ = CategoryMetaclass
    NAME = None
    KEYWORDS = None

    @classmethod
    def matches(cls, keywords):
        return len(keywords.intersection(cls.KEYWORDS))
        # return sum(cls.KEYWORDS.get(word, 0) for word in cls.KEYWORDS.keys())

    @staticmethod
    def get(keywords):
        if isinstance(keywords, basestring):
            keywords = keywords.split()
        keywords = set(keywords)
        matches = dict()
        for category in CATEGORIES_SET:
            matches[category.NAME] = category.matches(keywords)
        ordered_list = sorted(matches.keys(), key=lambda x: matches[x])
        if matches[ordered_list[0]] == matches[ordered_list[1]]:
            return 'Unknown'
        else:
            return ordered_list[0]
        # return max(CATEGORIES_SET, key=lambda cat: cat.matches(keywords)).NAME


class MedicalEmergency(Category):
    NAME = 'Medical Emergency'
    KEYWORDS = {'כואב', 'ראש', 'לב', 'בטן', 'הקיא', 'הקיאה', 'התעלף', 'התעלפה', 'משלשל', 'משלשלת', 'מתעלף', 'מקיא',
                'מקיאה', 'מתעלפת', 'התקף', 'נפל', 'נפלה', 'אמבולנס'}

class Fire(Category):
    NAME = 'Fire'
    KEYWORDS = {'אש', 'שריפה', 'בוער', 'נשרף', 'נשרפה', 'בוערת'}


class Kidnapping(Category):
    NAME = 'Kidnapping'
    KEYWORDS = {'חטיפה', 'חטפו', 'חטף', 'חטפה'}


class TerrorAttack(Category):
    NAME = 'Terror Attack'
    KEYWORDS = {'טרור', 'פיגוע', 'פיצוץ'}

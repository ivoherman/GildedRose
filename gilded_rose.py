# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Regular(Item):
    """Items which have no special traits"""

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        if self.sell_in < 0:
            self.quality -= 2
        elif self.quality < 1:
            self.quality = 0
        else:
            self.quality -= 1

        self.sell_in -= 1


class Ripening(Item):
    """Items which increase in quality"""

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        if self.quality >= 50:
            self.quality = 50
        elif self.sell_in < 1:
            self.quality += 2
        else:
            self.quality += 1

        self.sell_in -= 1


class BackstagePass(Item):
    """
    Items which increase in quality untill sell_in date expires
    """

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        if self.sell_in < 1:
            self.quality = 0
        elif self.sell_in < 6:
            self.quality += 3
        elif self.sell_in < 11:
            self.quality += 2
        else:
            self.quality += 1

        if self.quality >= 50:
            self.quality = 50

        self.sell_in -= 1


class Legendary(Item):
    """
    Items with static quality and sell_in date
    """

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        self.quality = 80


class Conjured(Item):
    """
    Items with a increased quality decrease"""
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        if self.sell_in < 1 :
            self.quality -= 4
        else:
            self.quality -= 2

        if self.quality < 1:
            self.quality = 0
    
        self.sell_in -= 1

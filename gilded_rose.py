# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """
        Update quality and sell_in for items
        """
        for item in self.items:
            item.update_quality()
            item.update_sell_in()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Regular(Item):
    """Base Items which have no special traits"""

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        """
        Method to update quality
        If sell_in <= 0 days -> quality decrease of 2
        If sell_in > 0 days -> quality decrease of 1
        Min quality = 0
        """
        if self.sell_in <= 0:
            self.quality -= 2
        else:
            self.quality -= 1

        if self.quality < 0:
            self.quality = 0

    def update_sell_in(self):
        """
        Method to update sell_in value
        """
        self.sell_in -= 1


class Ripening(Regular):
    """Items which increase in quality"""

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        """
        Method to update quality
        If sell_in <= 0 days -> quality increase of 2
        If sell_in > 0 days quality increase of 1
        Max quality = 50
        """
        if self.sell_in <= 0:
            self.quality += 2
        else:
            self.quality += 1

        if self.quality >= 50:
            self.quality = 50


class BackstagePass(Regular):
    """
    Items which increase in quality untill sell_in date expires
    """

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        """
        Method to update quality
        If sell_in < 1 days -> quality = 0
        If sell_in <= 5 days quality increase of 3
        If sell_in <= 10 days quality increase of 2
        Else quality increase of 1
        Max quality = 50
        """
        if self.sell_in < 1:
            self.quality = 0
        elif self.sell_in <= 5:
            self.quality += 3
        elif self.sell_in <= 10:
            self.quality += 2
        else:
            self.quality += 1

        if self.quality >= 50:
            self.quality = 50


class Legendary(Regular):
    """
    Items with static quality and sell_in date
    """

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        """
        Method to update quality
        Quality is a static value of 80
        """
        self.quality = 80

    def update_sell_in(self):
        """
        Method to update sell_in value
        Legendary items have a static sell_in value
        """


class Conjured(Regular):
    """
    Items with a doubled quality decrease
    """
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        """
        Method to update quality
        If sell_in <= 0 days -> quality decrease of 4
        If sell_in > 0 days -> quality decrease of 2
        Min quality = 0
        """
        if self.sell_in <= 0:
            self.quality -= 4
        else:
            self.quality -= 2

        if self.quality <= 0:
            self.quality = 0

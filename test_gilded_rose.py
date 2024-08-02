# -*- coding: utf-8 -*-
import unittest

from gilded_rose import (
    Item,
    Regular,
    Ripening,
    BackstagePass,
    Legendary,
    Conjured,
    GildedRose
)


class ItemTest(unittest.TestCase):
    def test_repr_func(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 80)
        self.assertEqual(repr(item), "Sulfuras, Hand of Ragnaros, 0, 80")


class RegularTest(unittest.TestCase):
    def test_decreasing_quality(self):
        self.items = [Regular("Elixir of the Mongoose", 10, 10)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        self.assertEqual(self.items[0].quality, 9)

    def test_quality_decreases_with_2_after_sellin_date(self):
        self.items = [Regular("Random", -1, 10)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        self.assertEqual(self.items[0].quality, 8)

    def test_quality_cannot_be_negative(self):
        self.items = [Regular("Elixir of the Mongoose", 8, 0)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        self.assertEqual(self.items[0].quality, 0)
    
    def test_sell_in_decrease(self):
        self.items = [Regular("Elixir of the Mongoose", 8, 0)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        self.assertEqual(self.items[0].sell_in, 7)


class RipeningTest(unittest.TestCase):
    def test_increasing_quality_before_sellin_date(self):
        self.items = [Ripening("Aged Brie", 10, 10)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        self.assertEqual(self.items[0].quality, 11)

    def test_increasing_quality_by_2_after_sellin_date(self):
        self.items = [Ripening("Aged Brie", 0, 10)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        self.assertEqual(self.items[0].quality, 12)

    def test_maximum_quality(self):
        self.items = [Ripening("Aged Brie", 0, 50)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        self.assertEqual(self.items[0].quality, 50)

    def test_sell_in_decrease(self):
        self.items = [Ripening("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        self.assertEqual(self.items[0].sell_in, 9)


class BackstagePassesTest(unittest.TestCase):
    def test_increasing_quality_with_sellin_higher_then_10(self):
        self.items = [BackstagePass("Backstage passes to a TAFKAL80ETC concert", 15, 10)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        self.assertEqual(self.items[0].quality, 11)

    def test_increasing_quality_with_sellin_between_10_and_5(self):
        self.items = [BackstagePass("Backstage passes to a TAFKAL80ETC concert", 10, 10)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        self.assertEqual(self.items[0].quality, 12)

    def test_increasing_quality_with_sellin_5_or_lower(self):
        self.items = [BackstagePass("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        self.assertEqual(self.items[0].quality, 13)

    def test_quality_0_when_sellin_0(self):
        self.items = [BackstagePass("Backstage passes to a TAFKAL80ETC concert", 0, 0)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        self.assertEqual(self.items[0].quality, 0)

    def test_quality_cannot_be_negative(self):
        self.items = [BackstagePass("Backstage passes to a TAFKAL80ETC concert", -1, 0)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        self.assertEqual(self.items[0].quality, 0)

    def test_quality_cannot_be_aabaove_50(self):
        self.items = [BackstagePass("Backstage passes to a TAFKAL80ETC concert", 5, 50)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        self.assertEqual(self.items[0].quality, 50)

    def test_sell_in_decrease(self):
        self.items = [BackstagePass("Backstage passes to a TAFKAL80ETC concert", 5, 50)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        self.assertEqual(self.items[0].sell_in, 4)


class LegendaryTest(unittest.TestCase):
    def test_quality_is_always_80(self):
        self.items = []
        self.items.append(Legendary("Sulfuras, Hand of Ragnaros", 10, 80))
        self.items.append(Legendary("Sulfuras, Hand of Ragnaros", 0, 80))
        self.items.append(Legendary("Sulfuras, Hand of Ragnaros", -1, 80))
        gilded_rose = GildedRose(self.items)

        gilded_rose.update_quality()

        for item in self.items:
            self.assertEqual(item.quality, 80)

    def test_sell_in_decrease(self):
        self.items = [Legendary("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        self.assertEqual(self.items[0].sell_in, 10)


class ConjuredTest(unittest.TestCase):
    def test_quality_decreases_with_2(self):
        self.items = [Conjured("Conjured", 10, 10)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        self.assertEqual(self.items[0].quality, 8)

    def test_quality_decreases_with_4_after_sellin_date(self):
        self.items = [Conjured("Conjured", 0, 10)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        self.assertEqual(self.items[0].quality, 6)

    def test_quality_cannot_be_negative(self):
        self.items = [Conjured("Conjured", 10, 0)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        self.assertEqual(self.items[0].quality, 0)

    def test_sell_in_does_not_change(self):
        self.items = [Conjured("Conjured", 10, 0)]
        gilded_rose = GildedRose(self.items)
        gilded_rose.update_quality()
        self.assertEqual(self.items[0].sell_in, 9)


if __name__ == '__main__':
    unittest.main()

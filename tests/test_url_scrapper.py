# coding: utf8

import unittest
from unittest import TestCase
from code.url_scrapper import Scrapper
from difflib import Differ
import unicodedata


class TestScrapper(TestCase):

    def test_get_data(self):
        scrapper = Scrapper(
            "https://gist.githubusercontent.com/jsdario/6d6c69398cb0c73111e49f1218960f79/raw/8d4fc4548d437e2a7203a5aeeace5477f598827d/el_quijote.txt")
        scrapper.get_data(11)
        assert(scrapper.data == "DON QUIJOTE")

    def test_get_data_no_param(self):
        scrapper = Scrapper(
            "https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt")
        scrapper.get_data()
        res = "ipurcbasefc for tbe Sltbrars of   be TUniverait? of {Toronto   out of tbe proceeds of tbe fun&   bequeatbefc bp     Stewart,   OB. A.D. 1892.      THE WORKS OF  HERMAN MELVILLE   STANDARD EDITION   VOLUME   VII     MOBY- DICK   OR, THE WHALE   BY   HERMAN MELVILLE     IN TWO VOLUMES  VOL. I     CONSTABLE AND COMPANY LTD   LONDON BOMBAY SYDNEY  1922     Ps     Printed in Great Britain by T. and A. CONSTABLE LTD  at the Edinburgh University Press     IN TOKEN   OF MY ADMIRATION FOB HIS GENIUS   THIS BOOK IS INSCRIBED   TO   NATHANIEL HAWTHORNE     CONTENTS   CHAP. PAGE   I. LOOMINGS . 1   II. THE CARPET-BAG ...... 8   III. THE SPOUTER-INN . . . . . . 13   IV. THE COUNTERPANE . . . . . 31  V. BREAKFAST ...... 36   VI. THE STREET . . . . . 39   VII. THE CHAPEL . . . . . . 42   VIII. THE PULPIT ....... 46   IX. THE SERMON ...... 49   X. A BOSOM FRIEND ...... 60   XI. NIGHTGOWN 65   XII. BIOGRAPHICAL ...... 68   XIII. WHEELBARROW . . . . . . 71   XIV. NANTUCKET ....... 77   XV. CHOWDER ....."
        assert(scrapper.data == res)

    def test_parse_data(self):
        scrapper = Scrapper(
            "https://gist.githubusercontent.com/jsdario/6d6c69398cb0c73111e49f1218960f79/raw/8d4fc4548d437e2a7203a5aeeace5477f598827d/el_quijote.txt")
        scrapper.get_data(11)
        scrapper.parse_data()
        res = {'QUIJOTE': 1, 'DON': 1}
        assert(scrapper.dictOfWords == res)


if __name__ == '__main__':
    unittest.main()

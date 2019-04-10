# -*- coding: utf-8 -*-
# © 2017 Diagram Software S.L.
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html


from .common import TestCommon


class TestProductSearch(TestCommon):

    def test_001_product_search_by_attr_value(self):
        gral_args = [('id', 'in', self.products_ids)]

        search_1 = self.ProductProduct.name_search(
            "16 GB", args=gral_args, operator='ilike', limit=100)
        self.assertEqual(len(search_1), 1)

        search_2 = self.ProductProduct.name_search(
            "32 GB", args=gral_args, operator='ilike', limit=100)
        self.assertEqual(len(search_2), 1)

        search_3 = self.ProductProduct.name_search(
            "GB", args=gral_args, operator='ilike', limit=100)
        self.assertEqual(len(search_3), 2)

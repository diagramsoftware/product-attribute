# -*- coding: utf-8 -*-
# © 2017 Diagram Software S.L.
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html


from openerp.tests import common


class TestCommon(common.SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(TestCommon, cls).setUpClass()

        cls.ProductProduct = cls.env["product.product"]

        cls.attribute_value_1 = cls.env.ref("product.product_attribute_value_1")
        cls.attribute_value_2 = cls.env.ref("product.product_attribute_value_2")

        cls.product_1 = cls.env.ref("product.product_product_4")
        cls.product_2 = cls.env.ref("product.product_product_4c")
        cls.products_ids = [cls.product_1.id, cls.product_2.id]

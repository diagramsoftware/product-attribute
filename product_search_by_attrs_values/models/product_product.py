# -*- coding: utf-8 -*-
# © 2017 Diagram Software S.L.
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html


from openerp import api, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        """ This method assumes attribute value is on display_name """
        attribute_values = self.env["product.attribute.value"].search([
            ('name', operator, name),
        ])
        products = self.search([
            ('attribute_value_ids', 'in', attribute_values.ids),
        ] + args)
        res = super(ProductProduct, self).name_search(
            name, args=args + [('id', 'not in', products.ids)],
            operator=operator, limit=limit)
        return res + products.name_get()

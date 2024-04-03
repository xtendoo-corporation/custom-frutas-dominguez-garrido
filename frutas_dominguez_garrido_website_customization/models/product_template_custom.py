# Copyright 2024 Xtendoo - Manuel Calero
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields

class ProductTemplateAttributeValue(models.Model):
    _inherit = 'product.template.attribute.value'
    _order = "sequence, name, id"

    sequence = fields.Integer(string="Sequence", readonly=True)

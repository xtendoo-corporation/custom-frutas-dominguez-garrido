# Copyright 2024 Xtendoo - Manuel Calero
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Website(models.Model):
    _inherit = "website"

    frutas_dominguez_garrido_website_price_default_message = fields.Char(
        string="Default Hidden price message",
        help="When the price is hidden on the website we can give the customer"
        "some tips on how to find it out.",
        translate=True,
    )


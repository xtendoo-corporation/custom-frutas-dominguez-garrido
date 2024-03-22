# Copyright 2024 Xtendoo - Manuel Calero
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    frutas_dominguez_garrido_website_price_default_message = fields.Char(
        related="website_id.frutas_dominguez_garrido_website_price_default_message",
        readonly=False,
    )

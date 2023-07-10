# Copyright 2015-TODAY ForgeFlow
# - Jordi Ballester Alomar
# Copyright 2015-TODAY Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import api, fields, models


class ResUsers(models.Model):

    _inherit = "res.users"

    brand_ids = fields.Many2many('product.brand', 'brand_user_rel', 'brand_id', 'user_id')
    categ_ids = fields.Many2many('product.category', 'categ_user_rel', 'categ_id', 'user_id')
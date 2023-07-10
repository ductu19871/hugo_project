# Copyright 2015-TODAY ForgeFlow
# - Jordi Ballester Alomar
# Copyright 2015-TODAY Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import api, fields, models


class ResUsers(models.Model):

    _inherit = "res.users"

    brand_ids = fields.Many2many('product.brand', 'brand_user_rel', 'brand_id', 'user_id', 'Brands')
    categ_ids = fields.Many2many('product.category', 'categ_user_rel', 'categ_id', 'user_id', 'Product Categories')
    warehouse_ids = fields.Many2many('stock.warehouse', 'warehouse_user_rel', 'warehouse_id', 'user_id', 'Warehouse')
    journal_ids = fields.Many2many('account.journal', 'journal_user_rel', 'journal_id', 'user_id', 'Journal')
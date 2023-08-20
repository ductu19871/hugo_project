from odoo import api, fields, models

class SO(models.Model):
    _inherit = 'sale.order'

    def _prepare_invoice(self):
        return super(SO, self.with_context(overwrite_user_warehouse_id = self.warehouse_id ))._prepare_invoice()
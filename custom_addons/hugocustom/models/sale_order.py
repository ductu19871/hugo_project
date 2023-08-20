from odoo import api, fields, models

class SO(models.Model):
    _inherit = 'sale.order'

    quotation_term = fields.Integer('Hiệu lực báo giá', default=30)
    add_state = fields.Selection([('send_request','Đã gửi yêu cầu xử lý'),
                                  ('confirmed', 'Xác nhận đơn hàng'),
                                  ('stocked', 'Đã xuất kho'),
                                  ('setup','Đang lắp đặt'),
                                  ('deliveried','Giao hàng thành công'),
                                  ('closed','Đơn hàng đã đóng'),
                                  ], string='Các trạng thái của đơn hàng')
    payment_method_id = fields.Many2one('account.payment.method', 'Phương thức thanh toán', domain="[('payment_type','=','inbound')]")
    def _prepare_invoice(self):
        return super(SO, self.with_context(overwrite_user_warehouse_id = self.warehouse_id ))._prepare_invoice()
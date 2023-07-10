from odoo import api, fields, models


class PP(models.Model):

    _inherit = "product.product"
    
    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        if not self.env.su and (self.user_has_groups('base.group_user') and not self.user_has_groups('base.group_system')):
        # if not self.env.su and (self.user_has_groups('base.group_user')):
            args += ['|', ('product_brand_id','=', False), ('product_brand_id','in',self.env.user.brand_ids.ids),
                     '|', ('categ_id','=', False), ('categ_id','child_of', self.env.user.categ_ids.ids),
                     ]
        return super(PP, self)._search(args, offset, limit, order, count=count, access_rights_uid=access_rights_uid)
    
    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        if not self.env.su and (self.user_has_groups('base.group_user') and not self.user_has_groups('base.group_system')):
        # if not self.env.su and (self.user_has_groups('base.group_user')):
            domain += ['|', ('product_brand_id','=', False), ('product_brand_id','in',self.env.user.brand_ids.ids),
                     '|', ('categ_id','=', False), ('categ_id','child_of', self.env.user.categ_ids.ids),
                     ]
        return super(PP, self).read_group(domain, fields, groupby, offset=offset, limit=limit, orderby=orderby, lazy=lazy)

class PT(models.Model):
    _inherit = "product.template"

    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        if not self.env.su and (self.user_has_groups('base.group_user') and not self.user_has_groups('base.group_system')):
        # if not self.env.su and (self.user_has_groups('base.group_user')):
            args += ['|', ('product_brand_id','=', False), ('product_brand_id','in',self.env.user.brand_ids.ids),
                     '|', ('categ_id','=', False), ('categ_id','child_of', self.env.user.categ_ids.ids),
                     ]
        return super(PT, self)._search(args, offset, limit, order, count=count, access_rights_uid=access_rights_uid)
    
    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        if not self.env.su and (self.user_has_groups('base.group_user') and not self.user_has_groups('base.group_system')):
        # if not self.env.su and (self.user_has_groups('base.group_user')):
            domain += ['|', ('product_brand_id','=', False), ('product_brand_id','in',self.env.user.brand_ids.ids),
                     '|', ('categ_id','=', False), ('categ_id','child_of', self.env.user.categ_ids.ids),
                     ]
        return super(PT, self).read_group(domain, fields, groupby, offset=offset, limit=limit, orderby=orderby, lazy=lazy)
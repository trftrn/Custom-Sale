from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.tools import config


class CustomerSalesPartner(models.Model):
    _inherit = 'res.partner'

    is_vvip_customer = fields.Boolean(
        string='Customer Vvip',
        required=False
    )
    customer_vvip_ids = fields.One2many(
        comodel_name='vvip.customer',
        inverse_name='customer_id',
        string='customer vvip id',
        required=False
    )
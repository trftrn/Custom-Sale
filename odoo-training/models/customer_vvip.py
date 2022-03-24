from odoo import models, fields, api

class CustomerVvip(models.Model):
    _name = 'vvip.customer'
    _description = 'VVIP CUSTOMER'

    name = fields.Char(
        string='Customer Name',
        required=False
    )
    phone = fields.Char(
        string='Phone Number',
        required=False
    )
    email = fields.Char(
        string='Email',
        required=False
    )
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'), ('female', 'Female')]
    )
    food_favorite = fields.Char(
        string='Foods Favorite',
        required=False
    )
    drink_favorite = fields.Char(
        string='Drinks Favorite',
        required=False
    )
    interest_data = fields.Char(
        string='Interest Data',
        required=False
    )


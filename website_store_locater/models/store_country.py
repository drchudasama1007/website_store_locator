from odoo import api, fields, models, _

class StoreCountry(models.Model):
    _name = "store.country"

    name = fields.Char("Name")
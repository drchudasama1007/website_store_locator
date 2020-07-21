from odoo import api, fields, models, _


class StoreLocation(models.Model):
    _name = "store.location"

    name = fields.Char("Name")
    city = fields.Char("City")
    store_country_id = fields.Many2one("store.country", string="Store Place")
    phone = fields.Char("Phone")
    lat = fields.Char("Latitude")
    long = fields.Char("Longitude")
    markers_id = fields.Integer("Marker Id")

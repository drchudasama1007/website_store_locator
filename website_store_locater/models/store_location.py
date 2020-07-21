from odoo import api, fields, models, _


class StoreLocation(models.Model):
    _name = "store.location"


    name = fields.Many2one("res.users", string="Name")
    address = fields.Char("Address")
    street = fields.Char("State")
    street2 = fields.Char("State2")
    city = fields.Char("City")
    state_id = fields.Many2one("res.country.state", string="Country")
    zip = fields.Char("Zip")
    area = fields.Text("Area")
    lat = fields.Char("Latitude")
    long = fields.Char("Longitude")
    store_id =fields.Many2one('store.store', string='Store Id')
    store_image = fields.Binary("Store Image")
    markers_id = fields.Integer("Marker Id")


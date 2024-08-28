from odoo import _, api, fields, models

class ThorpeBase(models.Model):
    _name = 'thorpe.base'
    _description = 'Infraestruct Orchestrator conection'

    #Model Fields
    name = fields.Char(string="Name", required=True)
    region = fields.Char(string="Region", required=True)
    url = fields.Char(string="Url Api", required=True)
    token = fields.Char(string="Token Api", required=True)
    secret = fields.Char(string="Secret Token", required=True)
    expiration = fields.Date(string="Expiration", required=True)
    latitude = fields.Float(string="Latitude", required=True)
    longitude = fields.Float(string="Longitude", required=True)
    comments = fields.Text(string="Comments", required=False, translate=True)

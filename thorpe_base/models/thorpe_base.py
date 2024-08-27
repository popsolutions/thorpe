# Copyright 2024 Marcos Mendez / PopSolutions.co
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class ThorpeBase(models.Model):
    _name = 'thorpe.base'
    _description = 'Odoo Hypervisor Orchestrator'

    #Model Fields
    name = fields.Char(string="Name", required=True)
    public_ip = fields.Char(string="Public Api", required=True)
    region = fields.Char(string="Region", required=True)
    url = fields.Char(string="Url Api", required=True)
    token = fields.Char(string="Token Api", required=True)
    secret = fields.Char(string="Secret Token", required=True)    
    latitude = fields.Float(string="Latitude", required=True)
    longitude = fields.Float(string="Longitude", required=True)
    comments = fields.Text(string="Comments", required=False, translate=True)

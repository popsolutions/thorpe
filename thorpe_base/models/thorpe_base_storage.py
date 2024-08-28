from odoo import _, api, fields, models

class ThorpeBaseStorage(models.Model):
    _name = 'thorpe.base.storage'
    _description = 'Storage of node selected'
    
    name = fields.Char(string="Name", required=True)
    node_id = fields.Many2one("thorpe.base.node", string="node", required=True)
    selected_to_images = fields.Boolean(string="Active to use", default=False, required=True)
    used_fraction = fields.Char(string="Fraction Used", required=True)

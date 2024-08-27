# Copyright 2024 Marcos Mendez / PopSolutions.co
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class ThorpeBaseNode(models.Model):
    _name = 'thorpe.base.node.storage'
    _description = 'Storage of node selected'
    
    name = fields.Char(string="Name", required=True)
    node_id = fields.Many2one("thorpe.base.node", string="node", required=True)
    selected_to_images = fields.Boolean(string="Select to Images", default=False, required=True)
    used_fraction = fields.Char(string="Fractuion Used", required=True)

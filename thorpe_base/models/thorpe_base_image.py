# Copyright 2024 Marcos Mendez / PopSolutions.co
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class ThorpeBaseImage(models.Model):
    _name = 'thorpe.base.image'
    _description = 'Images from nodes'
 
    name = fields.Char(string="Name", required=True)
    node_id = fields.Many2one("thorpe.base.node", string="node", required=True)
    storage_id = fields.Many2one("thorpe.base.node.storage", string="storage", required=True)
    content = fields.Char(string="Content", required=True)

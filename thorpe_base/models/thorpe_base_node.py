# Copyright 2024 Marcos Mendez / PopSolutions.co
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class ThorpeBaseNode(models.Model):
    _name = 'thorpe.base.node'
    _description = 'Nodes of pve selected'
    
    name = fields.Char(string="Name", required=True)
    pve_id = fields.Many2one("thorpe.base", string="pve", required=True)
    selected_to_sales = fields.Boolean(string="Select to Sales", required=True, default=False)
    status = fields.Char(string="status", required=True)

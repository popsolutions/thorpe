# Copyright 2024 Marcos Mendez / PopSolutions.co
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class ThorpeBase(models.Model):
    _name = 'thorpe.base'
    _description = 'Odoo Hypervisor Orchestrator'

    #Model Fields
    name = fields.Char("Name")

import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        # Call the original method
        super(SaleOrder, self).action_confirm()

        # Custom logic to be executed when a sales order is confirmed
        for order in self:
            # Your custom logic here
            # For example, you can send a notification, update some fields, etc.
            _logger.info("FUNCIONOU!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

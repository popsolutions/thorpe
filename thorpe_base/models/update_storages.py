import logging
import json
from odoo import models, api
from . import thorpe_request

_logger = logging.getLogger(__name__)                                                                                        

class UpdateStorage(models.Model):
    _name = 'thorpe.update.storage'
    _description = 'methodos to update storage models'

    @api.model
    def update_storages(self):
        # Consulta para obter todos os Nodes
        _logger.info("-----------------------------------------------------")
        _logger.info("atualiza_storages_com_node")
        nodes = self.env['thorpe.base.node'].search([('selected_to_sales', '=', True)])
        providers = self.env['thorpe.base'].search([])
        provider = providers[0]
        for node in nodes:
            try:                
                request = thorpe_request.ThorpeRequest()
                url = f"/nodes/{node.name}/storage"

                response = request.make_request(provider, url, 'GET', None)
                _logger.info(f"response: {response.text}")
                data = response.json()
                storage_list = data.get('data')
                for item in storage_list:
                    storage = item.get('storage')
                    used_fraction = item.get('used_fraction')

                    storage_record = self.env['thorpe.base.storage'].search([('name', '=', storage)], limit=1)

                    if not storage_record:
                        storage_record = self.env['thorpe.base.storage'].create({
                            'name': storage,
                            'node_id': node.id,
                            'used_fraction': used_fraction
                        })

                    storage_record.write({
                        'node_id': node.id,
                        'used_fraction': used_fraction,
                    })
            except Exception as e:
                _logger.error("Erro ao processar nó do provedor %s: %s" % (nodes.name, str(e)))

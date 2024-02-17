import logging
import json
from odoo import models, api
from . import thorpe_request

_logger = logging.getLogger(__name__)                                                                                        

class ThorpeBaseUpdateNode(models.Model):
    _name = 'thorpe.base.update.node'

    @api.model
    def atualiza_node_com_pve(self):
        # Consulta para obter todos os Nodes
        _logger.info("-----------------------------------------------------")
        _logger.info("atualiza_node_com_pve")
        providers = self.env['thorpe.base.cluster'].search([])
        for provider in providers:
            try:
                request = thorpe_request.ThorpeRequest()
                response = request.make_request(provider, '/nodes', 'GET', None)
                data = response.json()
                node_list = data.get('data')
                for item in node_list:
                    node_name = item.get('node')
                    status = item.get('status')
                    node_record = self.env['thorpe.base.node'].search([('name', '=', node_name), ('pve_id', '=', provider.id)], limit=1)

                    if not node_record:
                        node_record = self.env['thorpe.base.node'].create({
                            'name': node_name,
                            'pve_id': provider.id,
                            'status': status
                        })

                    node_record.write({
                        'status': status,
                    })
            except Exception as e:
                _logger.error("Erro ao processar nó do provedor %s: %s" % (provider.name, str(e)))

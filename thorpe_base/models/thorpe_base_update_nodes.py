import logging
import json
from odoo import models, api
from . import thorpe_request

_logger = logging.getLogger(__name__)                                                                                        

class ThorpeBaseUpdateNodes(models.Model):
    _name = 'thorpe.base.update.nodes'

    @api.model
    def atualiza_node_com_pve(self):
        # Consulta para obter todos os Nodes
        _logger.info("-----------------------------------------------------")
        _logger.info("atualiza_node_com_pve")
        providers = self.env['thorpe.base'].search([])
        for provider in providers:
            try:
                request = thorpe_request.ThorpeRequest()
                response = request.make_request(provider, '/nodes', 'GET', None)
                data = response.json()
                node_list = data.get('data')
                for item in node_list:
                    node_name = item.get('node')
                    status = item.get('status')

                    node_record = self.env['thorpe.base.node'].search([('name', '=', node_name)], limit=1)

                    if not node_record:
                        node_record = self.env['thorpe.base.node'].create({
                            'name': node_name,
                            'pv_id': provider.id,
                            'status': status
                        })

                    node_record.write({
                        'pv_id': provider.id,
                        'status': status,
                    })
            except Exception as e:
                _logger.error("Erro ao processar nó do provedor %s: %s" % (provider.name, str(e)))

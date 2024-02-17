import logging
import json
from odoo import models, api
from . import thorpe_request

_logger = logging.getLogger(__name__)                                                                                        

class ThorpeBaseUpdateImage(models.Model):
    _name = 'thorpe.base.update.image'

    @api.model
    def atualiza_images(self):
        _logger.info("-----------------------------------------------------")
        _logger.info("atualiza_images")
        storages = self.env['thorpe.base.storage'].search([('selected_to_images', '=', True)])
        providers = self.env['thorpe.base.cluster'].search([])
        provider = providers[0]
        for storage in storages:
            try:            
                node = self.env['thorpe.base.node'].search([('id', '=', storage.node_id.id)])
                request = thorpe_request.ThorpeRequest()
                url = f"/nodes/{node.name}/storage/{storage.name}/content"

                response = request.make_request(provider, url, 'GET', None)
                data = response.json()
                storage_list = data.get('data')
                for item in storage_list:
                    name = item.get('volid')
                    content = item.get('content')

                    record = self.env['thorpe.base.image'].search([('name', '=', name), ('node_id', '=', node.id), ('storage_id', '=', storage.id)])

                    if not record:
                        record = self.env['thorpe.base.image'].create({
                            'name': name,
                            'node_id': node.id,
                            'storage_id': storage.id,
                            'content': content,
                        })

            except Exception as e:
                _logger.error("Erro ao processar nó do provedor %s: %s" % (node.name, str(e)))

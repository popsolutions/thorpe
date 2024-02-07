import logging                                                                                                               
import requests                                                                                                              
from odoo import models, api, fields, _                                                                                  
from dataclasses import dataclass                                                                                            
                                                                                                                             
_logger = logging.getLogger(__name__)                                                                                        
                                                                                                                             
class SaleOrder(models.Model):                                                                                               
    _inherit = 'sale.order'                                                                                                  
                                                                                                                             
    def action_confirm(self):                                                                                                
        # Call the original method                                                                                           
        super(SaleOrder, self).action_confirm()                                                                              
                                                                                                                             
        # Custom logic to be executed when a sales order is confirmed                                                        
        for order in self:
            self.next_vmid()
            sucesso, mensagem = self.next_vmid()
            if sucesso:
                _logger.info(mensagem)
            else:
                _logger.info(mensagem)
            # Your custom logic here                                                                                         
            # For example, you can send a notification, update some fields, etc.                                             
            _logger.info("FUNCIONOU!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
       
    def next_vmid(self):
        base_url = 'https://10.10.1.2:8006/api2/json'
        url = f"{base_url}/cluster/nextid"        
        token_id = "bot-admin@pve!maglev"                                                                
        token_secret = "b57b4570-c4ec-4846-a7e4-2418a4e052e7"                                                            
        pve_api_token = f"{token_id}={token_secret}"

        # Cabeçalhos da solicitação
        headers = {
            'Authorization': f'PVEAPIToken={pve_api_token}'
        }
            
        _logger.info("-----------------------------------------------------")
        _logger.info("next vmid")
        _logger.info("-----------------------------------------------------")
        
        try:
            # Realizando a solicitação
            response = requests.post(url, headers=headers)

            # Verificando a resposta
            if response.status_code == 200:
                return True, "A VM foi iniciada com sucesso!"
            else:
                return False, f"Erro ao iniciar a VM: {response.text}"
        except Exception as e:
            return False, f"Erro ao iniciar a VM: {str(e)}"

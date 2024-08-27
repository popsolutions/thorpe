import logging
import requests
import json
from dataclasses import dataclass, asdict

_logger = logging.getLogger(__name__)                                                                                        

class ThorpeRequest():                                                                                               
    _name = 'thorpe.request'

    def show_log(self, msg):
        _logger.info("-----------------------------------------------------")
        _logger.info(f"{msg}")

    def make_request(self, pve, url_request, method, body=None):
        _logger.info(f"PVE: {pve.name} -> {pve.url}")
        base_url = pve.url
        token_id = pve.token
        token_secret = pve.secret
        pve_api_token = f"{token_id}={token_secret}"

        # Cabeçalhos da solicitação
        headers = {
            'Authorization': f'PVEAPIToken={pve_api_token}',
            'Content-Type': 'application/json'
        }
        url = f"{base_url}{url_request}"
        
        if method.upper() == 'GET':
            self.show_log("Request GET")
            self.show_log(url)
            response = requests.get(url, headers=headers, verify=False)
        elif method.upper() == 'POST':
            self.show_log("Request POST")
            self.show_log(url)
            self.show_log(body)
            response = requests.post(url, headers=headers, data=body, verify=False)
        elif method.upper() == 'PUT':
            self.show_log("Request PUT")
            self.show_log(url)
            response = requests.put(url, headers=headers, json=body, verify=False)
        elif method.upper() == 'DELETE':
            self.show_log("Request DELETE")
            self.show_log(url)
            response = requests.delete(url, headers=headers, verify=False)
        else:
            raise ValueError("Método HTTP inválido. Escolha entre 'GET', 'POST', 'PUT' ou 'DELETE'.")

        return response
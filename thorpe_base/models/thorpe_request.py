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

    def get_request(self, url, headers):
        try:
            self.show_log("Request GET")
            self.show_log(url)
            response = requests.get(url, headers=headers, verify=True)
            return response
        except Exception as e:
            self.show_log(f"Error to GET request: {str(e)}")

    def post_request(self, url, headers, body):
        try:
            self.show_log("Request POST")
            self.show_log(url)
            self.show_log(body)
            response = requests.post(url, headers=headers, data=body, verify=True)
        except Exception as e:
            self.show_log(f"Error to POST request: {str(e)}")

    def put_request(self, url, headers, body):
        try:
            self.show_log("Request PUT")
            self.show_log(url)
            self.show_log(body)
            response = requests.put(url, headers=headers, json=body, verify=True)
        except Exception as e:
            self.show_log(f"Error to PUT request: {str(e)}")

    def delete_request(self, url, headers):
        try:
            self.show_log("Request DELETE")
            self.show_log(url)
            response = requests.delete(url, headers=headers, verify=True)
            return response
        except Exception as e:
            self.show_log(f"Error to DELETE request: {str(e)}")


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
            return self.get_request(url, headers=headers)
        elif method.upper() == 'POST':
            return self.post_request(url, headers=headers, body=body)
        elif method.upper() == 'PUT':
            return self.put_request(url, headers=headers, body=body)
        elif method.upper() == 'DELETE':
            return self.delete_request(url, headers=headers)
        else:
            raise ValueError("Método HTTP inválido. Escolha entre 'GET', 'POST', 'PUT' ou 'DELETE'.")

        return response

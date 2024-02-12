import logging
import requests
import json
from odoo import models, api, fields, _
from dataclasses import dataclass, asdict

_logger = logging.getLogger(__name__)                                                                                        


@dataclass
class LxcConfig:
    hostname: str
    space: int
    password: str
    vmid: str
    memory: int
    core: int
    product_name: str

@dataclass
class LxcPayload:
    ostemplate: str
    vmid: str
    hostname: str
    password: str
    memory: str
    rootfs: str
    cores: str
    swap: str
    net0: str
    start: bool
    tags: str


class SaleOrder(models.Model):                                                                                               
    _inherit = 'sale.order'

    def action_confirm(self):                                                                                                
        # Call the original method                                                                                           
        super(SaleOrder, self).action_confirm()                                                                              

        for order in self:
            self.create_lxc()

    def show_log(self, msg):
        _logger.info("-----------------------------------------------------")
        _logger.info(f"{msg}")
        _logger.info("-----------------------------------------------------")

    def make_request(self, url_request, method, body=None):
        base_url = 'https://10.10.1.2:8006/api2/json'

        token_id = "bot-admin@pve!maglev"
        token_secret = "b57b4570-c4ec-4846-a7e4-2418a4e052e7"
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
            response = requests.put(url, headers=headers, data=body, verify=False)
        elif method.upper() == 'DELETE':
            self.show_log("Request DELETE")
            self.show_log(url)
            response = requests.delete(url, headers=headers, verify=False)
        else:
            raise ValueError("Método HTTP inválido. Escolha entre 'GET', 'POST', 'PUT' ou 'DELETE'.")

        return response

    def next_vmid(self):
        self.show_log("next vmid")
        try:
            url = f"/cluster/nextid"
            response = self.make_request(url, 'GET')

            # Verificando a resposta
            if response.status_code == 200:
                data = response.json()
                data_value = data.get('data')
                
                return True, data_value
            else:
                return False, response.text
        except Exception as e:
            return False, f"Erro ao pegar proximo id: {str(e)}"

    def create_lxc(self):
        self.show_log("create lxc")
        try:
            self.next_vmid()
            sucesso, res = self.next_vmid()
            if sucesso:                
                self.show_log(res)
                self.show_log("config lxc")
                configs = LxcConfig(
                    hostname="my-container",
                    space=6,
                    password="secretpassword",
                    vmid=res,
                    memory=512,
                    core=2,
                    product_name="myproduct"
                )

                self.show_log("payload lxc")
                lxc_payload = self.config_lxc(configs)


                node = "data"
                url = f"/nodes/data/lxc"
                response = self.make_request(url, 'POST', lxc_payload)
                
                self.show_log(response.text)
                if response.status_code == 200:
                    self.show_log(f"sucesso para criar lxc: {response.text}")
                    return response.text
                else:
                    self.show_log(f"erro para criar lxc")
                    self.show_log(response)
                    return response.text
            else:
                self.show_log(res)  
     
        except Exception as e:
            self.show_log(f"Erro ao tentar criar lxc: {str(e)}")
            return False, f"Erro ao tentar criar lxc: {str(e)}"

    def config_lxc(self, configs: LxcConfig) -> LxcPayload:
        net0 = "name=eth0,bridge=vmbr0,firewall=1,ip=10.10.1.20/24,gw=10.10.1.1,ip6=dhcp"
        rootfs = f"local-lvm:{configs.space}"
        cores = str(configs.core)
        memory = str(configs.memory)
        tags = f"thorpe-lxc,{configs.product_name}"

        payload = LxcPayload(
            ostemplate="local:vztmpl/debian-11-standard_11.7-1_amd64.tar.zst",
            vmid=configs.vmid,
            hostname=configs.hostname,
            password=configs.password,
            memory=memory,
            rootfs=rootfs,
            cores=cores,
            swap="0",
            net0=net0,
            start=False,
            tags=tags
        )

        lxc_dict = asdict(payload)

        lxc_payload = json.dumps(lxc_dict)
        return lxc_payload
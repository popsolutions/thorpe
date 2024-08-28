# Setup config in proxmox

Downdload this project in connect node in proxmox and execute `./setup.sh` script.

## Output

```bash
Setup config in proxmox \n
Create group thorpe \n
Create user thorpe_access@pve
Add to thorpe groupe user thorpe_access@pve
Create and config api token
┌──────────────┬──────────────────────────────────────────────────────────
│ key          │ value                                                    
╞══════════════╪══════════════════════════════════════════════════════════
│ full-tokenid │ thorpe_access@pve!thorpe_api_token                       
├──────────────┼──────────────────────────────────────────────────────────
│ info         │ {"comment":"Token to acess by thorpe integration","privse
├──────────────┼──────────────────────────────────────────────────────────
│ value        │ 219cd33f-fc7a-4cb8-b94e-32d4a4df99de
└──────────────┴──────────────────────────────────────────────────────────
Add permitions to api token \n
Add permitions to vms
Add permitions to storage
Add permitions to nodes
Add permitions to group user \n
```

The config of api token is finish, copy `full-tokenid` to `Token` in thorpe-base and `value` to  `Secret` in thorpe-base


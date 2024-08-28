echo "Add permitions to api token \n"

echo "Add permitions to vms"
pveum aclmod /vms -token thorpe_access@pve!thorpe_api_token -role Thorpe.instance

echo "Add permitions to storage"
pveum aclmod /store/local-lvm -token thorpe_access@pve!thorpe_api_token -role Thorpe.storage
pveum aclmod /store/local -token thorpe_access@pve!thorpe_api_token -role Thorpe.storage
pveum aclmod /store -token thorpe_access@pve!thorpe_api_token -role Thorpe.storage
pveum aclmod /store -token thorpe_access@pve!thorpe_api_token -role Thorpe.template

echo "Add permitions to nodes"
pveum aclmod /nodes -token thorpe_access@pve!thorpe_api_token -role Thorpe.nodes


echo "Add permitions to group user \n"
pveum aclmod /storage/local-lvm -group thorpe -role Thorpe.storage
pveum aclmod /storage/local -group thorpe -role Thorpe.storage



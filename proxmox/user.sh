
echo "Create group thorpe \n"
pveum groupadd thorpe -comment "Goup to manager thorpe access"

echo "Create user thorpe_access@pve"
pveum useradd thorpe_access@pve -comment "User to thorpe config"

echo "Add to thorpe groupe user thorpe_access@pve"
pveum usermod thorpe_access@pve -group thorpe

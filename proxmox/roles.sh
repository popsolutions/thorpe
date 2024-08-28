# create Role to manager lxc and vms
#
pveum role add Thorpe.instance --privs "Datastore.Audit VM.Allocate VM.Audit VM.Config.CDROM VM.Config.Disk VM.Migrate VM.Monitor VM.PowerMgmt"

# create Role to list nodes
#
pveum role add Thorpe.nodes --privs "Sys.Audit"

# create Role to manger storage
#
pveum role add Thorpe.storage --privs "Datastore.Allocate Datastore.AllocateSpace Datastore.Audit VM.Audit"

# create Role to list templates lxc and vms
#
pveum role add Thorpe.template --privs "VM.Audit"

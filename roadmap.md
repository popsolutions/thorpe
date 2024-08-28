MODULO PARA GERENCIAR O MENU E AS CONFIGURAÇÔES

 Nome: thorpe-base
 Descrição: Adicionar 1 ou mais PVE Cluster nos Banco, configurar usuário e token de acesso ele irá usar as configurações de thorpe-products para criar thorpe-machines

MODULO PARA GERENCIAR PRODUTOS PADRÃO

 Nome: thorpe-products
 Descrição: Irá listar produtos base/template para poder adicionar no e-commerce com alguns valores padrões (Node para fazer o deployment, Rede Disponível, LXC ou VM | Número de CPUs(lxc) ou CPUS + Sockets(vm) + Discos + Imagens disponívels (Tkl-odoo, tkl-wordpres, tkl-debian, debin, ubuntu etc)
 
MODULO PARA GERENCIAR MAQUINAS/CONTAINERS

 Nome: thorpe-machine
 Descrição: Irá listar as maquinas já disponíveis e os usuários vinculados a elas, irá disponibilizar valores estáticos de status da maquina, nº de CPUs ativos atualmente, RAM Disponível e Uso de Disco
 
MODULO PARA GERENCIAR PERMISSÕES DE ACESSO AS MAQUINAS

 Nome: thorpe-users
 Descrição: irá vincular res.partners a faturas e thorpe-machines ativas 
 

---------------------------------------------------------------

##thorpe-base##
	MENU CONFIGURAÇÃO
	
	--PVE CLUSTER
    ----PVE AUTH
    ----PVE NODES
    ----PVE MACHINES (vm ou lxc)

##thorpe-machines## 

Estrutura:
	type(lxc/vm):       #Herado do thorpe-base
	domain:             #input do usuário na loja
	cores:              #input do usuário na loja
	mem:                #input do usuário na loja
	disk:               #input do usuário na loja
	image:              #input do usuário na loja
	!owner:             #herdado do res.partner/e-commerce-sale

##thorpe-users one-to-many (Odoo nativo)
	model(owner:machine) será equivalente a:
	res.partner:thorpe.machine
	
##thorpe-products
    pve.node: 
    pve.network
    pve.machine (lxc ou vm)

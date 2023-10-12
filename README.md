# Name

Automation of warewulf4 configuration and other services on an operating system.
**WIP**

# Goals

Prepare everything to be able to deploy Compute nodes with ww4.

* **dnsmask**: dns ready
* **tftp**: get it ready
* **ww4**:
    * general configure
    * nodes
    * get container
    * prepare container (ssh key, munge key, slurm, etc...)
* **firewalld**: permit dns and dhcp request

# User Settings

NOT YET USED 

Example:
```yaml
# WARNING: INCORRET PARAMATERS WILL LEAD TO BAD VM CONFIGURATION
# Dont change the section name
```

# Usage

```
git clone https://github.com/aginies/autoww4
cd autoww4/src
python3 -m autoww4
```

# Functions

[tftp.py](src/autoww4/tftp.py)
```
tftp_directory(directory)
tftp_option(options)
tftp_enable()
tftp_start()
```

[dhcpd.py](src/autoww4/dhcpd.py)
```
dhcpd_interface(interface)
set_authoritative(value)
```

[dnsmasq.py](src/autoww4/dnsmasq.py)
```
restart_dnsmask()
start_dnsmask()
enable_dnsmask()
dnsmasq_conf(config)
dnsmasq_host_conf(config)
dnsmasq_resolv_conf(config)
dnsmasq_test()
```

[ww4.py](src/autoww4/ww4.py)
```
ww4_start()
ww4_restart()
ww4_enable()
import_container(container)
ww4_nodes_conf(config)
ww4_warewulf_conf(config)
prepare_container(container)
container_set_default(container)
```

[util.py](src/autoww4/util.py)
```
Various utils functions
```

[containers.py](src/autoww4/containers.py)
```
This file contains the base_url and list of product per familly (SUSE, openSUSE, ubuntu...)
```

# Code

[Source](https://github.com/aginies/autoww4)

[Issues](https://github.com/aginies/autoww4/issues)

# Authors

Written by Antoine Ginies

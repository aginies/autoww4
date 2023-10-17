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

config are stored in [configuration](src/autow4/configuration.py) for now,
will be in [autoww4.yaml](src/autoww4.yaml) in the futur
```
git clone https://github.com/aginies/autoww4
cd autoww4/src
python3 -m autoww4
auto
```

# Functions

[auto.py](src/autoww4/auto.py)
```
def doall():
```
[cmd.py](src/autoww4/cmd.py)
```
```
[configuration.py](src/autoww4/configuration.py)
```
def find_file_dir(name, what):
def check_conffile(conf):
def find_conffile():
```
[dhcpd.py](src/autoww4/dhcpd.py)
```
def dhcpd_interface(interface):
def set_authoritative(value):
```
[dnsmasq.py](src/autoww4/dnsmasq.py)
```
def restart_dnsmasq():
def start_dnsmasq():
def enable_dnsmasq():
def dnsmasq_config(config, interface):
def add_node(node, ipaddr):
def dnsmasq_resolv_conf(config):
def dnsmasq_test():
```
[__init__.py](src/autoww4/__init__.py)
```
```
[__main__.py](src/autoww4/__main__.py)
```
```
[main.py](src/autoww4/main.py)
```
def main():
```
[tftp.py](src/autoww4/tftp.py)
```
def tftp_directory(directory):
def tftp_option(options):
def tftp_enable():
def tftp_start():
def tftp_restart():
```
[util.py](src/autoww4/util.py)
```
def run_command(cmd):
def run_command_with_except(cmd):
def systemd_start(service):
def systemd_restart(service):
def systemd_enable(service):
def cmd_exists(cmd):
def get_network_interface():
def list_containers_registry(familly):
def change_var(conffile, var_to_change, var_value, equal="="):
def esc(color):
def print_error(text):
def print_warning(text):
def print_ok(text):
def print_info(text):
def print_summary(text):
def print_title(text):
def print_summary_ok(text):
def print_command(text):
def print_data(data, value):
def validate_yaml_file(file_path):
def backup_file(file):
def check_iam_root():
def find_ext_file(ext):
def extract_subnet_range(config):
def get_ip_address(interface):
def create_if_not_exist(file):
```
[ww4.py](src/autoww4/ww4.py)
```
def ww4_start():
def ww4_restart():
def ww4_enable():
def import_container(familly, product):
def ww4_nodes_conf(config):
def ww4_warewulf_conf(config):
def add_node(node, ipaddr):
def containers_available():
def prepare_container(container):
def container_set_default(container, node):
def create_nodes_list():
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

# Authors: Antoine Ginies <aginies@suse.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
dnsmasq
"""

import autoww4.util as util
import autoww4.configuration as conf

def restart_dnsmasq():
    """
    restart dnsmasq service
    """
    util.print_info("Re-Starting dnsmasq")
    util.systemd_restart("dnsmasq")

def start_dnsmasq():
    """
    start dnsmasq
    """
    util.print_info("Starting dnsmasq")
    util.systemd_start("dnsmasq")

def enable_dnsmasq():
    """
    enable dnsmasq
    """
    util.print_info("Enabling dnsmasq")
    util.systemd_enable("dnsmasq")

def dnsmasq_config(config, interface):
    """
    configure dnsmasq
    """
    # do backup
    # various config
    util.print_info(f"dnsmasq {config}")
    util.backup_file(config)
    ipaddr = util.get_ip_address(interface)
    util.change_var(config, "interface", interface)
    util.change_var(config, "address", "/"+conf.dnsmasq_domain+"/127.0.0.1")
    util.change_var(config, "address", "/"+conf.dnsmasq_domain+"/"+ipaddr)
    util.change_var(config, "resolv-file", conf.dnsmasq_resolv)
    util.change_var(config, "addn-hosts", conf.dnsmasq_hosts)
    util.change_var(config, "server", ipaddr)
    util.change_var(config, "domain", conf.dnsmasq_domain)

def add_node(node, ipaddr):
    """
    add node in dnsmasq hosts conf
    """
    util.print_info(f"host {conf.dnsmasq_hosts}")
    with open(conf.dnsmasq_hosts, "w") as file:
        file.write(ipaddr+" "+node)
    file.close()

def dnsmasq_resolv_conf(config):
    """
    dnsmasq resolv config
    """
    util.print_info(f"resolv {config}")
    util.change_var(conf.dnsmasq_resolv, "nameserver", "127.0.0.1")

def dnsmasq_test():
    """
    check conf is ok
    """
    util.print_info("Testing dnsmasq configuration")
    util.run_command_with_except(conf.dnsmasq+" --test")

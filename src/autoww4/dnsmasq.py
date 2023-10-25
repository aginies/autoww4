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

class Dnsmasq():
    """
    manage dnsmasq config
    """

    def dnsmasq_config(self, config, interface):
        """
        configure dnsmasq
        """
        # do backup
        # various config
        util.print_info(f"dnsmasq {config}")
        util.create_if_not_exist(config)
        util.backup_file(config)
        ipaddr = util.get_ip_address(interface)
        print(ipaddr)
        util.change_var(config, "interface", interface)
        util.change_var(config, "address", "/"+self.dnsmasq_domain+"/127.0.0.1")
        util.change_var(config, "address", "/"+self.dnsmasq_domain+"/"+ipaddr)
        util.change_var(config, "resolv-file", self.dnsmasq_resolv)
        util.create_if_not_exist(self.dnsmasq_hosts)
        util.change_var(config, "addn-hosts", self.dnsmasq_hosts)
        util.change_var(config, "server", ipaddr)
        util.change_var(config, "domain", self.dnsmasq_domain)

    def d_add_node(self, node, ipaddr):
        """
        add node in dnsmasq hosts conf
        """
        #util.print_info(f"host {self.dnsmasq_hosts}")
        ip_exist = False
        with open(self.dnsmasq_hosts, 'r') as file:
            for line in file:
                if ipaddr in line:
                    ip_exist = True
                    break

        # no ip previously see in the config file
        if not ip_exist:
            with open(self.dnsmasq_hosts, "a") as file:
                file.write(ipaddr+" "+node+"\n")

    def dnsmasq_resolv_conf(self, config):
        """
        dnsmasq resolv config
        """
        util.create_if_not_exist(config)
        util.print_info(f"resolv {config}")
        util.change_var(self.dnsmasq_resolv, "nameserver", "127.0.0.1", " ")

    def dnsmasq_test(self):
        """
        check conf is ok
        """
        util.print_info("Testing dnsmasq configuration")
        util.run_command_with_except(self.dnsmasq+" --test")

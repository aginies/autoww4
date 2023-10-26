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
auto mode
"""

import autoww4.dhcpd as dhcpd
import autoww4.tftp as tftp
import autoww4.dnsmasq as dnsmasq
import autoww4.ww4 as ww4
import autoww4.util as util
import autoww4.configuration as configuration

class Automatic():
    """
    do all stuff!
    """

    def __init__(self):
        """
        init some stuff
        """

    def do_all(self):
        """
        do everything automatically
        """
        configuration.Configuration.check_user_settings(self)
        #import pprint as pp
        #pp.pprint(dir(self))
        util.backup_file(self.dhcpd_config_file)
        # dhcp part
        dhcpd.Dhcpd.dhcpd_interface(self)
        dhcpd.Dhcpd.set_authoritative(self, self.authoritative)
        # tftp
        tftp.tftp_enable()
        tftp.tftp_restart()
        # dnsmasq
        util.backup_file(self.dnsmasq_config_file)
        dnsmasq.enable_dnsmasq()
        dnsmasq.Dnsmasq.dnsmasq_config(self)
        dnsmasq.Dnsmasq.dnsmasq_resolv_conf(self)
        dnsmasq.restart_dnsmasq()
        # ww4
        util.backup_file(self.ww4_config_file)
        ww4.Ww4.ww4_warewulf_conf(self)
        util.backup_file(self.ww4_nodes_file)
        ww4.Ww4.ww4_nodes_conf(self)
        ww4.ww4_enable()
        ww4.ww4_restart()
        ww4.Ww4.create_nodes_list(self)
        # check dnsmask after adding node in ww4 config
        dnsmasq.Dnsmasq.dnsmasq_test(self)
        ww4.Ww4.import_container(self, "opensuse")
        ww4.Ww4.prepare_container(self)
        ww4.Ww4.container_set_default(self, self.nodename+"[1-"+str(self.nbnode)+"]")

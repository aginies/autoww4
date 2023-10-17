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
auto
"""

import autoww4.dhcpd as dhcpd
import autoww4.tftp as tftp
import autoww4.dnsmasq as dnsmasq
import autoww4.ww4 as ww4
import autoww4.util as util
import autoww4.configuration as conf

def doall():
    """
    do everything automatically
    """
    # dhcp part
    util.backup_file(conf.dhcpd_config_file)
    dhcpd.dhcpd_interface("eth0")
    dhcpd.set_authoritative("no")
    # tftp
    tftp.tftp_enable()
    tftp.tftp_restart()
    # dnsmasq
    util.backup_file(conf.dnsmasq_config_file)
    dnsmasq.enable_dnsmasq()
    dnsmasq.dnsmasq_config(conf.dnsmasq_config_file, conf.interface)
    dnsmasq.dnsmasq_resolv_conf(conf.dnsmasq_config_file)
    dnsmasq.restart_dnsmasq()
    # ww4
    util.backup_file(conf.ww4_config_file)
    ww4.ww4_warewulf_conf(conf.ww4_config_file)
    util.backup_file(conf.ww4_nodes_file)
    ww4.ww4_nodes_conf(conf.ww4_nodes_file)
    ww4.ww4_enable()
    ww4.ww4_restart()
    ww4.create_nodes_list()
    dnsmasq.dnsmasq_test()
    ww4.import_container("opensuse", "leap15.4")
    ww4.prepare_container("leap15.4")
    ww4.container_set_default("leap15.4", conf.nodename+"[1-"+str(conf.maxnode)+"]")

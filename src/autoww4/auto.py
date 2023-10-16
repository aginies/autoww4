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
import autoww4.configuration as conf

def doall():
    """
    do everything automatically
    """
    # dhcp part
    dhcpd.dhcpd_interface("eth0")
    dhcpd.set_authoritative("no")
    # tftp
    tftp.tftp_enable()
    tftp.tftp_start()
    # dnsmasq
    util.backup_file(conf.dnsmasq_config_file)
    dnsmasq.enable_dnsmasq()
    dnsmasq.dnsmasq_config(conf.dnsmasq_config_file)
    dnsmasq.dnsmasq_host_conf(conf.dnsmasq_config_file)
    dnsmasq.dnsmasq_resolv_conf(conf.dnsmasq_config_file)
    dnsmasq.dnsmasq_resolv_conf(conf.dnsmasq_config_file)
    dnsmasq.dnsmasq_test()
    dnsmasq.restart_dnsmasq()
    # ww4
    util.backup_file(conf.ww4_config_file)
    ww4.ww4_warewulf_conf(conf.ww4_config_file)

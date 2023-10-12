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

wwctl = "/usr/sbin/dnsmasq"

def restart_dnsmask():
    """
    restart dnsmask service
    """
    util.systemd_restart("dnsmasq")

def start_dnsmask():
    """
    start dnsmasq
    """
    util.systemd_start("dnsmasq")

def enable_dnsmask():
    """
    enable dnsmasq
    """
    util.systemd_enable("dnsmasq")

def dnsmasq_conf(config):
    """
    configure dnsmasq
    """
    # do backup
    # various config

def dnsmasq_host_conf(config):
    """
    dnsmasq host config
    """

def dnsmasq_resolv_conf(config):
    """
    dnsmasq resolv config
    """

def dnsmasq_test():
    """
    check conf is ok
    """

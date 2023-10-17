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
configuration
"""

import os
import autoww4.util as util

conffile_locations = [
    '.',
    '~/.local/autoww4',
    '/etc/autoww4',
    '/etc',
]

nodename = "slenode"
maxnode = 3
wwctl = "/usr/bin/wwctl"
dnsmasq_config_file = "/etc/dnsmasq.conf"
dnsmasq = "/usr/sbin/dnsmasq"
ww4_config_file = "/etc/warewulf/warewulf.conf"
ww4_nodes_file = "/etc/warewulf/nodes.conf"
tftp_config_file = "/etc/sysconfig/tftp"
dhcpd_sysconfig_file = "/etc/sysconfig/dhcpd"
dhcpd_config_file = '/etc/dhcpd.conf'

conffile_name = 'autoww4.yaml'

def find_file_dir(name, what):
    """
    find file
    """
    global conffile_locations
    conffile = "{}/{}".format(conffile_locations[0], name)

    for path in conffile_locations:
        path = os.path.expanduser(path)
        tofind = "{}/{}".format(path, name)
        if what == "file":
            if os.path.isfile(tofind):
                #print("configuration found: "+tofind)
                return tofind
        elif what == "dir":
            if os.path.isdir(tofind):
                return tofind

    return conffile

def find_conffile():
    global conffile_name
    return find_file_dir(conffile_name, "file")

def check_conffile(conf):
    """
    check if the configuration file is present
    """
    if os.path.isfile(conf) is False:
        util.print_error(conf+" configuration Yaml file Not found!")
        print("Please select one to contine:")
        print("conf /path/to/file.yaml")
        return False
    return True

class Configuration():
    """
    all stuff relative to configuration
    """
    conffile = find_conffile()
    util.check_iam_root()

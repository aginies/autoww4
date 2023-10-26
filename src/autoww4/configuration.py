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
import yaml
import autoww4.util as util

CONFFILE_LOCATIONS = [
    '.',
    '~/.local/autoww4',
    '/etc/autoww4',
    '/etc',
]

CONFFILE_NAME = 'autoww4.yaml'

def find_file_dir(name, what):
    """
    find file
    """
    global CONFFILE_LOCATIONS
    conffile = "{}/{}".format(CONFFILE_LOCATIONS[0], name)

    for path in CONFFILE_LOCATIONS:
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

def find_conffile():
    """
    find the conf file
    """
    global CONFFILE_NAME
    return find_file_dir(CONFFILE_NAME, "file")

class Configuration():
    """
    all stuff relative to configuration
    """
    util.check_iam_root()
    conffile = find_conffile()

    dataprompt = {
        'nodename': None,
        'dnsmasq_domain': None,
        'conf': conffile,
        'nbnode': None,
        'interface': None,
        'container': None,
        }

    find_interface = util.get_network_interface()
    interface = find_interface[0]
    nodename = "slenode"
    nbnode = 3
    container = ""
    authoritative = "off"
    on_off_options = ['on', 'off']
    hostname = util.get_hostname()

    dnsmasq_config_file = "/etc/dnsmasq.conf"
    dnsmasq_hosts = "/etc/dnsmasq-hosts.conf"
    dnsmasq_resolv = "/etc/dnsmasq-resolv.conf"
    dnsmasq = "/usr/sbin/dnsmasq"
    dnsmasq_domain = "sle.lan"

    wwctl = "/usr/bin/wwctl"
    ww4_config_file = "/etc/warewulf/warewulf.conf"
    ww4_nodes_file = "/etc/warewulf/nodes.conf"

    tftp_config_file = "/etc/sysconfig/tftp"
    dhcpd_config_file = '/etc/dhcpd.conf'
    dhcpd_sysconfig_file = "/etc/sysconfig/dhcpd"

    slurm_config_file = "/etc/slurm/slurm.conf"

    def __init__(self):
        """
        init some var
        """

    def basic_config(self):
        """
        basic config load
        """
        # Using autoww4.yaml to file some VAR
        with open(self.conf.conffile) as file:
            config = yaml.full_load(file)
            # parse all section of the yaml file
            for item, value in config.items():
                # check mathing section
                if item == "general":
                    for dall in value:
                        for datai, valuei in dall.items():
                            #print(valuei)
                            if datai == 'interface':
                                config = {'interface': valuei}
                                self.conf.dataprompt.update({'interface': config['interface']})
                            elif datai == 'nodename':
                                config = {'nodename': valuei}
                                self.conf.dataprompt.update({'nodename': config['nodename']})
                            elif datai == 'nbnode':
                                config = {'nbnode': valuei}
                                self.conf.dataprompt.update({'nbnode': config['nbnode']})
                            else:
                                util.print_error("Unknow parameter in general section: {}".format(datai))
                if item == "dnsmasq":
                    for dall in value:
                        for datai, valuei in dall.items():
                            if datai == 'dnsmasq_domain':
                                config = {'dnsmasq_domain': valuei}
                                self.conf.dataprompt.update({'dnsmasq_domain': config['dnsmasq_domain']})
                            #else:
                            #    util.print_error("Unknow parameter in dnsmasq section: {}".format(datai))

    def check_user_settings(self):
        """
        Check if the user as set some stuff, if yes use it
        """
        interface = self.dataprompt.get('interface')
        if interface != None:
            self.interface = interface

        nodename = self.dataprompt.get('nodename')
        if nodename != None:
            self.nodename = nodename

        nbnode = self.dataprompt.get('nbnode')
        if nbnode != None:
            self.nbnode = nbnode

        dnsmasq_domain = self.dataprompt.get('dnsmasq_domain')
        if dnsmasq_domain != None:
            self.dnsmasq_domain = dnsmasq_domain

        authoritative = self.dataprompt.get('authoritative')
        if authoritative != None:
            self.authoritative = authoritative

        container = self.dataprompt.get('container')
        if container != None:
            self.container = container

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
dhcpd config
"""

#import configparser
import autoww4.util as util
import autoww4.configuration as configuration

######
# ####

class Dhcpd():
    """
    all needed to work on dhcpd conf
    """
    def __init__(self):
        """
        init some stuff
        """

    def dhcpd_interface(self, interface):
        """
        change the interface
        """
        util.print_info("Setting DHCPD_INTERFACE to "+str(interface))
        util.change_var(self.dhcpd_sysconfig_file, "DHCPD_INTERFACE", str(interface))

    def set_authoritative(self, value):
        """
        authoritative or not
        yes or no
        """
        #import pprint as pp
        #pp.pprint(dir(self))

        with open(self.dhcpd_config_file, 'r') as file:
            dhcpd_conf = file.read()

        #print("HERE")

        if value == "no":
            if 'not authoritative;' not in dhcpd_conf:
                if 'authoritative' in dhcpd_conf:
                    dhcpd_conf = dhcpd_conf.replace('authoritative;', 'not authoritative;')
                else:
                    dhcpd_conf += '\nnot authoritative;\n'
                util.print_info("Setting dhcpd to not authoritative")
        elif value == "yes":
            if 'authoritative;' not in dhcpd_conf:
                if 'not authoritative' in dhcpd_conf:
                    dhcpd_conf = dhcpd_conf.replace('not authoritative;', 'authoritative;')
                else:
                    dhcpd_conf += '\nauthoritative;\n'
                util.print_info("Setting dhcpd to authoritative")
        else:
            util.print_error("Whats the hell?")

        with open(self.dhcpd_config_file, 'w') as file:
            file.write(dhcpd_conf)

        file.close()

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
Interactive mode for autoww4
"""

import os
from cmd import Cmd
import autoww4.util as util
#import autoww4.configuration as configuration
import autoww4.dhcpd as dhcpd
import autoww4.containers as containers
import autoww4.ww4 as ww4
import autoww4.auto as auto

######
# Interactive command
# ####

class Interactive(Cmd):
    """
    Interactive Cmd
    """

    def __init__(self, config):
        """
        Init the Cmd
        """
        self.conf = config
        Cmd.__init__(self)

        self.promptline = '_________________________________________\n'
        self.prompt = self.promptline +'> '
        self.prompt = 'autoww4 > '
        lines = []
        lines.append("\n"+util.esc('green') +" autoww4 "+util.esc('reset'))
        lines.append("Interactive Terminal!\n\n")

        self.intro = ''.join(lines)
        self.prompt = self.promptline+'\n'+'> '

    def do_interface(self, args):
        """
        Define the dhcpd interface
        """
        list_interface = util.get_network_interface()
        if args not in list_interface:
            util.print_error("Please select a correct interface name:")
            print(str(list_interface))
        else:
            dhcpd.dhcpd_interface(args)

    def complete_do_interface(self, text, _line, _begidx, _endidx):
        """
        Auto completion interface
        """
        list_interface = util.get_network_interface()
        if not text:
            completions = list_interface[:]
        else:
            completions = [f for f in list_interface if f.startswith(text)]
        return completions

    def do_list_containers_registry(self, args):
        """
        List all containers registry
        """
        if args not in containers.list_familly:
            util.print_error("Please select a correct familly:")
            print(str(containers.list_familly))
        else:
            util.list_containers_registry(args)

    def do_available_container(self, arfs):
        """
        List containers installed
        """
        ww4.containers_available()

    def complete_list_containers(self, text, _line, _begidx, _endidx):
        """
        Auto complete familly for containers
        """
        list_f = containers.list_familly
        if not text:
            completions = list_f[:]
        else:
            completions = [f for f in list_f if f.startswith(text)]
        return completions

    def do_auto(self, _args):
        """
        Do all the stuff automatically
        """
        auto.doall()

    def do_quit(self, _args):
        """
        Exit the application
        Shorthand: Ctrl-D
        """
        # French Flag :)
        print(util.esc('blue')+'Bye'+util.esc('white')+'Bye'+util.esc('red')+'Bye'+util.esc('reset'))
        return True

    do_EOF = do_quit

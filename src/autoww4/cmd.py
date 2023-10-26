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
import yaml
import autoww4.util as util
import autoww4.configuration as configuration
import autoww4.dhcpd as dhcpd
import autoww4.containers as containers
import autoww4.ww4 as ww4
import autoww4.auto as auto
#import pprint as pp

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

        configuration.Configuration.basic_config(self)
        self.promptline = '_________________________________________\n'
        self.prompt = self.promptline +'> '
        self.prompt = 'autoww4 > '
        lines = []
        lines.append("\n"+util.esc('green') +" autoww4 "+util.esc('reset'))
        lines.append("Interactive Terminal\n")
        lines.append("\n Available parameters:\n")
        lines.append(util.esc('blue')+" conf"+util.esc('reset')+": configuration file to use\n")
        lines.append(util.esc('blue')+" interface"+util.esc('reset')+": interface to use for dhcpd\n")
        lines.append(util.esc('blue')+" authoritative"+util.esc('reset')+": Set DHCPD server as authoritative or not\n")
        lines.append(util.esc('blue')+" nbnode"+util.esc('reset')+": how many nodes to prepare\n")
        lines.append(util.esc('blue')+" nodename"+util.esc('reset')+": node name (alphanumeric)\n")
        lines.append(util.esc('blue')+" dnsmasq_domain"+util.esc('reset')+": domain name for dnsmasq\n")
        lines.append("\n Container parameters:\n")
        lines.append(util.esc('blue')+" list_containers_registry"+util.esc('reset')+": list containers registry available\n")
        lines.append(util.esc('blue')+" available_containers"+util.esc('reset')+": containers already available on the system\n")
        lines.append(util.esc('blue')+" container"+util.esc('reset')+": container to use for deployment\n")

        #self.conf.dataprompt.update({'nodename': self.conf.dataprompt['nodename']})

        line1 = ""
        if os.path.isfile(self.conf.conffile):
            line1 = util.esc('green')+'Main Configuration: '+util.esc('reset')+self.conf.conffile+'\n'

        self.intro = ''.join(lines)
        self.prompt = self.promptline+line1+'\n'+'> '
        # fill data with default value
        self.update_prompt()
        self.list_interface = util.get_network_interface()

    def update_prompt(self):
        """
        update prompt with value set by user
        """
        options = [('Network Interface', 'interface'),
                   ('authoritative', 'authoritative'),
                   ('Node Name', 'nodename'),
                   ('Number Node(s)', 'nbnode'),
                   ('dnsmasq domain', 'dnsmasq_domain'),
                   ('Main Configuration', 'conf'),
                   ('Container', 'container'),
                  ]

        lines = []
        self.promptline = '---------- User Settings ----------\n'

        for option_name, option_key in options:
            option_value = self.conf.dataprompt.get(option_key)
            if option_value is not None:
                line = util.esc('green')+option_name+': '+util.esc('reset')+str(option_value)+'\n'
                # append to the main line
                lines.append(line)

        output = ''.join(lines)
        self.prompt = self.promptline+output+'\n'+'> '

    def do_interface(self, args):
        """
        Define the dhcpd interface
        """
        if args not in self.list_interface:
            util.print_error("Please select a correct interface name:")
            print(str(self.list_interface))
        else:
            config = {'interface': args,}
            self.conf.dataprompt.update({'interface': config['interface']})
            self.update_prompt()
            self.interface = args
            dhcpd.Dhcpd.dhcpd_interface(self.conf)

    def complete_interface(self, text, _line, _begidx, _endidx):
        """
        Auto completion interface
        """
        if not text:
            completions = self.list_interface
        else:
            completions = [f for f in self.list_interface if f.startswith(text)]
        return completions

    def do_authoritative(self, args):
        """
        Set Dhcpd server in authoritative or not
        """
        if args not in self.conf.on_off_options:
            util.print_error("Available options are: on / off")
        else:
            if args == "on":
                dhcpd.Dhcpd.set_authoritative(self.conf, "on")
            else:
                dhcpd.Dhcpd.set_authoritative(self.conf, "off")

    def do_nodemane(self, args):
        """
        define the node name
        """
        if not isinstance(args, str) or args == "":
            util.print_error("Should be a alphanumeric")
        else:
            config = {'nodename': args,}
            self.conf.dataprompt.update({'nodename': config['nodename']})
            self.update_prompt()

    def do_dnsmasq_domain(self, args):
        """
        define the dnsmasq domain
        """
        if not isinstance(args, str) or args == "":
            util.print_error("Should be a alphanumeric")
        else:
            config = {'dnsmasq_domain': args}
            self.conf.dataprompt.update({'dnsmasq_domain': config['dnsmasq_domain']})
            self.update_prompt()

    def do_conf(self, args):
        """
        Select the yaml configuration file
        """
        file = args
        if os.path.isfile(file):
            Cmd.file = file
            util.validate_yaml_file(Cmd.file)
            self.conf.conffile = file
            config = {'conf': file}
            self.conf.dataprompt.update({'conf': config['conf']})
            self.update_prompt()
        else:
            util.print_error("File " +file +" Doesnt exist!")

    def do_nbnode(self, args):
        """
        how many node to configure
        """
        if args.isdigit() is False:
            util.print_error("Number of node must be a ... Number")
        else:
            config = {'nbnode': args,}
            self.conf.dataprompt.update({'nbnode': config['nbnode']})
            self.update_prompt()

    def do_list_containers_registry(self, args):
        """
        List all containers registry
        """
        if args not in containers.LIST_FAMILLY:
            util.print_error("Please select a correct familly:")
            print(str(containers.LIST_FAMILLY))
        else:
            util.list_containers_registry(args)

    def complete_list_containers_registry(self, text, _line, _begidx, _endidx):
        """
        Auto complete familly for containers
        """
        list_f = containers.LIST_FAMILLY
        if not text:
            completions = list_f[:]
        else:
            completions = [f for f in list_f if f.startswith(text)]
        return completions

    def do_available_containers(self, _args):
        """
        List containers installed
        """
        ww4.Ww4.containers_available(self.conf)

    def do_container(self, args):
        """
        Select the container to use
        locked to opensuse for now
        """
        l_c_r = util.list_containers_registry("opensuse")
        if args not in l_c_r:
            util.print_error("Please select a container in registry")
        else:
            config = {'container': args,}
            self.conf.dataprompt.update({'container': config['container']})
            self.update_prompt()

    def complete_container(self, text, _line, _begidx, _endidx):
        """
        Auto complete container name
        """
        list_c = util.list_containers_registry("opensuse")
        if not text:
            completions = list_c[:]
        else:
            completions = [f for f in list_c if f.startswith(text)]
        return completions

    def do_test(self, _args):
        """
        test
        """
        ww4.Ww4.get_nodes_list(self.conf)

    def do_auto(self, _):
        """
        Do all the stuff automatically
        """
        auto.Automatic.do_all(self.conf)

    def do_quit(self, _):
        """
        Exit the application
        Shorthand: Ctrl-D
        """
        # French Flag :)
        print(util.esc('blue')+'Bye'+util.esc('white')+'Bye'+util.esc('red')+'Bye'+util.esc('reset'))
        return True

    do_EOF = do_quit

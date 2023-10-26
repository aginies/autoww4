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
ww4 config
"""

import subprocess
import autoww4.util as util
import autoww4.containers as containers
import autoww4.dnsmasq as dnsmasq

def ww4_start():
    """
    start warewulfd service
    """
    util.print_info("Starting ww4")
    util.systemd_start("warewulfd")

def ww4_restart():
    """
    restart warewulfd service
    """
    util.print_info("Re-Starting ww4")
    util.systemd_restart("warewulfd")

def ww4_enable():
    """
    enable warewulfd service
    """
    util.print_info("Enabling ww4")
    util.systemd_enable("warewulfd")

class Ww4():
    """
    manage warewulf 4
    """

    def import_container(self, familly):
        """
        import a container
        """
        util.print_info(f"Importing container: {familly} {self.container}")
        list_containers = Ww4.containers_available(self)
        for test in list_containers:
            if test == self.container:
                util.print_error(f"{familly} {self.container} already imported")
            else:
                if familly == "opensuse":
                    for plist in containers.OPENSUSE_LIST:
                        if plist == self.container:
                            container_url = containers.OPENSUSE_BASE_URL+plist+"/containers/kernel:latest"
                            cmd = self.wwctl+" container import "+container_url+" "+self.container
                            util.print_command(cmd)
                            util.run_command_live(cmd)

    def ww4_nodes_conf(self):
        """
        nodes.conf parameter for ww4
        """
        util.print_info(f"validating ww4 {self.ww4_nodes_file}")
        util.validate_yaml_file(self.ww4_nodes_file)

    def ww4_warewulf_conf(self):
        """
        warewulf config
        """
        util.print_info(f"{self.ww4_config_file}")

    def add_node(self, node, ipaddr):
        """
        add node
        """
        nodes_list = Ww4.get_nodes_list(self)
        #print(nodes_list)
        if node not in nodes_list:
            util.print_data("Adding:", f"{node} {ipaddr}")
            util.run_command_with_except(self.wwctl +" node add "+node+" -I "+ipaddr)
            #util.run_command(self.wwctl +"node list")
        else:
            util.print_warning(f"{node} already in ww4 config")

    def get_nodes_list(self):
        """
        get the node list
        """
        command = self.wwctl+" node list"
        try:
            output_bytes = subprocess.check_output(command, shell=True)
            output_str = output_bytes.decode('utf-8')
            lines = output_str.split('\n')
            nodes_names = [line.split()[0] for line in lines if line.strip() and line.split()]
            nodes_list = nodes_names[2:]
            if nodes_list:
                pass
            else:
                nodes_list = ["EMPTY"]
            return nodes_list
        except subprocess.CalledProcessError as err:
            print(f"Error: {err.returncode}\n{err.output}")

    def containers_available(self):
        """
        container list
        """
        command = self.wwctl+" container list"
        try:
            output_bytes = subprocess.check_output(command, shell=True)
            output_str = output_bytes.decode('utf-8')
            lines = output_str.split('\n')

            container_names = [line.split()[0] for line in lines if line.strip() and line.split()]
            container_list = container_names[1:]
            if container_list:
                util.print_info(f"Container(s) already imported:")
                for name in container_list:
                    print(name)
            else:
                container_list = ["EMPTY"]
                util.print_warning("No containers currently available on this system")
            return container_list

        except subprocess.CalledProcessError as err:
            print(f"Error: {err.returncode}\n{err.output}")

    def prepare_container(self):
        """
        ssh root key from host
        munge key from host
        node list
        slurm configuration
        """
        util.print_info(f"Working on {self.container}")

    def container_set_default(self, node):
        """
        set the default container to use
        """
        util.print_info(f"{node} set container to {self.container}")
        util.run_command_live(self.wwctl+" node set --container "+self.container+" "+node)

    def create_nodes_list(self):
        """
        create the node list from dhcpd config
        """
        # create the node config with nodemane and IP
        subnet_ranges = util.extract_subnet_range(self.dhcpd_config_file)
        #print(subnet_ranges)
        util.print_info("Create the ww4 node list")
        for _, range_i in subnet_ranges:
            number = 1
            parts_range_ip = range_i[0].split(".")[:3]
            range_ip = ".".join(parts_range_ip)
            last_number_ip = range_i[0].split(".")[-1]
            while number <= int(self.nbnode):
                lastip = int(last_number_ip)+number
                ipaddr = range_ip+"."+str(lastip)
                nname = self.nodename+str(number)
                Ww4.add_node(self, nname, ipaddr)
                dnsmasq.Dnsmasq.d_add_node(self, nname, ipaddr)
                number += 1

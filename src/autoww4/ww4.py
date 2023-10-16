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
import autoww4.configuration as conf

def ww4_start():
    """
    start warewulfd service
    """
    util.systemd_start("warewulfd")

def ww4_restart():
    """
    restart warewulfd service
    """
    util.systemd_restart("warewulfd")

def ww4_enable():
    """
    enable warewulfd service
    """
    util.systemd_enable("warewulfd")

def import_container(container):
    """
    import a container
    """

def ww4_nodes_conf(config):
    """
    nodes.conf parameter for ww4
    """
    util.validate_yaml_file(config)

def ww4_warewulf_conf(config):
    """
    warewulf config
    """

def add_node(node, ipaddr):
    """
    add node
    """
    util.run_command_with_except(conf.wwctl +" node add "+node+" -I "+ipaddr)
    util.run_command(conf.wwctl +"node list")

def containers_available():
    """
    container list
    """
    command = conf.wwctl+" container list"
    try:
        output_bytes = subprocess.check_output(command, shell=True)
        output_str = output_bytes.decode('utf-8')
        lines = output_str.split('\n')

        container_names = [line.split()[0] for line in lines if line.strip() and line.split()]
        container_list = container_names[1:]

        for name in container_list:
            print(name)

        return container_list

    except subprocess.CalledProcessError as err:
        print(f"Error: {err.returncode}\n{err.output}")

def prepare_container(container):
    """
    ssh root key from host
    munge key from host
    node list
    slurm configuration
    """

def container_set_default(container, node):
    """
    set the default container to use
    """
    util.run_command_with_except(conf.wwctl+" node set --container "+container+" "+node)

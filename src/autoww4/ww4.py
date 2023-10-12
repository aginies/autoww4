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

import autoww4.util as util

wwctl = "/usr/bin/wwctl"

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

def ww4_warewulf_conf(config):
    """
    warewulf config
    """

def prepare_container(container):
    """
    ssh root key from host
    munge key from host
    node list
    slurm configuration
    """

def container_set_default(container):
    """
    set the default container to use
    """

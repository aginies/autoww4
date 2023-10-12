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
tftp config
"""

import autoww4.util as util

######
# ####

tftp_config_file = "/etc/sysconfig/tftp"
tftp_config_file = "/tmp/tftp"

def tftp_directory(directory):
    """
    change the directory
    """
    util.change_var(tftp_config_file, "TFTP_DIRECTORY", str(directory))


def tftp_option(options):
    """
    change tftp options
    """
    util.change_var(tftp_config_file, "TFTP_OPTIONS", str(options))

def tftp_enable():
    """
    enable the tftp service
    """
    util.systemd_enable("tftp")

def tftp_start():
    """
    start the tftp service
    """
    util.systemd_start("tftp")

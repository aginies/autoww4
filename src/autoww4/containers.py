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
containers registry
"""

LIST_FAMILLY = ["opensuse", "ubuntu"]

OPENSUSE_BASE_URL = "docker://registry.opensuse.org/science/warewulf/"
OPENSUSE_LIST = [
    "leap-15.3",
    "leap-15.4",
    "leap-15.5",
    "tumbleweed",
]

UBUNTU_BASE_URL = "docker://registry.ubuntu.org/"
UBUNTU_LIST = [
    "20.4",
    "22.4",
    "23.4",
]

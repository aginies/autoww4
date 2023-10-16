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

list_familly = ["opensuse", "ubuntu"]

opensuse_base_url = "docker://registry.opensuse.org/science/warewulf/"
opensuse_list = [
    "leap15.3",
    "leap15.4",
    "leap15.5",
    "leap15.6",
    "tumbleweed",
]

ubuntu_base_url = "docker://registry.ubuntu.org/"
ubuntu_list = [
    "20.4",
    "22.4",
    "23.4",
]

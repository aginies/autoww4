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
import autoww4.configuration as configuration

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
        lines.append("\n"+util.esc('green') +" autoww4 "+util.esc('reset')+ "Interactive Terminal!\n\n")

        self.intro = ''.join(lines)
        self.prompt = self.promptline+'\n'+'> '

    def do_quit(self, _args):
        """
        Exit the application
        Shorthand: Ctrl-D
        """
        # French Flag :)
        print(util.esc('blue')+'Bye'+util.esc('white')+'Bye'+util.esc('red')+'Bye'+util.esc('reset'))
        return True

    do_EOF = do_quit

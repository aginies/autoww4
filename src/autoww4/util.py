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
Util
"""

import subprocess
import os
import shutil
import datetime
import re
import socket
import fcntl
import struct
import yaml
import psutil
import socket
import autoww4.containers as containers

def run_command(cmd):
    """
    Launch a system command
    """
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.wait()
    out, errs = proc.communicate(timeout=5)
    out = out.decode('utf-8')
    return out, errs

def run_command_with_except(cmd):
    """
    run command with except
    """
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=True, encoding='utf8', universal_newlines=True)
        stdout = result.stdout
        stderr = result.stderr
        return stdout, stderr

    except subprocess.CalledProcessError as err:
        print(f"Command:\n'{cmd}'\n failed with exit code {err.returncode}:")
        print(err.stderr)

def run_command_live(cmd):
    """
    run a live command
    """
    process = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True
    )

    # Read and print the output line by line
    for line in process.stdout:
        print(line, end='')
    process.wait()
    if process.returncode == 0:
        pass
    else:
        print(f"Command {cmd} failed with return code {process.returncode}")

def systemd_start(service):
    """
    Start the service
    """
    run_command_with_except("systemctl start "+service)

def systemd_restart(service):
    """
    restart the service
    """
    run_command_with_except("systemctl restart "+service)

def systemd_enable(service):
    """
    enable the service
    """
    run_command("systemctl enable "+ service)

def cmd_exists(cmd):
    """
    check a command exist
    """
    return shutil.which(cmd) is not None

def get_network_interface():
    """
    get the list of available interface on the system
    """
    interfaces = psutil.net_if_addrs()
    interface_list = []
    # _ = addresses
    for interface_name, _ in interfaces.items():
        interface_list.append(interface_name)
    return interface_list

def select_an_interface():
    """
    select a default interface
    """
    interface_list = get_network_interface()
    selected_index = next((index for index, iface in enumerate(interface_list) if iface.startswith('eth') or 'ensp' in iface), None)
    return interface_list[selected_index]

def get_hostname():
    """
    get hostname of current server
    """
    hostname = socket.gethostname()
    return hostname

def list_containers_registry(familly):
    """
    list all containers available
    """
    if familly == "opensuse":
        for plist in containers.OPENSUSE_LIST:
            #print(containers.OPENSUSE_BASE_URL+plist+"/containers/kernel:latest")
            print(plist)
        return containers.OPENSUSE_LIST
    elif familly == "ubuntu":
        for plist in containers.UBUNTU_LIST:
            #print(containers.UBUNTU_BASE_URL+plist+"/containers/kernel:latest")
            print(plist)
        return containers.UBUNTU_LIST

def change_var(conffile, var_to_change, var_value, equal="="):
    """
    change var in a config file
    """
    config_file_path = conffile
    modified_lines = []
    change_made = False
    if os.path.isfile(config_file_path):
        with open(config_file_path, 'r') as file:
            for line in file:
            # Check if the line contains the variable you want to change
                if (not change_made) and (line.strip().startswith(var_to_change + equal) or line.strip().startswith('#' + var_to_change + equal)):
                    # If it's a commented line, uncomment it
                    if line.strip().startswith('#'):
                        line = line.replace('#', '', 1)
                    # Update the value
                    line = var_to_change + equal + var_value + '\n'
                    change_made = True
                modified_lines.append(line)

        if not change_made:
            modified_lines.append(var_to_change + equal + var_value + '\n')

        # Open the config file for writing and save the changes
        with open(config_file_path, 'w') as file:
            file.writelines(modified_lines)

        print(f'{var_to_change} set to {var_value}')
        file.close()
    else:
        print_error(config_file_path+" Doesnt exist!")

COLORS = {
    'reset': '\033[0m',
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'bg_black': '\033[40m',
    'bg_red': '\033[41m',
    'bg_green': '\033[42m',
    'bg_yellow': '\033[43m',
    'bg_blue': '\033[44m',
    'bg_purple': '\033[45m',
    'bg_cyan': '\033[46m',
    'bg_white': '\033[47m',
}

def esc(color):
    """
    Return the ANSI escape code for the given color
    """
    return COLORS[color]

def print_error(text):
    """
    Print error in red
    """
    prefix = esc('bg_yellow') + ' ERROR ' + esc('reset') + " "
    formated_text = prefix+esc('red')+text+esc('reset')+"\n"
    print(formated_text)

def print_warning(text):
    """
    Print warning in red
    """
    prefix = esc('bg_yellow') + ' WARNING ' + esc('reset') + " "
    formated_text = "     "+prefix+esc('red') +text.upper()+esc('reset')
    print(formated_text)

def print_ok(text):
    """
    Print ok in green
    """
    formated_text = esc('green')+text+esc('reset')
    print(formated_text)

def print_info(text):
    """
    Print info in green
    """
    formated_text = esc('bg_blue')+text+esc('reset')+" "
    print(formated_text)

def print_summary(text):
    """
    Print title with blue background
    """
    formated_text = "\n"+esc('bg_blue')+text+esc('reset')+"\n"
    print(formated_text)

def print_title(text):
    """
    Print summary with magenta background
    """
    formated_text = esc('bg_purple')+text.upper()+esc('reset')
    print(formated_text)

def print_summary_ok(text):
    """
    Print summary with green background
    """
    formated_text = esc('bg_green')+text+esc('reset')+"\n"
    print(formated_text)

def print_command(text):
    """
    Print command with blue background
    """
    formated_text = esc('bg_blue')+text+esc('reset')+"\n\n"
    print(formated_text)

def print_data(data, value):
    """
    Print the data
    """
    formated_text = "\n"+esc('bg_cyan')+data+" "+esc('reset')+" "+value.rstrip()
    print(formated_text.strip())

def validate_yaml_file(file_path):
    """
    validate the yaml file
    """
    try:
        with open(file_path, 'r') as stream:
            yaml_contents = yaml.safe_load(stream)
    except FileNotFoundError:
        print_error(f"file {file_path} not found.")
        return False
    except yaml.YAMLError as exc:
        print(f"Error while parsing the YAML file: {exc}")
        return False
    if not isinstance(yaml_contents, dict):
        print("File should contain a dict.")
        return False

    stream.close()
    return yaml_contents

def backup_file(file):
    """
    do a backup of the file with a timestamp
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    bck_file = f"{file}.{timestamp}.bck"
    try:
        shutil.copy(file, bck_file)
        print_info(f"Backup {file} to {bck_file}")
    except FileNotFoundError:
        print(f"Error: {file} not found")
    except Exception as err:
        print(f"An error occurred: {err}")

def check_iam_root():
    """
    some part needs to be root user
    """
    if os.geteuid() != 0:
        print_error("You are not root.")
        return False
    return True

def find_ext_file(ext):
    """
    Show all extension files in current path
    """
    files_list = []
    for files in os.listdir('.'):
        if files.endswith(ext):
            files_list.append(files)
    return files_list

def extract_subnet_range(config):
    """
    return all subnet available
    """
    subnet_pattern = re.compile(r'subnet\s+([\d.]+)\s+netmask\s+([\d.]+)\s*{([^}]*)}', re.MULTILINE)
    range_pattern = re.compile(r'range\s+([\d.]+)\s+([\d.]+);')
    subnet_ranges = []

    with open(config, 'r') as dhcpd_conf:
        contents = dhcpd_conf.read()
        for subnet_match in subnet_pattern.finditer(contents):
            subnet_info = subnet_match.group(1, 2)
            for range_match in range_pattern.finditer(subnet_match.group(3)):
                subnet_ranges.append((subnet_info, range_match.group(1, 2)))

    return subnet_ranges


def get_ip_address(interface):
    """
    get the ipaddress of an interface
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip_address = socket.inet_ntoa(fcntl.ioctl(
            sock.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', interface[:15].encode('utf-8'))
        )[20:24])

        return ip_address
    except Exception as err:
        return str(err)

def create_if_not_exist(afile):
    """
    create a file if it doesnt exist
    """
    if os.path.isfile(afile):
        pass
    else:
        try:
            with open(afile, "w") as file:
                pass
        except FileNotFoundError:
            print(f"File '{file}' not found.")
        except Exception as err:
            print(f"An error occurred: {err}")

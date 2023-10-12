# Name

Automation of warewulf4 configuration and other services on an operating system.

# Goals

Prepare everything to be able to deploy Compute nodes with ww4.

* **dnsmask**: dns ready
 **tftp**: get it ready
* **ww4**:
    * general configure
    * nodes
    * get container
    * prepare container (ssh key, munge key, slurm, etc...)
* **firewalld**: permit dns and dhcp request

# User Settings

Example:
```yaml
# WARNING: INCORRET PARAMATERS WILL LEAD TO BAD VM CONFIGURATION
# Dont change the section name
```

# Usage

```
python3 -m autoww4
```

# Functions

[tftp.py](src/autoww4/tftp.py)
```
tftp_directory(directory)
tftp_option(options)
tftp_enable()
tftp_start()
```

[dhcpd.py](src/autoww4/dhcpd.py)
```
dhcpd_interface(interface)
set_authoritative(value)
```

# Code

[Source](https://github.com/aginies/autoww4)

[Issues](https://github.com/aginies/autoww4/issues)

# Authors

Written by Antoine Ginies

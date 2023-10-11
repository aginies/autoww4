# Name

hpc warewul4 automatic configuration

# Goals

Prepare everything to be able to deploy Compute nodes with ww4.

* **dnsmask**: dns ready
* **tftp**: get it ready
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

# Code

[Source](https://github.com/aginies/hpc)

[Issues](https://github.com/aginies/hpc/issues)

# Authors

Written by Antoine Ginies

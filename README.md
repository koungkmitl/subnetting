# subnetting

## Details

[Download subnetting.exe v0.1.1](https://github.com/pe3zx/subnetting/releases/tag/v0.1.1)

Subnetting is python-based CLI program that provides capability for subnetting IPv4.

```
C:>subnetting.exe
Enter IP Address with subnet mask: 192.168.0.0/20
Enter amount of subnet: 2
Enter amount of hosts: 64
Enter amount of hosts: 256
192.168.0.0/25 255.255.255.128
192.168.2.0/23 255.255.254.0
```

## Dependencies

For Debian/Ubuntu/DEB-based distro:

```
sudo apt-get install python-pip
sudo pip install netaddr
```
For Windows, [pip](https://pip.pypa.io/en/latest/installing.html) is required:

```
pip install netaddr
```

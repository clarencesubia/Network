#!/usr/bin/env python3

from jnpr.junos import Device
from lxml import etree


with Device(host='192.168.3.101', user="ayens", ssh_private_key_file="/home/ayens/.ssh/id_rsa") as dev:
    config = dev.rpc.get_config()
    res = etree.tostring(config, encoding="unicode")
    print(res)

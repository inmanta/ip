"""
    Copyright 2012 KU Leuven Research and Development - iMinds - Distrinet

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Administrative Contact: dnet-project-office@cs.kuleuven.be
    Technical Contact: bart.vanbrabant@cs.kuleuven.be
"""
from Imp.plugins.base import plugin
from operator import attrgetter
import iplib

@plugin
def hostname(fqdn : "string") -> "string":
    """
        Return the hostname part of the fqdn
    """
    return fqdn.split(".")[0]

@plugin
def networkaddress(ip : "ip::Alias") -> "string":
    """
        Return the network address
    """
    net = iplib.CIDR(ip.ipaddress, ip.netmask)
    return str(net.network_ip)

@plugin
def network(ip : "ip::ip", cidr : "string") -> "string":
    """
        Given the ip and the cidr, return the network address
    """
    net = iplib.CIDR("%s/%s" % (ip, cidr))
    return str(net.network_ip)

@plugin
def netmask(cidr : "number") -> "ip::ip":
    """
        Given the cidr, return the netmask
    """
    inp = iplib.detect_nm(cidr)
    return str(iplib.convert_nm(cidr, notation="dot", inotation=inp))

@plugin
def concat(host : "std::hoststring", domain : "std::hoststring") -> "std::hoststring":
    """
        Concat host and domain
    """
    return "%s.%s" % (host, domain)

@plugin
def net_to_nm(network_addr : "string") -> "string":
    net = iplib.CIDR(network_addr)
    return str(net.netmask)

@plugin
def connect_to(scope : "ip::services::VirtualScope") -> "string":
    scope = scope[0]._get_instance()
    if hasattr(scope, "hostname"):
        return scope.hostname
    else:
        raise Exception("Unable to determine connection endpoint")

    return ""

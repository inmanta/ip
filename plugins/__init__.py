"""
    Copyright 2016 Inmanta

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Contact: code@inmanta.com
"""
from inmanta.plugins import plugin
from operator import attrgetter
import iplib
import netaddr


@plugin
def hostname(fqdn: "string") -> "string":
    """
        Return the hostname part of the fqdn
    """
    return fqdn.split(".")[0]


@plugin
def networkaddress(ip: "ip::Alias") -> "string":
    """
        Return the network address
    """
    net = iplib.CIDR(ip.ipaddress, ip.netmask)
    return str(net.network_ip)


@plugin
def network(ip: "ip::ip", cidr: "string") -> "string":
    """
        Given the ip and the cidr, return the network address
    """
    net = iplib.CIDR("%s/%s" % (ip, cidr))
    return str(net.network_ip)


@plugin
def cidr_to_network(cidr: "string") -> "string":
    """
        Given cidr return the network address
    """
    net = iplib.CIDR(cidr)
    return str(net.network_ip)


@plugin
def netmask(cidr: "number") -> "ip::ip":
    """
        Given the cidr, return the netmask
    """
    inp = iplib.detect_nm(cidr)
    return str(iplib.convert_nm(cidr, notation="dot", inotation=inp))


@plugin
def concat(host: "std::hoststring", domain: "std::hoststring") -> "std::hoststring":
    """
        Concat host and domain
    """
    return "%s.%s" % (host, domain)


@plugin
def net_to_nm(network_addr: "string") -> "string":
    net = iplib.CIDR(network_addr)
    return str(net.netmask)


@plugin
def connect_to(scope: "ip::services::VirtualScope") -> "string":
    return scope[0].hostname


@plugin
def ipnet(addr: "ip::cidr", what: "string") -> "string":
    net = netaddr.IPNetwork(addr)
    if what == "ip":
        return str(net.ip)

    elif what == "prefixlen":
        return str(net.prefixlen)

    elif what == "netmask":
        return str(net.netmask)

    elif what == "network":
        return str(net.network)


@plugin
def ipindex(addr: "ip::cidr", position: "number") -> "string":
    """
        Return the address at position in the network.
    """
    net = netaddr.IPNetwork(addr)
    return str(net[position])
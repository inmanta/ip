import pytest

@pytest.mark.parametrize(
        "cidr,ip,prefixlen,netmask,network",
        [
            ("192.168.5.3/16", "192.168.5.3", "16", "255.255.0.0", "192.168.0.0"),
            ("2001:0db8:85a3::8a2e:0370:7334/64", "2001:db8:85a3::8a2e:370:7334", "64", "ffff:ffff:ffff:ffff::", "2001:db8:85a3::")
        ]
)
def test_ipnet(project, cidr, ip, prefixlen, netmask, network):
    ipnet = project.get_plugin_function("ipnet")

    assert ipnet(cidr, "ip") == ip
    assert ipnet(cidr, "prefixlen") == prefixlen
    assert ipnet(cidr, "netmask") == netmask
    assert ipnet(cidr, "network") == network



@pytest.mark.parametrize(
        "cidr, idx, result",
        [
            ("192.168.5.3/16", 1, "192.168.0.1"),
            ("192.168.5.3/16", 256, "192.168.1.0"),
            ("2001:0db8:85a3::8a2e:0370:7334/64", 1, "2001:db8:85a3::1"),
            ("2001:0db8:85a3::8a2e:0370:7334/64", 10000, "2001:db8:85a3::2710"),
            ("2001:0db8:85a3::8a2e:0370:7334/64", 100000, "2001:db8:85a3::1:86a0")
        ]
)
def test_ipindex(project, cidr, idx, result):
    ipnet = project.get_plugin_function("ipindex")
    assert ipnet(cidr, idx) == result
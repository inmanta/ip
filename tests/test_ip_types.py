import pytest
import inmanta.ast


def run_test(project, thetype, value, is_ok):
    def make():
        project.compile(
                f"""
import ip
entity Holder:
    {thetype} value
end
implement Holder using std::none

Holder(value="{value}")
"""
            )

    if not is_ok:
        with pytest.raises(inmanta.ast.RuntimeException):
            make()
    else:
        make()

@pytest.mark.parametrize(
    "ip,is_ok",
    [
        ("192.168.5.3",True),
        ("5236",True),
        ("635.236.45.6",False),
        ("1.1.1.1/32",False),
        ("2001:0db8:85a3:0000:0000:8a2e:0370:7334", False)
    ]
)
def test_ip(project, ip, is_ok):
   run_test(project, "ip::ip", ip, is_ok)

@pytest.mark.parametrize(
    "ip,is_ok",
    [
        ("192.168.5.3",False),
        ("5236/24",False),
        ("635.236.45.6/32",False),
        ("1.1.1.1/32",True),
        ("2001:0db8:85a3:0000:0000:8a2e:0370:7334/36", False)
    ]
)
def test_cidr(project, ip, is_ok):
    run_test(project, "ip::cidr", ip, is_ok)


@pytest.mark.parametrize(
    "ip,is_ok",
    [
        ("192.168.5.3",False),
        ("5236",False),
        ("2z01:0db8:85a3:0000:0000:8a2e:0370:7334",False),
        ("2001:0db8:85a3::8a2e:0370:7334",True),
        ("2001:0db8:85a3:0000:0000:8a2e:0370:7334", True)
    ]
)
def test_ip_v6(project, ip, is_ok):
    run_test(project, "ip::ip_v6", ip, is_ok)

@pytest.mark.parametrize(
    "ip,is_ok",
    [
        ("192.168.5.3/32",False),
        ("2z01:0db8:85a3:0000:0000:8a2e:0370:7334/64",False),
        ("2001:0db8:85a3:0000:0000:8a2e:0370:7334/64", True),
        ("2001:0db8:85a3::8a2e:0370:7334/64", True)
    ]
)
def test_cidr_v6(project, ip, is_ok):
    run_test(project, "ip::cidr_v6", ip, is_ok)

@pytest.mark.parametrize(
    "ip,is_ok",
    [
        ("192.168.5.3",True),
        ("5236",True),
        ("2z01:0db8:85a3:0000:0000:8a2e:0370:7334",False),
        ("2001:0db8:85a3::8a2e:0370:7334",True),
        ("2001:0db8:85a3:0000:0000:8a2e:0370:7334", True)
    ]
)
def test_ip_v10(project, ip, is_ok):
    run_test(project, "ip::ip_v10", ip, is_ok)

@pytest.mark.parametrize(
    "ip,is_ok",
    [
        ("192.168.5.3/32",True),
        ("2z01:0db8:85a3:0000:0000:8a2e:0370:7334/64",False),
        ("2001:0db8:85a3:0000:0000:8a2e:0370:7334/64", True),
        ("2001:0db8:85a3::8a2e:0370:7334/64", True)
    ]
)
def test_cidr_v10(project, ip, is_ok):
    run_test(project, "ip::cidr_v10", ip, is_ok)
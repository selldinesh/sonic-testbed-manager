import sys
from ipaddress import ip_address, IPv4Address, IPv6Address
'''
In this file user can modify the line_card_choice and it chooses the corresponding hostname
and asic values from the config_set hostnames can be modified according to the dut hostname mentioned
in the snappi_sonic_devices.csv and asic values based on if its a chassis based dut

    chassis_single_line_card_single_asic : this option selects the ports form the
                                           hostname and its respective asic value

    chassis_single_line_card_multi_asic : this option selects the ports from the hostname
                                          and minimum of 1 port from each of the asic values

    chassis_multi_line_card_single_asic : this option selects min 1 port from each of
                                          the hostnames and its asic value

    chassis_multi_line_card_multi_asic : this option selects min of 1 port from hostname1
                                         and asic1 and 1 port from hostname2 and asic2

    non_chassis_multi_line_card : this option selects min of 1 port from hostname1
                                  and 1 port from hostname2

    non_chassis_single_line_card : this option selects all the ports from the hostname

'''
line_card_choice = 't1-t2-bgp'
config_set = {
                "chassis_single_line_card_single_asic": {
                    'hostname': ["sonic-s6100-dut1"],
                    'asic': ["asic0"]
                },
                "chassis_single_line_card_multi_asic": {
                    'hostname': ["sonic-s6100-dut1"],
                    'asic': ["asic0", "asic1"]
                },
                "chassis_multi_line_card_single_asic": {
                    'hostname': ["sonic-s6100-dut1", "sonic-s6100-dut2"],
                    'asic': ["asic1"]
                },
                "chassis_multi_line_card_multi_asic": {
                    'hostname': ["sonic-s6100-dut1", "sonic-s6100-dut2"],
                    'asic': ["asic0", "asic1"]
                },
                "non_chassis_multi_line_card": {
                    'hostname': ["sonic-s6100-dut1", "sonic-s6100-dut2"],
                    'asic': [None]
                },
                "non_chassis_single_line_card": {
                    'hostname': ["sonic-s6100-dut1"],
                    'asic': [None]
                },
                "t1-t2-bgp": {
                    'hostname': ["sonic-t1", "sonic-t2-uplink","sonic-t2-downlink"],
                    'asic': [None]
                },
            }
# Used for RDAM cases and for 
dut_ip_start = '40.0.1.1'
snappi_ip_start = '40.0.1.2'
prefix_length = 24

dut_ipv6_start = '4000:1::1'
snappi_ipv6_start = '4000:1::2'
v6_prefix_length = 16


def create_ip_list(value, count, mask=32, incr=0):
    '''
        Create a list of ips based on the count provided
        Parameters:
            value: start value of the list
            count: number of ips required
            mask: subnet mask for the ips to be created
            incr: increment value of the ip
    '''
    if sys.version_info.major == 2:
        value = unicode(value)          # noqa: F821

    ip_list = [value]
    for i in range(1, count):
        if ip_address(value).version == 4:
            incr1 = pow(2, (32 - int(mask))) + incr
            value = (IPv4Address(value) + incr1).compressed
        elif ip_address(value).version == 6:
            if mask == 32:
                mask = 64
            incr1 = pow(2, (128 - int(mask))) + incr
            value = (IPv6Address(value) + incr1).compressed
        ip_list.append(value)

    return ip_list

#START ---------------------   T2 BGP Case -------------------
# Expect the T1 and T2 orts to be routed ports and not part of any portchannel. The ports may or maynot have ips configured
SNAPPI_AS_NUM = 65100
SNAPPI_AS_NUM2 = 65400
T1_AS_NUM = 65700
T2_AS_NUM = 65300
AS_PATHS = [65002, 65003]
BGP_TYPE = 'ebgp'
route_count = 1000
v4_prefix_length = 24
v6_prefix_length = 64
TIMEOUT = 30

t1_t2_device_hostnames = ["sonic-t1", "sonic-t2-uplink","sonic-t2-downlink"]

#To DOs

# 1. Between T1 and t2 we should have a choice a porttchannel.
# Prerequisite checks vlan, portchannels, routed
# Add entropy for the bgp routes
t1_ports = {t1_t2_device_hostnames[0]:
            [
                'Ethernet64',
                'Ethernet68',
                'Ethernet72',
                'Ethernet76'
            ]
        }

t2_uplink_portchannel_members = {t1_t2_device_hostnames[1]:
                            [
                                ('Ethernet64', 'Ethernet68'),
                                ('Ethernet72', 'Ethernet76')
                            ]
                        }
t1_t2_downlink_interconected_port_info = [
                                {t1_t2_device_hostnames[0]:'Ethernet0', t1_t2_device_hostnames[2]:'Ethernet0'},
                                {t1_t2_device_hostnames[0]:'Ethernet4', t1_t2_device_hostnames[2]:'Ethernet4'}
                            ]

routed_port_count = len(t1_t2_downlink_interconected_port_info)+len(t1_ports[list(t1_ports.keys())[0]])
portchannel_count = len(t2_uplink_portchannel_members[list(t2_uplink_portchannel_members.keys())[0]])

t1_t2_dut_ipv4_list = create_ip_list('20.0.1.1', routed_port_count, mask=v4_prefix_length)
t1_t2_dut_ipv6_list = create_ip_list('2000:1::1', routed_port_count, mask=v6_prefix_length)

t1_t2_snappi_ipv4_list = create_ip_list('20.0.1.2', routed_port_count, mask=v4_prefix_length)
t1_t2_snappi_ipv6_list = create_ip_list('2000:1::2', routed_port_count, mask=v6_prefix_length)


t2_dut_portchannel_ipv4_list = create_ip_list('30.0.1.1', portchannel_count, mask=v4_prefix_length)
t2_dut_portchannel_ipv6_list = create_ip_list('3000:1::1', portchannel_count, mask=v6_prefix_length)

snappi_portchannel_ipv4_list = create_ip_list('30.0.1.2', portchannel_count, mask=v4_prefix_length)
snappi_portchannel_ipv6_list = create_ip_list('3000:1::2', portchannel_count, mask=v6_prefix_length)

# END ---------------------   T2 BGP Case -------------------

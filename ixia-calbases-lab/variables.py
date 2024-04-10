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
line_card_choice = 'non_chassis_single_line_card'
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
                }
            }

dut_ip_start = '20.0.1.1'
snappi_ip_start = '20.0.1.2'
prefix_length = 24

dut_ipv6_start = '2000:1::1'
snappi_ipv6_start = '2000:1::2'
v6_prefix_length = 16

#BGP
t1_ports = ['Ethernet64', 'Ethernet68', 'Ethernet72', 'Ethernet76']
t2_portchannel_port_groups = [('Ethernet64', 'Ethernet68'),('Ethernet72', 'Ethernet76')]
t1_t2_interconected_ports = {'sonic-s6100-dut1':'Ethernet0', 'sonic-s6100-dut2':'Ethernet0' }

t1_v4_subnet = '20.0.1.1'
prefix_length = 24
t2_v4_subnet = '30.0.1.1'

t1_v6_subnet = '2000:1::1'
prefix_length = 24
t2_v6_subnet = '2000:1::2'

#

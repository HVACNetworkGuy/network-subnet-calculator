"""Unit tests for the Network Subnet Calculator module."""

import pytest
from subnet_calculator import (
    calculate_subnet,
    cidr_to_decimal,
    decimal_to_cidr,
    print_subnet_info,
)


class TestCalculateSubnet:
      """Test suite for calculate_subnet function."""

    def test_calculate_subnet_class_c(self):
              """Test calculation of Class C subnet."""
              result = calculate_subnet('192.168.1.0/24')
              assert result is not None
              assert result['Network Address'] == '192.168.1.0'
              assert result['Broadcast Address'] == '192.168.1.255'
              assert result['Netmask'] == '255.255.255.0'
              assert result['Prefix Length'] == '/24'
              assert result['Number of Addresses'] == '256'
              assert result['Usable IPs'] == '254'
              assert result['First Host'] == '192.168.1.1'
              assert result['Last Host'] == '192.168.1.254'

    def test_calculate_subnet_class_a(self):
              """Test calculation of Class A subnet."""
              result = calculate_subnet('10.0.0.0/8')
              assert result is not None
              assert result['Network Address'] == '10.0.0.0'
              assert result['Broadcast Address'] == '10.255.255.255'
              assert result['Netmask'] == '255.0.0.0'
              assert result['Prefix Length'] == '/8'

    def test_calculate_subnet_class_b(self):
              """Test calculation of Class B subnet."""
              result = calculate_subnet('172.16.0.0/16')
              assert result is not None
              assert result['Network Address'] == '172.16.0.0'
              assert result['Broadcast Address'] == '172.16.255.255'
              assert result['Netmask'] == '255.255.0.0'
              assert result['Prefix Length'] == '/16'

    def test_calculate_subnet_invalid_input(self):
              """Test handling of invalid IP address."""
              result = calculate_subnet('invalid.ip.address/24')
              assert result is None

    def test_calculate_subnet_invalid_cidr(self):
              """Test handling of invalid CIDR notation."""
              result = calculate_subnet('192.168.1.0/33')
              assert result is None

    def test_calculate_subnet_slash_30(self):
              """Test calculation of /30 subnet (point-to-point)."""
              result = calculate_subnet('10.0.0.0/30')
              assert result is not None
              assert result['Usable IPs'] == '2'
              assert result['First Host'] == '10.0.0.1'
              assert result['Last Host'] == '10.0.0.2'

    def test_calculate_subnet_slash_31(self):
              """Test calculation of /31 subnet."""
              result = calculate_subnet('10.0.0.0/31')
              assert result is not None
              assert result['Usable IPs'] == '0'  # No first/last host


class TestCIDRToDecimal:
      """Test suite for cidr_to_decimal function."""

    def test_cidr_24_to_decimal(self):
              """Test conversion of /24 to decimal."""
              result = cidr_to_decimal(24)
              assert result == '255.255.255.0'

    def test_cidr_16_to_decimal(self):
              """Test conversion of /16 to decimal."""
              result = cidr_to_decimal(16)
              assert result == '255.255.0.0'

    def test_cidr_8_to_decimal(self):
              """Test conversion of /8 to decimal."""
              result = cidr_to_decimal(8)
              assert result == '255.0.0.0'

    def test_cidr_32_to_decimal(self):
              """Test conversion of /32 to decimal."""
              result = cidr_to_decimal(32)
              assert result == '255.255.255.255'

    def test_cidr_0_to_decimal(self):
              """Test conversion of /0 to decimal."""
              result = cidr_to_decimal(0)
              assert result == '0.0.0.0'


class TestDecimalToCIDR:
      """Test suite for decimal_to_cidr function."""

    def test_decimal_255_255_255_0_to_cidr(self):
              """Test conversion of 255.255.255.0 to /24."""
              result = decimal_to_cidr('255.255.255.0')
              assert result == 24

    def test_decimal_255_255_0_0_to_cidr(self):
              """Test conversion of 255.255.0.0 to /16."""
              result = decimal_to_cidr('255.255.0.0')
              assert result == 16

    def test_decimal_255_0_0_0_to_cidr(self):
              """Test conversion of 255.0.0.0 to /8."""
              result = decimal_to_cidr('255.0.0.0')
              assert result == 8

    def test_invalid_netmask(self):
              """Test handling of invalid netmask."""
              result = decimal_to_cidr('256.0.0.0')
              assert result is None


if __name__ == '__main__':
      pytest.main([__file__, '-v'])

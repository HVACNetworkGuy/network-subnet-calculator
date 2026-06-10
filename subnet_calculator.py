#!/usr/bin/env python3
"""
Network Subnet Calculator
A comprehensive tool for subnet calculations and IP planning.
"""

import ipaddress
import sys
from typing import Dict, Optional


def calculate_subnet(ip_cidr: str) -> Optional[Dict[str, str]]:
      """
          Calculate subnet information from an IP address and CIDR notation.

                  Args:
                          ip_cidr: IP address with CIDR notation (e.g., '192.168.1.0/24')

                                  Returns:
                                          Dictionary with subnet information or None if invalid input

                                                  Example:
                                                          >>> info = calculate_subnet('10.0.0.0/8')
                                                                  >>> print(info['Network Address'])
                                                                          10.0.0.0
                                                                              """
      try:
                network = ipaddress.ip_network(ip_cidr, strict=False)

        results = {
                      'Network Address': str(network.network_address),
                      'Broadcast Address': str(network.broadcast_address),
                      'Netmask': str(network.netmask),
                      'Prefix Length': f"/{network.prefixlen}",
                      'Number of Addresses': str(network.num_addresses),
                      'Usable IPs': str(network.num_addresses - 2) if network.num_addresses > 2 else '0',
        }

        if network.num_addresses > 2:
                      results['First Host'] = str(network.network_address + 1)
                      results['Last Host'] = str(network.broadcast_address - 1)

        return results
except (ipaddress.AddressValueError, ipaddress.NetmaskValueError, ValueError):
        return None


def print_subnet_info(ip_cidr: str) -> None:
      """
          Print formatted subnet information.

                  Args:
                          ip_cidr: IP address with CIDR notation
                              """
    info = calculate_subnet(ip_cidr)

    if info is None:
              print(f"Error: Invalid IP address or CIDR notation: {ip_cidr}")
              return

    print(f"\nSubnet Information for {ip_cidr}")
    print("=" * 50)
    for key, value in info.items():
              print(f"{key:.<30} {value}")
          print("=" * 50)


def cidr_to_decimal(cidr: int) -> str:
      """
          Convert CIDR notation to decimal subnet mask.

                  Args:
                          cidr: CIDR prefix length (0-32)

                                  Returns:
                                          Decimal subnet mask
                                              """
    try:
              mask = (0xffffffff >> (32 - cidr)) << (32 - cidr)
              return ".".join([str((mask >> (i << 3)) & 0xff) for i in (3, 2, 1, 0)])
except (ValueError, IndexError):
        return "Invalid CIDR"


def decimal_to_cidr(netmask: str) -> Optional[int]:
      """
          Convert decimal subnet mask to CIDR notation.

                  Args:
                          netmask: Decimal subnet mask (e.g., '255.255.255.0')

                                  Returns:
                                          CIDR prefix length or None if invalid
                                              """
    try:
              network = ipaddress.ip_network(f"0.0.0.0/{netmask}", strict=False)
              return network.prefixlen
except (ipaddress.AddressValueError, ValueError):
        return None


def main():
      """
          Main function for CLI usage.
              """
    if len(sys.argv) < 2:
              print("Usage: python subnet_calculator.py <IP/CIDR>")
              print("Example: python subnet_calculator.py 192.168.1.0/24")
              sys.exit(1)

    ip_cidr = sys.argv[1]
    print_subnet_info(ip_cidr)


if __name__ == "__main__":
      main()

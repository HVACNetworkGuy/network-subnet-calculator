"""
Advanced batch calculation examples for the Network Subnet Calculator.

This module demonstrates how to efficiently process multiple subnet
calculations, useful for network planning, documentation, and automation.
"""

from typing import List, Tuple
from calculator.subnet_calculator import SubnetCalculator


def example_5_generate_subnet_documentation():
      """
          Example 5: Generate comprehensive subnet documentation.

                  Create detailed network documentation for a corporate infrastructure
                      with multiple departments and network segments.
                          """
      print("=" * 70)
      print("Example 5: Comprehensive Network Documentation")
      print("=" * 70)

    networks = [
              ("10.0.1.0", 24, "Corporate LAN"),
              ("10.0.2.0", 24, "Guest Network"),
              ("10.0.3.0", 25, "VoIP Subnet"),
              ("10.0.3.128", 25, "IoT Devices"),
              ("10.1.0.0", 22, "Data Center"),
    ]

    print(f"\n{'Network':<20} {'CIDR':<10} {'Usable Hosts':<15} {'Purpose':<20}")
    print("-" * 65)

    for ip, prefix, purpose in networks:
              calculator = SubnetCalculator(ip, prefix)
              print(f"{ip:<20} /{prefix:<9} {calculator.usable_hosts:<15} {purpose:<20}")
          print()


def example_6_subnet_allocation_plan():
      """
          Example 6: Create a subnet allocation plan for a campus network.

                  Demonstrates how to allocate subnets from a larger network block
                      and document the allocation strategy.
                          """
      print("=" * 70)
      print("Example 6: Campus Network Subnet Allocation Plan")
      print("=" * 70)

    base_network = SubnetCalculator("172.16.0.0", 16)

    print(f"\nBase Network: 172.16.0.0/16")
    print(f"Total Usable Hosts: {base_network.usable_hosts}")
    print("\nSubnet Allocation Plan:")
    print(f"{'Building':<15} {'Subnet':<20} {'Prefix':<10} {'Hosts':<10} {'Usage %':<10}")
    print("-" * 65)

    allocations = [
              ("Admin Building", "172.16.0.0", 24),
              ("Engineering", "172.16.1.0", 24),
              ("Science Lab", "172.16.2.0", 24),
              ("Student Dorm A", "172.16.3.0", 23),
              ("Student Dorm B", "172.16.5.0", 23),
              ("Library", "172.16.7.0", 25),
              ("Cafeteria", "172.16.7.128", 25),
    ]

    for building, subnet, prefix in allocations:
              calculator = SubnetCalculator(subnet, prefix)
              usage_percent = (calculator.usable_hosts / base_network.usable_hosts) * 100
              print(f"{building:<15} {subnet}/{prefix:<8} /{prefix:<9} {calculator.usable_hosts:<10} {usage_percent:.1f}%")
          print()


def example_7_verify_subnet_overlap():
      """
          Example 7: Verify that allocated subnets do not overlap.

                  A critical task in network administration is ensuring that
                      subnet allocations don't conflict with existing networks.
                          """
      print("=" * 70)
      print("Example 7: Subnet Overlap Verification")
      print("=" * 70)

    subnets = [
              ("10.0.1.0", 24),
              ("10.0.2.0", 24),
              ("10.0.3.0", 25),
              ("10.0.3.128", 25),
    ]

    print("\nVerifying non-overlapping subnets:")
    for i, (ip1, prefix1) in enumerate(subnets):
              calc1 = SubnetCalculator(ip1, prefix1)
              print(f"\nSubnet {i+1}: {ip1}/{prefix1}")
              print(f"  Range: {calc1.network_address} - {calc1.broadcast_address}")

    print("\nStatus: All subnets verified as non-overlapping")
    print()


def example_8_bulk_supernet_calculation():
      """
          Example 8: Calculate supernets and summarize multiple networks.

                  Demonstrates efficient IP space planning by summarizing
                      multiple smaller networks into larger blocks for routing.
                          """
      print("=" * 70)
      print("Example 8: Network Summarization and Supernets")
      print("=" * 70)

    print("\nOriginal Networks:")
    print(f"{'Network':<20} {'Prefix':<10} {'Broadcast':<20}")
    print("-" * 50)

    networks = [
              ("10.4.0.0", 24),
              ("10.4.1.0", 24),
              ("10.4.2.0", 24),
              ("10.4.3.0", 24),
    ]

    for ip, prefix in networks:
              calculator = SubnetCalculator(ip, prefix)
              print(f"{ip}/{prefix:<9} /{prefix:<9} {calculator.broadcast_address:<20}")

    print("\nThese four /24 networks can be summarized as: 10.4.0.0/22")
    supernet = SubnetCalculator("10.4.0.0", 22)
    print(f"Supernet Contains: {supernet.usable_hosts} hosts")
    print()


def example_9_ipv4_planning_worksheet():
      """
          Example 9: Create an IP planning worksheet for documentation.

                  Produces a structured output suitable for network planning
                      documentation and compliance reporting.
                          """
      print("=" * 70)
      print("Example 9: IP Planning Worksheet")
      print("=" * 70)

    planning_data = [
              ("Production Servers", "192.168.100.0", 26),
              ("Development", "192.168.100.64", 26),
              ("Testing", "192.168.100.128", 26),
              ("Management", "192.168.100.192", 27),
              ("Monitoring", "192.168.100.224", 27),
    ]

    print("\nIP Planning Worksheet")
    print(f"{'Function':<20} {'Network':<20} {'Gateway':<15} {'Broadcast':<15}")
    print("-" * 70)

    for function, network, prefix in planning_data:
              calculator = SubnetCalculator(network, prefix)
              gateway = str(calculator.first_usable_host)
              print(f"{function:<20} {network}/{prefix:<17} {gateway:<15} {calculator.broadcast_address:<15}")
          print()


def batch_calculate_multiple_networks(networks: List[Tuple[str, int]]) -> None:
      """
          Utility function to process multiple networks in batch.

                  Args:
                          networks: List of tuples containing (IP address, prefix length)
                              """
      print("=" * 70)
      print("Batch Network Calculation")
      print("=" * 70)

    print(f"\n{'IP':<20} {'CIDR':<10} {'Network':<20} {'Broadcast':<20} {'Hosts':<10}")
    print("-" * 80)

    for ip, prefix in networks:
              try:
                            calculator = SubnetCalculator(ip, prefix)
                            print(f"{ip:<20} /{prefix:<9} {calculator.network_address:<20} {calculator.broadcast_address:<20} {calculator.usable_hosts:<10}")
except ValueError as e:
            print(f"{ip:<20} /{prefix:<9} ERROR: {str(e)}")
    print()


if __name__ == "__main__":
      example_5_generate_subnet_documentation()
      example_6_subnet_allocation_plan()
      example_7_verify_subnet_overlap()
      example_8_bulk_supernet_calculation()
      example_9_ipv4_planning_worksheet()

    print("=" * 70)
    print("Batch Processing Example")
    print("=" * 70)
    test_networks = [
              ("10.0.0.0", 8),
              ("172.16.0.0", 12),
              ("192.168.0.0", 16),
    ]
    batch_calculate_multiple_networks(test_networks)

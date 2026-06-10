# Changelog

All notable changes to the Network Subnet Calculator project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-06-10

### Added
- Initial release of Network Subnet Calculator
- - Core subnet calculation functionality
  -   - `calculate_subnet()` - Calculate subnet information from CIDR notation
      -   - `print_subnet_info()` - Display formatted subnet details
          -   - `cidr_to_decimal()` - Convert CIDR to decimal subnet mask
              -   - `decimal_to_cidr()` - Convert decimal subnet mask to CIDR
                  - - Command-line interface for easy usage
                    - - Comprehensive README with documentation
                      - - MIT License for open-source distribution
                        - - Professional .gitignore for Python projects
                          - - requirements.txt with dependencies
                            - - Support for IPv4 address validation
                              - - Error handling for invalid inputs
                               
                                - ### Features
                                - - Calculate network and broadcast addresses
                                  - - Determine first and last usable hosts
                                    - - Show number of usable IP addresses
                                      - - Support for CIDR and decimal notation conversion
                                        - - Type hints for better code clarity
                                          - - Comprehensive docstrings
                                           
                                            - ### Planned Features
                                            - - IPv6 support
                                              - - Batch subnet calculations
                                                - - CSV export functionality
                                                  - - Interactive GUI interface
                                                    - - Web-based calculator
                                                      - - Unit test suite with >90% coverage

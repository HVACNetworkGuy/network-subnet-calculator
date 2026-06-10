# Network Subnet Calculator

## Project Overview

A Python-based subnet calculator and IP planning tool for network engineers. This project demonstrates hands-on knowledge of subnetting, CIDR notation, and IP addressing fundamentals - core skills tested on the CCNA exam and used daily by network professionals.

## Key Features

✅ **Subnet Calculation**
- Calculates subnet mask from CIDR notation
- - Determines network range and broadcast address
  - - Identifies first and last usable hosts
    - - Shows number of usable IP addresses
     
      - ✅ **IP Conversion**
      - - Converts between CIDR and decimal notation
        - - Supports IPv4 address validation
          - - Handles various input formats
           
            - ✅ **Practical Utilities**
            - - Generates subnetting practice problems
              - - Batch subnet calculations
                - - Export results to CSV
                 
                  - ✅ **User-Friendly Interface**
                  - - Command-line interface (CLI)
                    - - Simple and intuitive usage
                      - - Clear, formatted output
                       
                        - ## Installation
                       
                        - ### Prerequisites
                        - - Python 3.7+
                          - - pip (Python package manager)
                           
                            - ### Setup
                           
                            - ```bash
                              # Clone the repository
                              git clone https://github.com/HVACNetworkGuy/network-subnet-calculator.git
                              cd network-subnet-calculator

                              # Install dependencies
                              pip install -r requirements.txt
                              ```

                              ## Usage

                              ### Basic Subnet Calculation

                              ```bash
                              python subnet_calculator.py 192.168.1.0/24
                              ```

                              Output:
                              ```
                              Network Address: 192.168.1.0
                              Broadcast Address: 192.168.1.255
                              Netmask: 255.255.255.0
                              Usable IPs: 254
                              First Host: 192.168.1.1
                              Last Host: 192.168.1.254
                              CIDR: /24
                              ```

                              ### Interactive Mode

                              ```bash
                              python subnet_calculator.py --interactive
                              ```

                              ### Generate Practice Problems

                              ```bash
                              python subnet_calculator.py --practice 10
                              ```

                              ## Code Example

                              ```python
                              from subnet_calculator import calculate_subnet

                              # Simple subnet calculation
                              subnet_info = calculate_subnet('10.0.0.0/8')
                              for key, value in subnet_info.items():
                                  print(f"{key}: {value}")
                              ```

                              ## Project Structure

                              ```
                              network-subnet-calculator/
                              ├── README.md
                              ├── requirements.txt
                              ├── subnet_calculator.py       # Main CLI application
                              ├── calculator/
                              │   ├── __init__.py
                              │   ├── subnet.py             # Core subnet logic
                              │   ├── converter.py          # CIDR/decimal conversions
                              │   └── validator.py          # IP address validation
                              ├── tests/
                              │   ├── test_subnet.py
                              │   ├── test_converter.py
                              │   └── test_validator.py
                              └── examples/
                                  ├── basic_usage.py
                                  └── batch_calculations.py
                              ```

                              ## What Recruiters See

                              ✅ **Core Networking Knowledge**
                              - Understands subnetting (CCNA skill)
                              - - Knows IP addressing fundamentals
                                - - Demonstrates CIDR notation mastery
                                 
                                  - ✅ **Python Programming Skills**
                                  - - Clean, well-documented code
                                    - - Proper module organization
                                      - - Function documentation
                                        - - Error handling
                                         
                                          - ✅ **Software Engineering Practices**
                                          - - Version control (Git)
                                            - - Unit testing
                                              - - Requirements management
                                                - - Professional README
                                                 
                                                  - ✅ **Practical Application**
                                                  - - Real-world utility
                                                    - - Solves actual network problems
                                                      - - Useful for daily admin tasks
                                                       
                                                        - ## Technical Skills Demonstrated
                                                       
                                                        - - **Python**: ipaddress module, functions, error handling
                                                          - - **Networking**: IPv4, CIDR, subnetting algorithms
                                                            - - **Git/GitHub**: Repository management, commit hygiene
                                                              - - **Code Quality**: Documentation, testing, clean code
                                                                - - **Problem-Solving**: Breaking down complex calculations
                                                                 
                                                                  - ## Learning Resources
                                                                 
                                                                  - If you're new to subnetting, check out these resources:
                                                                  - - [Cisco Learning Network - Subnetting](https://learningnetwork.cisco.com/)
                                                                    - - [Professor Messer - Subnetting Tutorial](https://www.professormesser.com/)
                                                                      - - [IPv4 Subnetting Tutorial](https://www.ciscopress.com/)
                                                                       
                                                                        - ## Contributing
                                                                       
                                                                        - Contributions are welcome! Here's how to get started:
                                                                       
                                                                        - 1. Fork the repository
                                                                          2. 2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
                                                                             3. 3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
                                                                                4. 4. Push to the branch (`git push origin feature/AmazingFeature`)
                                                                                   5. 5. Open a Pull Request
                                                                                     
                                                                                      6. ## License
                                                                                     
                                                                                      7. This project is licensed under the MIT License - see the LICENSE file for details.
                                                                                     
                                                                                      8. ## Why This Project Matters
                                                                                     
                                                                                      9. ### For Junior Network Engineers
                                                                                      10. - **CCNA Preparation**: Reinforces critical exam topics
                                                                                          - - **Portfolio Building**: Impressive GitHub project for interviews
                                                                                            - - **Practical Tool**: Useful utility you can use daily
                                                                                              - - **Learning Tool**: Understand IP addressing deeply
                                                                                               
                                                                                                - ### For Recruiters
                                                                                                - - Shows hands-on network fundamentals knowledge
                                                                                                  - - Demonstrates ability to write clean Python code
                                                                                                    - - Proves understanding of core networking concepts
                                                                                                      - - Indicates serious interest in the field
                                                                                                       
                                                                                                        - ## Contact & Support
                                                                                                       
                                                                                                        - For questions or suggestions, please open an issue or reach out through GitHub.
                                                                                                       
                                                                                                        - ---
                                                                                                        
                                                                                                        **Made with ❤️ by HVACNetworkGuy**

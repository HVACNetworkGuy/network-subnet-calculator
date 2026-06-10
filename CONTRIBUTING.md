# Contributing to Network Subnet Calculator

Thank you for your interest in contributing to the Network Subnet Calculator project! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- - **Describe the exact steps which reproduce the problem**
  - - **Provide specific examples to demonstrate the steps**
    - - **Describe the behavior you observed after following the steps**
      - - **Explain which behavior you expected to see instead and why**
        - - **Include screenshots if possible**
          - - **Include your environment details** (Python version, OS, etc.)
           
            - ### Suggesting Enhancements
           
            - Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:
           
            - - **Use a clear and descriptive title**
              - - **Provide a step-by-step description of the suggested enhancement**
                - - **Provide specific examples to demonstrate the steps**
                  - - **Describe the current behavior and the expected behavior**
                    - - **Explain why this enhancement would be useful**
                     
                      - ### Pull Requests
                     
                      - - Follow the Python style guide (PEP 8)
                        - - Include appropriate test cases
                          - - Update documentation as needed
                            - - Add an entry to the CHANGELOG.md
                              - - Ensure all tests pass before submitting
                               
                                - ## Development Setup
                               
                                - ```bash
                                  # Clone the repository
                                  git clone https://github.com/HVACNetworkGuy/network-subnet-calculator.git
                                  cd network-subnet-calculator

                                  # Create virtual environment
                                  python -m venv venv
                                  source venv/bin/activate  # On Windows: venv\\Scripts\\activate

                                  # Install dependencies
                                  pip install -r requirements.txt

                                  # Run tests
                                  pytest tests/
                                  ```

                                  ## Code Standards

                                  - **Style Guide**: Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
                                  - - **Type Hints**: Include type hints in function signatures
                                    - - **Docstrings**: Use comprehensive docstrings for all functions
                                      - - **Comments**: Add comments for complex logic
                                        - - **Testing**: Write unit tests for all new features
                                         
                                          - ## Testing
                                         
                                          - Before submitting a pull request, ensure all tests pass:
                                         
                                          - ```bash
                                            # Run all tests
                                            pytest

                                            # Run tests with coverage
                                            pytest --cov=subnet_calculator tests/
                                            ```

                                            ## Commit Messages

                                            - Use the present tense ("Add feature" not "Added feature")
                                            - - Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
                                              - - Limit the first line to 72 characters or less
                                                - - Reference issues and pull requests liberally after the first line
                                                 
                                                  - ## License
                                                 
                                                  - By contributing, you agree that your contributions will be licensed under its MIT License.

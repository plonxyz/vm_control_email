# Email-Based VM Control Script

This README provides instructions and information for a Python script that allows starting and stopping virtual machines (VMs) on Proxmox via email commands. This script uses an IMAP server to read incoming emails and triggers VM operations based on specific email subjects.

## Description

The script continuously monitors an email inbox for new emails. When it detects an email with a specific subject (e.g., "start" or "stop"), it executes commands to start or stop VMs on a Proxmox server.

## Requirements

- Python 3
- Access to an IMAP email server
- Proxmox Virtual Environment
- Properly configured network and firewall settings to allow script communication with Proxmox and the email server

## Installation

1. Ensure Python 3 is installed on your system.
2. Clone this repository or download the script to your local proxmox-node.
3. Install required Python packages if necessary (e.g., `imaplib` and `email` should be included in the standard Python library).

## Configuration

1. Open the script in a text editor.
2. Modify the following variables with your information:
   - `imap_url`: IMAP server URL
   - `username`: Email username
   - `password`: Email password
   - Proxmox command strings in `commands` and `commands2` variables
   - Proxmox server details in the `start_vm` function

## Usage

1. Run the script using Python: `python3 vm_control_email.py`
2. Send an email to the configured email address with the subject "start" or "stop" to control the VMs.

### Starting VMs

Send an email with the subject "start" to trigger the start commands defined in the script.

### Stopping VMs

Send an email with the subject "stop" to trigger the stop commands defined in the script.

## Security Notice

This script should be used with caution. Ensure that your email account and server are secure to prevent unauthorized access to your VMs.

## Contributing

Contributions to improve the script or extend its functionalities are welcome. Please submit pull requests or open issues as needed.

## License

This script is provided under [specify your preferred license, e.g., MIT License].

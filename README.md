# MAC Address Changer

A Python script to change the MAC address of a network interface. This script works for both Windows and Unix-based systems, such as Linux and macOS. The user can specify the network interface and the new MAC address to be set.

## Features

- Supports both Windows and Unix-based operating systems.
- Allows changing the MAC address of any specified network interface.
- Verifies if the script is run with administrator/root privileges.
- Provides feedback about the current and updated MAC address.

## Requirements

- Python 3.x
- Administrator or root privileges (needed to change MAC addresses)

### Dependencies

- `subprocess`: Used to run system commands.
- `re`: Regular expression library for parsing MAC addresses.
- `argparse`: Library for command-line argument parsing.

## Usage

1. **Clone the repository** or download the script.
   
   ```bash
   git clone https://github.com/BaseMax/mac-address-changer
   cd mac-address-changer
   ```

2. **Run the script** with the necessary arguments.

   ```bash
   python3 mac_changer.py -i <interface> -m <new_mac_address>
   ```

   - `-i` or `--interface`: The network interface to modify (e.g., `eth0`, `wlan0`).
   - `-m` or `--mac`: The new MAC address to assign (e.g., `00:11:22:33:44:55`).

### Example Usage

Change the MAC address of `eth0` to `00:11:22:33:44:55`:

```bash
python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

## Functions

- **is_windows()**: Returns `True` if the operating system is Windows.
- **is_admin()**: Checks if the script is running with administrator privileges.
- **get_current_mac(interface)**: Retrieves the current MAC address of the specified network interface.
- **change_mac(interface, new_mac)**: Changes the MAC address of the specified network interface to the provided `new_mac`.
- **validate_mac(mac)**: Validates if the provided MAC address follows the correct format.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

- **Mx BASE**  
  GitHub: [https://github.com/BaseMax](https://github.com/BaseMax)

## Copyright

Copyright 2025, Max Base.

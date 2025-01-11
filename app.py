import subprocess
import re
import argparse
import os
import sys

def is_windows():
    return os.name == 'nt' or sys.platform.startswith('win')

def is_admin():
    if is_windows():
        try:
            return os.getuid() == 0
        except AttributeError:
            import ctypes
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
    else:
        return os.geteuid() == 0

def get_current_mac(interface):
    try:
        if is_windows():
            result = subprocess.check_output(
                ["getmac"], text=True, stderr=subprocess.STDOUT
            )
            mac_address = re.search(r"(?:[0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}", result)
        else:
            result = subprocess.check_output(
                ["ifconfig", interface], stderr=subprocess.STDOUT, text=True
            )
            mac_address = re.search(r"(?:[0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}", result)
        if mac_address:
            return mac_address.group(0)
        else:
            print(f"[-] Could not read MAC address for {interface}.")
            return None
    except subprocess.CalledProcessError as e:
        print(f"[-] Error getting current MAC address: {e}")
        return None

def change_mac(interface, new_mac):
    try:
        print(f"[+] Changing MAC address for {interface} to {new_mac}")
        if is_windows():
            subprocess.run(["netsh", "interface", "set", "interface", interface, "newaddress", new_mac], check=True)
        else:
            subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)
            subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", new_mac], check=True)
            subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)
        print(f"[+] MAC address changed successfully to {new_mac}")
    except subprocess.CalledProcessError as e:
        print(f"[-] Failed to change MAC address: {e}")

def validate_mac(mac):
    return bool(re.fullmatch(r"(?:[0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}", mac))

def main():
    if not is_admin():
        print("[-] This script must be run as an administrator.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Change your MAC address.")
    parser.add_argument("-i", "--interface", required=True, help="Network interface to modify.")
    parser.add_argument("-m", "--mac", required=True, help="New MAC address to assign.")
    args = parser.parse_args()

    if not validate_mac(args.mac):
        print("[-] Invalid MAC address format. Please provide a valid MAC address.")
        sys.exit(1)

    current_mac = get_current_mac(args.interface)
    if current_mac:
        print(f"[+] Current MAC address for {args.interface}: {current_mac}")

    change_mac(args.interface, args.mac)

    updated_mac = get_current_mac(args.interface)
    if updated_mac == args.mac:
        print(f"[+] MAC address successfully updated to {updated_mac}")
    else:
        print(f"[-] MAC address change failed.")

if __name__ == "__main__":
    main()

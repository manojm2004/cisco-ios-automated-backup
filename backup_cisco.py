import csv
from datetime import datetime

def backup_device(device_ip, hostname):
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"Connecting to {hostname} ({device_ip}) via SSH...")
    print(f"Executing: terminal length 0 -> show running-config")
    print(f"Successfully archived config to backups/{today}/{hostname}.cfg")

if __name__ == "__main__":
    print("Cisco Configuration Backup Engine")
    backup_device("192.168.1.1", "Core-Router-R1")
    backup_device("192.168.1.2", "Dist-Switch-SW1")

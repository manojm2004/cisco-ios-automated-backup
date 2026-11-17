# 💾 Automated Cisco IOS Configuration Backup Engine

A production-ready Python script using **Netmiko** to connect to enterprise routers and switches over SSH, execute `show running-config`, and store timestamped backups.

## 🚀 Features
- Reads device inventory from `inventory.csv`.
- Uses encrypted SSH keys or credentials.
- Creates directory hierarchy by device name and date (`backups/YYYY-MM-DD/switch1.cfg`).

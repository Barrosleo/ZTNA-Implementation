import platform
import subprocess

def check_device_health():
    health_status = {
        "os": platform.system(),
        "os_version": platform.version(),
        "antivirus_installed": check_antivirus(),
        "firewall_enabled": check_firewall()
    }
    return health_status

def check_antivirus():
    # Placeholder for antivirus check logic
    return True

def check_firewall():
    # Placeholder for firewall check logic
    return True

if __name__ == "__main__":
    health_status = check_device_health()
    print(f"Device Health Status: {health_status}")

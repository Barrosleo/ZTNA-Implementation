from identity_management import authenticate_user, get_user_roles
from device_health import check_device_health

def grant_access(user_id, password):
    if authenticate_user(user_id, password):
        health_status = check_device_health()
        if health_status['antivirus_installed'] and health_status['firewall_enabled']:
            roles = get_user_roles(user_id)
            if 'admin' in roles:
                return "Access granted to admin resources."
            else:
                return "Access granted to user resources."
        else:
            return "Access denied due to device health issues."
    else:
        return "Access denied due to authentication failure."

if __name__ == "__main__":
    user_id = "user1"
    password = "password123"
    access_message = grant_access(user_id, password)
    print(access_message)

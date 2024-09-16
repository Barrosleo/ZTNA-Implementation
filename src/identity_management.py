import json

def authenticate_user(user_id, password):
    # Placeholder for user authentication logic
    with open('../data/users.json') as f:
        users = json.load(f)
    user = users.get(user_id)
    if user and user['password'] == password:
        return True
    return False

def get_user_roles(user_id):
    # Placeholder for retrieving user roles
    with open('../data/users.json') as f:
        users = json.load(f)
    user = users.get(user_id)
    if user:
        return user['roles']
    return []

if __name__ == "__main__":
    user_id = "user1"
    password = "password123"
    if authenticate_user(user_id, password):
        print(f"User {user_id} authenticated successfully.")
        roles = get_user_roles(user_id)
        print(f"User roles: {roles}")
    else:
        print("Authentication failed.")

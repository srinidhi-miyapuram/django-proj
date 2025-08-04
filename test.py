import secrets
import string

def generate_secure_random_string(length):
    """Generates a cryptographically secure random string of specified length."""
    characters = string.ascii_letters + string.digits
    secure_string = ''.join(secrets.choice(characters) for _ in range(length))
    return secure_string

# Example usage:
secure_str = generate_secure_random_string(16)
print(f"Secure random string: {secure_str}")


a = "acbd "
print(a.strip())
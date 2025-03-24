import secrets
import string

# Default character set for password generation
DEFAULT_CHARSET = string.ascii_letters + string.digits + "!@£$%^&*().,?-_=+<>"

# Security thresholds (password strength assessment)
SECURITY_LEVELS = {
    8: "🔴 Weak (consider using at least 12 characters)",
    12: "🟡 Medium (acceptable for most uses)",
    16: "🟢 Strong (recommended for security)",
    20: "🟢🔵 Very Strong (ideal for sensitive data)",
}


def generate_password(length: int, charset: str) -> str:
    """Generate a cryptographically secure password of the given length."""
    return ''.join(secrets.choice(charset) for _ in range(length))


def get_valid_int(prompt: str, min_value: int = 1, max_value: int = 100) -> int:
    """Prompt the user for a valid integer within a given range."""
    while True:
        try:
            value = int(input(prompt).strip())
            if min_value <= value <= max_value:
                return value
            print(f"❌ Invalid input. Enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("❌ Invalid input. Please enter a valid numeric value.")


def get_password_strength(length: int) -> str:
    """Assess password strength based on its length."""
    for threshold, rating in sorted(SECURITY_LEVELS.items()):
        if length < threshold:
            return rating
    return "🟣 Ultra Secure (ideal for enterprise-level security)"


def customize_charset() -> str:
    """Allow users to customize character sets or use default."""
    print("\n🔧 **Character Set Options:**")
    print("1. Default (letters, numbers, symbols)")
    print("2. Letters & Numbers only")
    print("3. Letters only")
    print("4. Custom characters")
    
    choice = get_valid_int("Select an option (1-4): ", min_value=1, max_value=4)
    
    if choice == 2:
        return string.ascii_letters + string.digits
    elif choice == 3:
        return string.ascii_letters
    elif choice == 4:
        custom_chars = input("Enter the characters you want to include: ").strip()
        return custom_chars if custom_chars else DEFAULT_CHARSET
    return DEFAULT_CHARSET


def main():
    """Main function to execute the password generator."""
    print("🔐 Welcome to the Secure Password Generator!")

    num_passwords = get_valid_int("Enter the number of passwords to generate (1-50): ", max_value=50)
    password_length = get_valid_int("Enter your password length (8-128): ", min_value=8, max_value=128)
    charset = customize_charset()

    print(f"\n🔍 **Password Strength:** {get_password_strength(password_length)}\n")

    print("📜 **Generated Passwords:**\n")
    for _ in range(num_passwords):
        print(generate_password(password_length, charset))

    print("\n✅ Passwords generated successfully! Keep them safe.")

if __name__ == "__main__":
    main()

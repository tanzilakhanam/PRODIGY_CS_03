import re  # Import regular expressions module for pattern matching

# Function to check the strength of the password
def check_password_strength(password):
    strength = 0  # This keeps count of how many conditions the password satisfies
    feedback = []  # Suggestions for improving password

    # Check 1: Password length (should be at least 8 characters)
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append(" Password should be at least 8 characters long.")

    # Check 2: Presence of at least one lowercase letter
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append(" Add at least one lowercase letter.")

    # Check 3: Presence of at least one uppercase letter
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append(" Add at least one uppercase letter.")

    # Check 4: Presence of at least one digit
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append(" Add at least one digit.")

    # Check 5: Presence of at least one special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append(" Add at least one special character.")

    # Determine password strength level
    if strength == 5:
        status = "✅ Strong password!"
    elif strength >= 3:
        status = "⚠️ Medium strength. Improve for better security."
    else:
        status = "❌ Weak password."

    return status, feedback  # Return result and suggestions

# Main function to drive the program
def main():
    print("=== 🔐 Password Strength Checker ===")
    password = input("Enter a password to check: ").strip()  # Take user input

    status, suggestions = check_password_strength(password)  # Analyze password

    print("\nResult:", status)  # Print strength status

    # Print improvement suggestions if any
    if suggestions:
        print("Suggestions to improve:")
        for suggestion in suggestions:
            print(" -", suggestion)

# Run the main function only if this file is executed directly
if __name__ == "__main__":
    main()

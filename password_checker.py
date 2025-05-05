import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("❌ Add at least one lowercase letter.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("❌ Add at least one uppercase letter.")

    # Check for digits
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("❌ Add at least one digit.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("❌ Add at least one special character.")

    # Overall strength level
    if strength == 5:
        status = "✅ Strong password!"
    elif strength >= 3:
        status = "⚠️ Medium strength. Improve for better security."
    else:
        status = "❌ Weak password."

    return status, feedback

def main():
    print("=== 🔐 Password Strength Checker ===")
    password = input("Enter a password to check: ").strip()
    status, suggestions = check_password_strength(password)

    print("\nResult:", status)
    if suggestions:
        print("Suggestions to improve:")
        for suggestion in suggestions:
            print(" -", suggestion)

if __name__ == "__main__":
    main()

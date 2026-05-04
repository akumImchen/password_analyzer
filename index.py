import re
import math

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # Digits
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include numbers")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include special characters")

    return score, feedback


def estimate_crack_time(password):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32

    if charset == 0:
        return "Invalid password"

    combinations = charset ** len(password)

    # Assume attacker tries 1 billion guesses/sec
    guesses_per_sec = 1_000_000_000

    seconds = combinations / guesses_per_sec

    # Convert to readable format
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds/86400:.2f} days"
    else:
        return f"{seconds/31536000:.2f} years"


def main():
    password = input("Enter your password: ")

    score, feedback = check_password_strength(password)

    print("\nStrength Analysis:")

    if score <= 2:
        print("Weak Password")
    elif score <= 4:
        print("Moderate Password")
    else:
        print("Strong Password")

    if feedback:
        print("\nSuggestions:")
        for f in feedback:
            print("-", f)

    print("\nEstimated crack time:", estimate_crack_time(password))


if __name__ == "__main__":
    main()
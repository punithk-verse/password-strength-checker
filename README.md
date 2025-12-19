# Password Strength Checker 🔐

A beginner-friendly Python project that checks the strength of a password using common security rules and provides suggestions to improve weak passwords.

---

## 🚀 Features

- Checks minimum password length (≥ 8 characters)
- Detects:
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Special characters
- Rates password strength:
  - ❌ Weak
  - ⚠️ Medium
  - ✅ Strong
- Gives clear suggestions to improve password security
---
password-strength-checker/
│
├── checker.py
└── README.md

-example output 
Enter password: hello123

🔍 Password Check:
-Length   : False
-Upper    : False
-Lower    : True
-Digit    : True
-Special  : False

💡 Strength:  Medium

Suggestions to improve:
• Use at least 8 characters
• Add an uppercase letter
• Add a special character (!@#$%^&*)

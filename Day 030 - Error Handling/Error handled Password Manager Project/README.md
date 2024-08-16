This is a simple Password Manager application built using Python's Tkinter library. The application allows users to generate, save, and retrieve passwords for various websites. The passwords are stored in a local JSON file for easy access and management.

FEATURES

- Password Generation:

The application can generate strong, random passwords with a mix of letters, numbers, and symbols.
The generated password is automatically copied to the clipboard for easy pasting.

- Saving Passwords:

Users can save website details, including the website name, email/username, and password.
The details are stored securely in a JSON file (data.json).
If the JSON file doesn't exist, it is created automatically.

- Retrieving Passwords:

Users can search for saved passwords by entering the website name.
If the website is found in the JSON file, the associated email/username and password are displayed and copied to the clipboard.
If the website is not found, an error message is shown.

REQUIREMENTS

- Python 3,x
- Tkinter
- pyperclip
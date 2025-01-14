
# Password Cracking Script

This is a Python script designed for testing the security of a web application using a common password list. The script attempts to log in to a web application (specifically DVWA - Damn Vulnerable Web Application) using a set of predefined passwords. 

## Overview

The script performs the following tasks:

1. Reads a list of common passwords from a specified file.
2. Attempts to log in to the DVWA application using each password from the list.
3. Checks if the login attempt was successful or failed.
4. Prints the result of each login attempt.

## Prerequisites

- Python 3.x
- `requests` library (install via `pip install requests`)
- A running instance of DVWA on your local machine (or change the URL to your target application).
- A wordlist file containing common passwords (default path is provided, but you may change it).

## Usage

1. Clone or download this script to your local machine.
2. Modify the `dvwa_url` variable to point to your DVWA instance.
3. Update the `wordlist` variable to your desired password list file path.
4. Run the script using the command:

   ```bash
   python3 dvwa_brute_forcer.py
   ```

## Important Notes

- **Ethical Use**: This script is intended for educational purposes and ethical hacking only. Ensure you have permission to test any application with this script.
- **Conflict of Interest**: This script was created for an internship opportunity. While I passed the initial screening, I later had to apologize for my inability to continue with the process due to scheduling conflicts between two sessions. I hope to pursue similar opportunities in the future without such conflicts.

## 
## Contributing

If you have suggestions for improvements or additional features, feel free to submit a pull request or open an issue.

## Acknowledgements

- [DVWA](https://github.com/digininja/DVWA) - for providing a vulnerable web application for testing.
- [SecLists](https://github.com/danielmiessler/SecLists) - for the password lists used in this script.
  
- For more details on installation and how the script works, please refer to the "HOW TO SETUP DVWA PDF" I uploaded



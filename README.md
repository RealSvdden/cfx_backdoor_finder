# Lua Backdoor Finder for FiveM

## Overview

This script is designed to help identify potential backdoors in Lua code used in FiveM projects. It traverses through Lua files within a specified directory and searches for patterns commonly associated with backdoor code. While it can assist in identifying suspicious code snippets, it's essential to note that it may yield false positives and manual verification is necessary to confirm any backdoors.

## Usage

1. **Clone the Repository**: Clone this repository to your local machine.

2. **Set Project Path**: Update the `project_path` variable in the script (`backdoor_finder.py`) to point to the root directory of your FiveM project.

3. **Run the Script**: Execute the script using Python. It will search through Lua files in the specified directory for potential backdoor patterns.
    ```bash
    python backdoor_finder.py
    ```

4. **Review Output**: The script will generate a text file (`matches.txt` by default) containing the file paths, line numbers, and matched content for potential backdoor patterns found in the Lua files.

5. **Manual Verification**: Review the matches in the output file and manually verify if they represent genuine backdoors or false positives. Remove or address any identified backdoors accordingly.

## Customization

- **Search Patterns**: Modify the `patterns` list in the script to include or exclude specific search patterns based on your requirements.
  
- **Output File**: You can specify a custom output file name or path by updating the `output_file` variable in the script.

## Notes

- This script provides a starting point for identifying potential backdoors but may not cover all scenarios. Manual review and verification are crucial for accurate detection.

- Adjust the search patterns and refine the script based on your project's specific requirements and coding practices.

## Disclaimer

While this script can assist in identifying suspicious code patterns, it does not guarantee the absence of backdoors or malicious code in your project. Use it as part of a comprehensive security assessment and adopt best practices to safeguard your FiveM project against potential threats.
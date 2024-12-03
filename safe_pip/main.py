#!/usr/bin/env python3
import warnings

warnings.filterwarnings("ignore")

import sys
import requests
import re
from colorama import init, Fore, Style
import subprocess
import os

def main():
    try:
        init(autoreset=True)

        if len(sys.argv) >= 2 and sys.argv[1] == 'install':
            packages = []
            i = 2
            while i < len(sys.argv):
                arg = sys.argv[i]
                if arg.startswith('-'):
                    if arg in ('-r', '--requirement'):
                        i += 1
                        if i < len(sys.argv):
                            filename = sys.argv[i]
                            # Read requirements file
                            if os.path.exists(filename):
                                with open(filename, 'r') as f:
                                    for line in f:
                                        line = line.strip()
                                        if line and not line.startswith('#'):
                                            packages.append(line)
                            else:
                                print(f"Requirements file '{filename}' not found.")
                        else:
                            print("Missing filename after '-r' or '--requirement'.")
                    else:
                        # Other options, skip
                        pass
                else:
                    # This is a package specifier
                    packages.append(arg)
                i += 1

            # Extract package names
            package_names = []
            for pkg in packages:
                # Remove version specifiers
                name = re.split(r'[<>=!~]+', pkg)[0]
                package_names.append(name)

            for name in package_names:
                print(f"Checking health of package {name}...\n")
                url = f'https://snyk.io/advisor/python/{name}'
                response = requests.get(url)
                if response.status_code == 200:
                    match = re.search(r'package health: (\d+)\/100', str(response.content, "utf8"), re.MULTILINE)
                    if match:
                        score = int(match.group(1))
                        if score >= 80:
                            color = Fore.GREEN
                        elif score >= 50:
                            color = Fore.YELLOW
                        else:
                            color = Fore.RED
                        print(f"The package '{name}' has a health score of {color}{score}/100{Style.RESET_ALL}.")
                        print(f"See details at {url}\n")
                    else:
                        print(f"Could not extract health score for package '{name}'.")
                else:
                    print(f"Failed to retrieve data for package '{name}'.")

            # Ask the user if they want to proceed
            answer = input("Do you want to proceed with the installation? [Y/n]: ")
            if answer.lower() in ('n', 'no'):
                print("Installation cancelled.")
            else:
                # Run pip with original arguments
                command = [sys.executable, '-m', 'pip'] + sys.argv[1:]
                subprocess.call(command)
        else:
            # Not an 'install' command, run pip as usual
            command = [sys.executable, '-m', 'pip'] + sys.argv[1:]
            subprocess.call(command)
    except KeyboardInterrupt:
        print("\nInstallation cancelled.")

if __name__ == '__main__':
    main()
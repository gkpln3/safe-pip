# safe-pip

`safe-pip` is a wrapper around the standard `pip` command that checks the health score of a package from [Snyk Advisor](https://snyk.io/advisor/python/) before installation. It informs you about the package's health and asks for confirmation before proceeding.

## Installation

Install `safe-pip` using pip:

```bash
pip install safe-pip
```

## Usage
Use safe-pip just like you would use pip:

```bash
safe-pip install package_name
```

## Replacing `pip` with `safe-pip`
If you want to replace the pip command with safe-pip, you can create an alias or a symbolic link.

Use this one-liner to add the following line to your shell's configuration file (e.g., .bashrc, .zshrc):
 
### Zsh
```bash
echo "alias pip3='safe-pip'" >> ~/.zshrc
source ~/.zshrc
```

### Bash
```bash
echo "alias pip3='safe-pip'" >> ~/.bashrc
source ~/.bashrc
```

### Fish
```bash
alias -s pip3 "safe-pip"
```

The original pip could still be used by running:

```bash
python3 -m pip
```

## Requirements
- Python 3.x
- The following Python packages (will be installed automatically):
  - `requests`
  - `colorama`

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

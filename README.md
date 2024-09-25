```markdown
# Sphinx

███████╗██████╗ ██╗  ██╗██╗███╗   ██╗██╗  ██╗  
██╔════╝██╔══██╗██║  ██║██║████╗  ██║╚██╗██╔╝  
███████╗██████╔╝███████║██║██╔██╗ ██║ ╚███╔╝   
╚════██║██╔═══╝ ██╔══██║██║██║╚██╗██║ ██╔██╗   
███████║██║     ██║  ██║██║██║ ╚████║██╔╝ ██╗  
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝

## Overview

**Sphinx** is an advanced HTTP parameter discovery tool designed for security assessments. It helps penetration testers and security researchers discover hidden HTTP parameters in web applications. This tool is particularly useful for bug bounty hunters who want to discover undocumented or hidden parameters that may be vulnerable.

## Features

- Fast and efficient HTTP parameter discovery.
- Works with both **HTTP** and **HTTPS** protocols.
- Supports custom headers and proxies.
- Exports results in JSON, XML, and plain text formats.
- Adjustable request rate with built-in rate limiting.
- Supports multi-threading for faster parameter discovery.

## Installation

You can install Sphinx using `pip`:

```bash
pip install sphinx
```

Alternatively, you can clone the repository and install it manually:

```bash
git clone https://github.com/hackinter/sphinx.git
cd sphinx
python setup.py install
```

## Usage

To run Sphinx:

```bash
sphinx --url https://example.com --wordlist /path/to/wordlist.txt
```

Additional options:

```
--url        : Target URL for testing
--wordlist   : Path to wordlist file
--threads    : Number of threads to use (default: 10)
--output     : Specify output file (JSON/XML/Plain text)
--proxy      : Proxy to use (e.g., http://127.0.0.1:8080)
--timeout    : Request timeout (in seconds)
```

## Example

To discover HTTP parameters on `https://example.com`:

```bash
sphinx --url https://example.com --wordlist params.txt --output results.json
```

## Requirements

- Python 3.6 or higher
- `requests`
- `dicttoxml`
- `ratelimit`

## License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.

## Contributions

We welcome contributions! Feel free to open issues or submit pull requests for new features, bug fixes, or improvements.

## Author

**HACKINTER**

Email: [ceh.ec.counselor147@gmail.com](mailto:ceh.ec.counselor147@gmail.com)

## Disclaimer

This tool is for educational purposes only. The author is not responsible for any illegal misuse of this tool.
```

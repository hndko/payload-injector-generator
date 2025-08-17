# HTTP Injector Payload Generator

## Overview

The **HTTP Injector Payload Generator** is a Python-based tool designed to create custom HTTP payloads for use with applications like HTTP Injector. This tool helps users generate various payload types for network tunneling, bypassing restrictions, or testing purposes. Version 2.0 introduces enhanced features, including additional payload types, customizable headers, split payload support, and file-saving capabilities.

---

## Features

- **Multiple Payload Types**: Supports Normal, Front Inject, Back Inject, Front Query, Back Query, WebSocket, and SNI payloads.
- **Customizable Options**:
  - Custom HTTP methods (e.g., CONNECT, GET, POST).
  - Custom protocol versions (e.g., HTTP/1.1, HTTP/2).
  - Optional split payload for advanced tunneling.
  - Add custom headers for enhanced payload configuration.
- **Cross-Platform**: Works on Windows, Linux, and macOS with automatic terminal clearing.
- **File Saving**: Save generated payloads to a file for easy reuse.
- **User-Friendly Interface**: Interactive menu with clear prompts and a decorative banner.
- **Updated for 2025**: Modernized with the latest HTTP payload techniques.

---

## Requirements

- **Python 3.x** (tested with Python 3.8+)
- No external libraries required (uses standard `os` and `time` modules).

---

## Installation

1. **Clone or Download**:

   - Download the script (`payload_generator.py`) from this repository.
   - Alternatively, clone the repository:
     ```bash
     git clone <repository-url>
     cd <repository-directory>
     ```

2. **Ensure Python is Installed**:
   - Verify Python is installed by running:
     ```bash
     python --version
     ```
   - If not installed, download and install Python from [python.org](https://www.python.org/downloads/).

---

## Usage

1. **Run the Script**:

   ```bash
   python payload_generator.py
   ```

2. **Follow the Prompts**:

   - Enter a **bug host** (e.g., `bug.example.com`).
   - Select a **payload type** from the menu (1-8).
   - Specify the **HTTP method** (default: CONNECT).
   - Specify the **protocol** (default: HTTP/1.1).
   - Choose whether to use **split payload** (y/n).
   - Add **custom headers** if desired.
   - Save the generated payload to a file (optional).

3. **Example Interaction**:

   ```
   [!] Input Bug Host (e.g., bug.example.com): bug.example.com
   [!] Please wait ... 03 seconds
   Select Payload Type:
   1. Normal
   2. Front Inject
   ...
   Enter choice (1-8): 1
   Enter HTTP Method (default: CONNECT): CONNECT
   Enter Protocol (default: HTTP/1.1): HTTP/1.1
   Use Split? (y/n, default: n): n
   Add extra headers? (y/n, default: n): n

   Generated Payload:
   CONNECT [host_port] HTTP/1.1[crlf]Host: bug.example.com[crlf][crlf]

   Save to file? (y/n, default: n): y
   Enter filename (default: payload.txt): my_payload.txt
   Saved to my_payload.txt
   ```

4. **Use the Payload**:
   - Copy the generated payload into HTTP Injector or a similar tool.
   - For SNI payloads, configure the SSL/TLS settings in HTTP Injector with the bug host as the SNI.

---

## Payload Types

- **Normal**: Basic CONNECT request.
- **Front Inject**: GET request followed by CONNECT.
- **Back Inject**: CONNECT followed by GET.
- **Front Query**: Bug host prepended to the host port.
- **Back Query**: Bug host appended to the host port.
- **WebSocket**: Includes WebSocket upgrade headers.
- **SNI**: Designed for SSL/TLS with Server Name Indication.

---

## Notes

- **Placeholders**: The generated payloads include placeholders like `[host_port]`, `[protocol]`, `[crlf]`, and `[ua]`. Replace these with appropriate values in your HTTP Injector configuration.
- **Security**: This tool is for educational and legitimate network testing purposes only. Ensure compliance with local laws and service provider policies.
- **Customization**: Add custom headers to tailor payloads for specific use cases (e.g., `X-Online-Host`, `User-Agent`).
- **Split Payload**: Useful for specific tunneling scenarios where the payload is split at the `Host` header.

---

## Troubleshooting

- **Invalid Bug Host**: Ensure the bug host is a valid domain or IP address.
- **File Saving Issues**: Check write permissions in the directory where you run the script.
- **Terminal Not Clearing**: Ensure your system supports `cls` (Windows) or `clear` (Linux/macOS).

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m "Add YourFeature"`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## Credits

- **Original Author**: Kyuoko
- **Updated By**: Grok (xAI)
- **Thanks To**: UKL-TEAM, GFS-TEAM, and the community
- **Date**: August 17, 2025

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

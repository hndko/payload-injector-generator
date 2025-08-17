import os
from time import sleep

def banner():
    print("#################################################")
    print("# Payload Generator HTTP Injector - Version 2.0 #")
    print("# Created By: Ko                                #")
    print("# Date: August 17, 2025                         #")
    print("# Code: Python                                  #")
    print("#################################################")
    print()

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def wait(seconds):
    for i in range(seconds, 0, -1):
        print(f"[!] Please wait ... {i:02d} seconds", end="\r")
        sleep(1)
    print()

def generate_payload(bug_host, payload_type, extra_headers=None, use_split=False, method="CONNECT", protocol="HTTP/1.1", sni=False):
    if extra_headers is None:
        extra_headers = {}

    crlf = "[crlf]"
    split = "[split]" if use_split else ""

    base_payload = ""

    if payload_type == "normal":
        base_payload = f"{method} [host_port] {protocol}{crlf}Host: {bug_host}{crlf}{crlf}"

    elif payload_type == "front_inject":
        base_payload = f"GET http://{bug_host}/ {protocol}{crlf}Host: {bug_host}{crlf}{crlf}{method} [host_port] {protocol}{crlf}{crlf}"

    elif payload_type == "back_inject":
        base_payload = f"{method} [host_port] {protocol}{crlf}{crlf}GET http://{bug_host}/ {protocol}{crlf}Host: {bug_host}{crlf}{crlf}"

    elif payload_type == "front_query":
        base_payload = f"{method} {bug_host}@[host_port] {protocol}{crlf}{crlf}"

    elif payload_type == "back_query":
        base_payload = f"{method} [host_port]@{bug_host} {protocol}{crlf}{crlf}"

    elif payload_type == "websocket":
        base_payload = f"{method} [host_port] {protocol}{crlf}Upgrade: websocket{crlf}Connection: Upgrade{crlf}Host: {bug_host}{crlf}{crlf}"

    elif payload_type == "sni":
        base_payload = f"{method} [host_port] {protocol}{crlf}Host: {bug_host}{crlf}{crlf}"
        print("Note: For SNI, set SSL/TLS in HTTP Injector with bug_host as SNI.")

    # Add split if requested
    if use_split and crlf in base_payload:
        base_payload = base_payload.replace(crlf + "Host", split + crlf + "Host")

    # Add extra headers
    extra_str = ""
    for key, value in extra_headers.items():
        extra_str += f"{key}: {value}{crlf}"

    base_payload = base_payload.replace(crlf + crlf, crlf + extra_str + crlf)

    return base_payload

def main():
    clear()
    banner()

    bug_host = input("[!] Input Bug Host (e.g., bug.example.com): ").strip()
    if not bug_host:
        print("Bug host cannot be empty!")
        return

    wait(3)  # Short wait for effect

    while True:
        clear()
        banner()
        print("Select Payload Type:")
        print("1. Normal")
        print("2. Front Inject")
        print("3. Back Inject")
        print("4. Front Query")
        print("5. Back Query")
        print("6. WebSocket")
        print("7. SNI (SSL/TLS)")
        print("8. Exit")

        choice = input("Enter choice (1-8): ").strip()

        if choice == "8":
            break

        payload_types = {
            "1": "normal",
            "2": "front_inject",
            "3": "back_inject",
            "4": "front_query",
            "5": "back_query",
            "6": "websocket",
            "7": "sni"
        }

        if choice not in payload_types:
            print("Invalid choice!")
            sleep(2)
            continue

        method = input("Enter HTTP Method (default: CONNECT): ") or "CONNECT"
        protocol = input("Enter Protocol (default: HTTP/1.1): ") or "HTTP/1.1"
        use_split = input("Use Split? (y/n, default: n): ").lower() == "y"
        add_headers = input("Add extra headers? (y/n, default: n): ").lower() == "y"

        extra_headers = {}
        if add_headers:
            print("Enter headers in format 'Key: Value', one per line. Empty line to finish.")
            while True:
                header = input().strip()
                if not header:
                    break
                if ":" in header:
                    key, value = header.split(":", 1)
                    extra_headers[key.strip()] = value.strip()
                else:
                    print("Invalid format!")

        sni = payload_types[choice] == "sni"

        payload = generate_payload(bug_host, payload_types[choice], extra_headers, use_split, method, protocol, sni)

        print("\nGenerated Payload:")
        print(payload)

        save = input("\nSave to file? (y/n, default: n): ").lower() == "y"
        if save:
            filename = input("Enter filename (default: payload.txt): ") or "payload.txt"
            with open(filename, "w") as f:
                f.write(payload)
            print(f"Saved to {filename}")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    # Optional password, removed for simplicity, can add back if needed
    main()
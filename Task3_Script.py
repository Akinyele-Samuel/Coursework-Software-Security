import os
import socket
import subprocess
import time

def my_safe():
    with open("safe.log", "a") as f:
        f.write("User typed: hello\n")
        f.write("User typed: password123\n")
        f.write("User typed: exit\n")
    print("[*] Simulated activity logged to safe.log")

def alienwave():
    target_dir = "test_files"
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "example.txt"), "w") as f:
        f.write("This is a test file.")

    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)
        if os.path.isfile(file_path):
            os.rename(file_path, file_path + ".encrypted")
    print("[*] Simulated alienwave: Files in 'test_files/' renamed with '.encrypted' extension")

def activate_server():
    server_address = ("127.0.0.1", 5555)  
    try:
        print("[*] Attempting to simulate a server...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)
        sock.sendall(b"Hello from server\n")
        response = sock.recv(1024)
        print(f"[*] Server responded: {response.decode()}")
        sock.close()
    except ConnectionRefusedError:
        print("[*] server failed to connect (as expected)")

def my_script():
    startup_file = os.path.expanduser("~/.my_script.sh")
    with open(startup_file, "w") as f:
        f.write("#!/bin/bash\n")
        f.write("echo 'My script executed'\n")
    os.chmod(startup_file, 0o755)
    print(f"[*] Simulated persistence: Startup script created at {startup_file}")

def main():
    print("[*] Controlled Malware Simulation")
    print("1. My Safe")
    print("2. Alienwave")
    print("3. Activate Server")
    print("4. My Script")
    print("5. Exit")

    while True:
        choice = input("Choose a behavior to simulate (1-5): ").strip()
        if choice == "1":
            my_safe()
        elif choice == "2":
            alienwave()
        elif choice == "3":
            activate_server()
        elif choice == "4":
            my_script()
        elif choice == "5":
            print("[*] Exiting simulated malware.")
            break
        else:
            print("[!] Invalid choice. Try again.")

if __name__ == "__main__":
    main()
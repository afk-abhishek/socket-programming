
#!/usr/bin/env python3
"""
TCP Echo Server - Complete Implementation

A simple TCP server that echoes back any data it receives.
This demonstrates the fundamental socket operations.

"""

import socket
import sys


def create_server(host='localhost', port=8000):
    """
    Create and configure a TCP server socket.
    
    This is where we set up the server to listen for connections.
    
    Args:
        host: Hostname or IP address to bind to
        port: Port number to listen on
        
    Returns:
        Configured server socket ready to accept connections
    """
    # Step 1: Create a TCP socket
    # AF_INET = IPv4 addressing
    # SOCK_STREAM = TCP (connection-oriented, reliable)
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"1: Socket created")
    
    # Step 2: Set SO_REUSEADDR option
    # This allows reusing the address immediately after server shutdown
    # Without this, you'd get "Address already in use" errors
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print(f"2: Socket configured (SO_REUSEADDR enabled)")
    
    # Step 3: Bind the socket to an address
    # This associates the socket with a specific IP and port
    # The OS will now route incoming connections on this port to our socket
    server_socket.bind((host, port))
    print(f"3: Socket bound to {host}:{port}")
    
    # Step 4: Start listening for connections
    # The backlog parameter (5) is the max number of queued connections
    # If 5 clients are waiting and a 6th tries to connect, it'll be refused
    server_socket.listen(5)
    print(f"4: Socket listening (backlog: 5)")
    
    return server_socket


def handle_client(client_socket, client_address):
    """
    Handle a single client connection.
    
    This function reads data from the client and echoes it back.
    It loops until the client disconnects.
    
    Args:
        client_socket: Socket object for the connected client
        client_address: Tuple of (host, port) for the client
    """
    print(f"\n[+] New connection from {client_address[0]}:{client_address[1]}")
    
    try:
        while True:
            # Step 5: Receive data from the client
            # recv() blocks until data arrives or the connection closes
            # 1024 = buffer size in bytes (1 KB)
            data = client_socket.recv(1024)
            
            # Step 6: Check if client disconnected
            # When a client closes the connection, recv() returns empty bytes
            if not data:
                print(f"[-] Client {client_address} disconnected")
                break
            
            # Step 7: Echo the data back
            # send() might not send all data at once (rare but possible)
            # For production, use sendall() which handles partial sends
            client_socket.send(data)
            
            # Step 8: Log what we received (for debugging)
            # Decode from bytes to string, strip whitespace
            try:
                message = data.decode('utf-8').strip()
                print(f"[ECHO] {client_address}: {message}")
            except UnicodeDecodeError:
                print(f"[ECHO] {client_address}: <binary data, {len(data)} bytes>")
            
    except ConnectionResetError:
        # Client forcefully closed the connection (e.g., crashed)
        print(f"[!] Connection reset by {client_address}")
    except Exception as e:
        # Catch any other errors
        print(f"[!] Error handling client {client_address}: {e}")
    finally:
        # Step 9: Always close the client socket
        # This releases system resources
        client_socket.close()
        print(f"[-] Connection closed: {client_address}")


def run_server(host='localhost', port=8000):
    """
    Main server loop - accept and handle client connections.
    
    This creates the server socket and enters an infinite loop
    accepting new client connections.
    
    Args:
        host: Hostname to bind to
        port: Port number to listen on
    """
    # Create and configure the server socket
    server_socket = create_server(host, port)
    
    print(f"\n{'='*60}")
    print(f"🚀 Echo Server Started!")
    print(f"{'='*60}")
    print(f"Listening on: {host}:{port}")
    print(f"Press Ctrl+C to stop the server")
    print(f"{'='*60}\n")
    
    try:
        while True:
            # Step 10: Accept a new client connection
            # This blocks until a client connects
            # Returns a NEW socket for this specific client and their address
            client_socket, client_address = server_socket.accept()
            
            # Step 11: Handle the client
            # Note: This is blocking - we can only handle one client at a time
            # In Phase 2, we'll use threading to handle multiple clients
            handle_client(client_socket, client_address)
            
    except KeyboardInterrupt:
        # User pressed Ctrl+C
        print("\n\n[*] Shutting down gracefully...")
    except Exception as e:
        print(f"\n[!] Server error: {e}")
    finally:
        # Step 12: Close the server socket
        # This stops accepting new connections and releases the port
        server_socket.close()
        print("[*] Server socket closed")
        print("[*] Goodbye! 👋\n")


if __name__ == "__main__":
    # Configuration
    HOST = 'localhost'  # Listen on localhost only (use '0.0.0.0' for all interfaces)
    PORT = 8000         # Port number (use 1024-65535 for non-privileged)
    
    # Allow command-line arguments for easy testing
    if len(sys.argv) == 3:
        HOST = sys.argv[1]
        PORT = int(sys.argv[2])
    
    # Start the server
    run_server(HOST, PORT)

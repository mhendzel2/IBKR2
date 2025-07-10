#!/usr/bin/env python3
"""
Simple IBKR TWS Connection Test Script
This script tests the basic connection to TWS without the full application.
"""

import socket
import time
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

class TestWrapper(EWrapper):
    def __init__(self):
        EWrapper.__init__(self)
        self.connected = False
        self.error_occurred = False
        self.error_message = ""

    def connectAck(self):
        print("✅ Successfully connected to TWS!")
        self.connected = True

    def error(self, reqId, errorCode, errorString, advancedOrderRejectJson=""):
        print(f"❌ Error {errorCode}: {errorString}")
        self.error_occurred = True
        self.error_message = f"Error {errorCode}: {errorString}"

    def connectionClosed(self):
        print("🔌 Connection closed")

class TestClient(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)

def test_port_connection(host, port):
    """Test if the port is open and listening"""
    print(f"🔍 Testing port connection to {host}:{port}...")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        sock.close()
        
        if result == 0:
            print(f"✅ Port {port} is open and listening")
            return True
        else:
            print(f"❌ Port {port} is not accessible")
            return False
    except Exception as e:
        print(f"❌ Port test failed: {e}")
        return False

def test_tws_connection(host="127.0.0.1", port=7497, client_id=999):
    """Test TWS API connection"""
    print(f"\n🚀 Testing TWS API connection...")
    print(f"Host: {host}")
    print(f"Port: {port}")
    print(f"Client ID: {client_id}")
    print("-" * 50)
    
    # First test port connectivity
    if not test_port_connection(host, port):
        print("\n❌ DIAGNOSIS: TWS is not listening on the specified port")
        print("SOLUTIONS:")
        print("1. Make sure TWS is running and fully logged in")
        print("2. Check API settings in TWS (File → Global Configuration → API)")
        print("3. Verify the port number (7497 for paper, 7496 for live)")
        print("4. Restart TWS if needed")
        return False
    
    # Test API connection
    wrapper = TestWrapper()
    client = TestClient(wrapper)
    
    try:
        print(f"🔗 Attempting API connection...")
        client.connect(host, port, client_id)
        
        # Wait for connection
        timeout = 10
        start_time = time.time()
        
        while not wrapper.connected and not wrapper.error_occurred:
            client.run()
            if time.time() - start_time > timeout:
                print("❌ Connection timeout")
                break
            time.sleep(0.1)
        
        if wrapper.connected:
            print("✅ TWS API connection successful!")
            
            # Test a simple request
            print("📊 Testing market data request...")
            contract = Contract()
            contract.symbol = "AAPL"
            contract.secType = "STK"
            contract.exchange = "SMART"
            contract.currency = "USD"
            
            client.reqMktData(1, contract, "", False, False, [])
            time.sleep(2)  # Wait for response
            
            client.disconnect()
            print("✅ Connection test completed successfully!")
            return True
            
        elif wrapper.error_occurred:
            print(f"❌ API connection failed: {wrapper.error_message}")
            print("\n🔧 COMMON SOLUTIONS:")
            print("1. Try a different Client ID (1-32)")
            print("2. Check 'Read-Only API' is UNCHECKED in TWS")
            print("3. Verify 127.0.0.1 is in Trusted IPs")
            print("4. Restart TWS completely")
            return False
        else:
            print("❌ Connection failed - unknown error")
            return False
            
    except Exception as e:
        print(f"❌ Connection test failed: {e}")
        print("\n🔧 POSSIBLE SOLUTIONS:")
        print("1. Make sure TWS is running")
        print("2. Check firewall settings")
        print("3. Verify API is enabled in TWS")
        print("4. Try restarting TWS")
        return False

def main():
    print("=" * 60)
    print("🧪 IBKR TWS CONNECTION TEST")
    print("=" * 60)
    print("This script will test your TWS connection step by step.")
    print()
    
    # Get user input
    try:
        host = input("Enter TWS host (default: 127.0.0.1): ").strip() or "127.0.0.1"
        port_input = input("Enter TWS port (default: 7497): ").strip() or "7497"
        port = int(port_input)
        client_id_input = input("Enter Client ID (default: 999): ").strip() or "999"
        client_id = int(client_id_input)
    except ValueError:
        print("❌ Invalid input. Using defaults.")
        host, port, client_id = "127.0.0.1", 7497, 999
    
    print()
    success = test_tws_connection(host, port, client_id)
    
    print("\n" + "=" * 60)
    if success:
        print("🎉 CONNECTION TEST PASSED!")
        print("Your TWS connection is working correctly.")
        print("You can now use the IBKR Data Collector application.")
    else:
        print("❌ CONNECTION TEST FAILED!")
        print("Please follow the troubleshooting steps above.")
        print("Check the TROUBLESHOOTING_GUIDE.md for detailed solutions.")
    print("=" * 60)

if __name__ == "__main__":
    main()


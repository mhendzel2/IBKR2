# IBKR Data Collector - Troubleshooting Guide

## 🚨 IMPORTANT: Network Connection Issue

**The main issue you're experiencing is that the deployed web application cannot connect to your local TWS instance.** 

The deployed app runs on a remote server (mzhyi8cqgelj.manus.space) and cannot access your local machine where TWS is running (127.0.0.1:7497). This is a fundamental networking limitation.

## ✅ SOLUTION: Run the Application Locally

You need to download and run the application on your local machine where TWS is installed.

### Step 1: Download and Setup

1. **Download the application** (ZIP file provided)
2. **Extract** the ZIP file to a folder on your computer
3. **Open Command Prompt** as Administrator
4. **Navigate** to the extracted folder:
   ```cmd
   cd C:\path\to\ibkr-data-collector
   ```

### Step 2: Install Python Dependencies

1. **Install Python 3.11+** if not already installed (from python.org)
2. **Create virtual environment**:
   ```cmd
   python -m venv venv
   ```
3. **Activate virtual environment**:
   ```cmd
   venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```cmd
   pip install -r requirements.txt
   ```

### Step 3: Configure TWS (Double-Check Settings)

Even though you mentioned these are configured, let's verify:

1. **Open TWS**
2. **Go to**: File → Global Configuration → API → Settings
3. **Verify these settings**:
   - ✅ **Enable ActiveX and Socket Clients** (checked)
   - ✅ **Socket port**: `7497` (for paper trading)
   - ✅ **Master API client ID**: `0` (default)
   - ✅ **Read-Only API**: **UNCHECKED** (very important!)
   - ✅ **Download open orders on connection**: Checked (recommended)

4. **Trusted IPs section**:
   - Add `127.0.0.1` if not already there
   - Add `localhost` as well (sometimes needed)

5. **Click OK** and **restart TWS** for changes to take effect

### Step 4: Start the Local Application

1. **In Command Prompt** (with virtual environment activated):
   ```cmd
   python src\main.py
   ```

2. **Open your web browser** and go to:
   ```
   http://localhost:5001
   ```

### Step 5: Test Connection

1. **Go to Settings tab** in the application
2. **Enter connection details**:
   - Host: `127.0.0.1`
   - Port: `7497`
   - Client ID: `1` (or any number 1-32)
3. **Click "Test Connection"**

## 🔧 Additional Troubleshooting Steps

### If Connection Still Fails:

#### 1. Check TWS API Status
- In TWS, look for **API status indicator** (usually in bottom right)
- Should show "API: Ready" or similar
- If not, restart TWS

#### 2. Verify Port Availability
Open Command Prompt and run:
```cmd
netstat -an | findstr 7497
```
You should see something like:
```
TCP    127.0.0.1:7497        0.0.0.0:0              LISTENING
```

#### 3. Windows Firewall
1. **Open Windows Defender Firewall**
2. **Click "Allow an app or feature through Windows Defender Firewall"**
3. **Add TWS** if not already listed
4. **Add Python** if not already listed

#### 4. Try Different Client ID
- In the app settings, try Client ID: `2`, `3`, or `4`
- Each connection needs a unique Client ID

#### 5. Check TWS Logs
1. **In TWS**: Help → Support → View Logs
2. **Look for API-related errors**
3. **Common issues**:
   - "API client connection rejected"
   - "Maximum number of clients reached"

#### 6. Alternative: Use IB Gateway
If TWS continues to have issues:

1. **Download IB Gateway** (lighter than TWS)
2. **Configure for Paper Trading**
3. **Use port 4001** instead of 7497
4. **Update app settings** to use port 4001

### Common Error Messages and Solutions:

#### "Connection refused"
- TWS is not running or API is disabled
- Wrong port number
- Firewall blocking connection

#### "Connection timeout"
- TWS is busy or frozen
- Network connectivity issues
- Try restarting TWS

#### "Authentication failed"
- Wrong client ID (try different number)
- API permissions not enabled
- Account not properly logged in

#### "Maximum clients reached"
- TWS has limit of 32 API connections
- Restart TWS to clear connections
- Use different client ID

## 📋 Quick Checklist

Before testing connection, verify:

- [ ] TWS is fully logged in and showing market data
- [ ] API settings are enabled in TWS
- [ ] Port 7497 is configured in TWS
- [ ] Read-Only API is UNCHECKED
- [ ] 127.0.0.1 is in trusted IPs
- [ ] Application is running locally (not deployed version)
- [ ] Using correct host (127.0.0.1) and port (7497)
- [ ] Unique client ID (1-32)
- [ ] No firewall blocking the connection

## 🆘 If All Else Fails

1. **Restart everything**:
   - Close TWS completely
   - Stop the application
   - Restart TWS
   - Wait for full login
   - Start application again

2. **Try IB Gateway instead of TWS**:
   - Often more reliable for API connections
   - Uses port 4001 for paper trading

3. **Check IBKR account permissions**:
   - Ensure API access is enabled in your account
   - Some accounts have API restrictions

4. **Test with simple connection**:
   - Try connecting with a basic Python script first
   - Verify the API works before using the full application

## 📞 Additional Resources

- **IBKR API Documentation**: https://interactivebrokers.github.io/tws-api/
- **TWS API Support**: Contact IBKR support for API-specific issues
- **Python ibapi Documentation**: Check the official Python API docs

Remember: The key issue was trying to connect from a remote server to your local machine. Running the application locally should resolve the connection problem!


# IBKR Data Collector

A comprehensive web application for collecting and storing various classes of data from the Interactive Brokers (IBKR) TWS API, designed specifically for feeding into transformer models for stock price prediction.

## Features

### Data Collection Types
- **Real-time Market Data**: Level I market data with bid/ask/last prices and volumes
- **Historical Data**: OHLCV historical bars with multiple timeframes
- **Tick-by-Tick Data**: Individual trades and quotes
- **Account Data**: Account values, buying power, and margin information
- **Portfolio Data**: Current positions and P&L information
- **News Data**: Real-time news headlines and articles
- **Fundamental Data**: Corporate events, earnings, and fundamental analysis
- **Options Data**: Option prices, Greeks, and implied volatility

### User Interface
- **Modern Web Interface**: Professional, responsive design with intuitive navigation
- **Checkbox Controls**: Easy selection of data types to collect
- **Job Management**: Create, monitor, and manage data collection jobs
- **Real-time Monitoring**: Live progress tracking and status updates
- **Data Explorer**: Browse and analyze collected data
- **Export Functionality**: Export data in various formats for ML training

### Technical Features
- **RESTful API**: Comprehensive backend API for all operations
- **Database Storage**: Structured storage with optimized schemas for time-series data
- **Real-time Updates**: Live data streaming and job progress monitoring
- **Error Handling**: Robust error handling and retry mechanisms
- **Scalable Architecture**: Modular design for easy extension and maintenance

## Prerequisites

1. **Interactive Brokers Account**: You need an active IBKR account
2. **TWS or IB Gateway**: Install and configure TWS (Trader Workstation) or IB Gateway
3. **Python 3.11+**: Required for running the application
4. **API Permissions**: Enable API access in your IBKR account settings

## Installation

### 1. Clone or Download the Application
```bash
# If you have the source code
cd ibkr-data-collector
```

### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure IBKR TWS/Gateway

#### TWS Configuration:
1. Open TWS (Trader Workstation)
2. Go to **File > Global Configuration > API > Settings**
3. Enable **Enable ActiveX and Socket Clients**
4. Set **Socket port** to `7497` (paper trading) or `7496` (live trading)
5. Add `127.0.0.1` to **Trusted IPs**
6. **Important**: Uncheck **Read-Only API** to allow data collection

#### IB Gateway Configuration:
1. Open IB Gateway
2. Use port `4001` (paper trading) or `4000` (live trading)
3. Enable API connections
4. Add `127.0.0.1` to trusted IPs

### 5. Start the Application
```bash
python src/main.py
```

The application will start on `http://localhost:5001`

## Usage Guide

### 1. Initial Setup
1. Open your web browser and navigate to `http://localhost:5001`
2. Go to the **Settings** tab
3. Configure your IBKR connection:
   - **Host**: `127.0.0.1` (default)
   - **Port**: `7497` (TWS paper) or `7496` (TWS live) or `4001` (Gateway paper) or `4000` (Gateway live)
   - **Client ID**: `1` (default, can be any unique number)
4. Click **Test Connection** to verify connectivity

### 2. Creating a Data Collection Job
1. Navigate to the **Data Collection** tab
2. Fill in the job configuration:
   - **Job Name**: Descriptive name for your collection job
   - **Start Date**: Optional start date for historical data
   - **End Date**: Optional end date for historical data
3. Select data types by checking the desired checkboxes:
   - **Real-time Market Data**: For live price feeds
   - **Historical Bars**: For historical OHLCV data
   - **Account Data**: For account information
   - **Portfolio Data**: For position tracking
   - **News Data**: For news feeds
   - **Options Data**: For options pricing and Greeks
4. Add symbols:
   - Enter stock symbols (e.g., AAPL, MSFT, GOOGL)
   - Click **Add** to include each symbol
5. Click **Start Collection** to begin data collection

### 3. Monitoring Jobs
1. Go to the **Jobs** tab to view all collection jobs
2. Monitor job progress with real-time progress bars
3. Use job controls:
   - **Start**: Begin a pending job
   - **Stop**: Halt a running job
   - **Delete**: Remove completed or failed jobs

### 4. Exploring Data
1. Navigate to the **Data Explorer** tab
2. Select a symbol and data type
3. Click **Load Data** to view collected information
4. Browse through the data table to analyze results

### 5. Exporting Data
1. Go to the **Settings** tab
2. Click **Export All Data** to generate datasets for ML training
3. Data will be exported in formats suitable for transformer models

## Data Schema

### Database Tables
- **symbols**: Symbol definitions and metadata
- **market_data_realtime**: Live market data feeds
- **historical_bars**: OHLCV historical data
- **tick_data**: Tick-by-tick trade and quote data
- **option_data**: Options pricing and Greeks
- **account_data**: Account value updates
- **portfolio_positions**: Position and P&L data
- **news_data**: News headlines and articles
- **fundamental_data**: Corporate events and fundamentals
- **data_collection_jobs**: Job management and tracking

### Data Export Formats
- **CSV**: Standard comma-separated format
- **Parquet**: Columnar format optimized for analytics
- **JSON**: JavaScript Object Notation
- **HDF5**: Hierarchical format for large datasets

## API Endpoints

### Configuration
- `GET /api/ibkr/config/data-types` - Get available data types
- `POST /api/ibkr/config/connection` - Test IBKR connection
- `GET /api/ibkr/config/status` - Get system status

### Job Management
- `GET /api/ibkr/jobs` - List all jobs
- `POST /api/ibkr/jobs` - Create new job
- `GET /api/ibkr/jobs/{id}` - Get job details
- `POST /api/ibkr/jobs/{id}/start` - Start job
- `POST /api/ibkr/jobs/{id}/stop` - Stop job
- `DELETE /api/ibkr/jobs/{id}` - Delete job

### Data Access
- `GET /api/ibkr/data/symbols` - Get available symbols
- `GET /api/ibkr/data/market/{symbol}` - Get market data
- `GET /api/ibkr/data/historical/{symbol}` - Get historical data
- `GET /api/ibkr/data/options/{symbol}` - Get options data
- `GET /api/ibkr/data/news/{symbol}` - Get news data

## Troubleshooting

### Connection Issues
1. **"Failed to connect to IBKR API"**:
   - Ensure TWS/Gateway is running
   - Check API settings are enabled
   - Verify port numbers match
   - Confirm trusted IPs include 127.0.0.1

2. **"Port already in use"**:
   - Change the application port in `src/main.py`
   - Or stop other applications using the same port

### Data Collection Issues
1. **"No data received"**:
   - Verify market hours (data may be limited outside trading hours)
   - Check symbol validity
   - Ensure proper market data subscriptions

2. **"Permission denied"**:
   - Verify API permissions in IBKR account
   - Check trading permissions for specific instruments
   - Ensure account is funded (required for some data types)

### Performance Optimization
1. **Slow data collection**:
   - Limit concurrent requests (max 100 market data lines)
   - Use appropriate timeframes for historical data
   - Consider data retention policies

2. **Database performance**:
   - Regular database maintenance
   - Index optimization for frequently queried data
   - Consider data archiving for old records

## Development

### Project Structure
```
ibkr-data-collector/
├── src/
│   ├── models/          # Database models
│   ├── routes/          # API routes
│   ├── static/          # Frontend files
│   ├── database/        # SQLite database
│   ├── ibkr_client.py   # IBKR API client
│   ├── data_collector.py # Data collection service
│   └── main.py          # Application entry point
├── venv/                # Virtual environment
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

### Adding New Data Types
1. Define new model in `src/models/ibkr_models.py`
2. Add collection handler in `src/data_collector.py`
3. Create API endpoints in `src/routes/ibkr_routes.py`
4. Update frontend checkboxes in `src/static/index.html`

### Extending the API
1. Add new routes in `src/routes/ibkr_routes.py`
2. Follow RESTful conventions
3. Include proper error handling
4. Update API documentation

## Security Considerations

1. **API Keys**: Never commit API credentials to version control
2. **Network Security**: Use secure connections in production
3. **Access Control**: Implement authentication for production use
4. **Data Privacy**: Ensure compliance with financial data regulations

## License

This application is provided for educational and research purposes. Please ensure compliance with Interactive Brokers' API terms of service and applicable financial regulations.

## Support

For issues and questions:
1. Check the troubleshooting section above
2. Review IBKR API documentation
3. Verify TWS/Gateway configuration
4. Check application logs for detailed error messages

## Disclaimer

This software is for educational purposes only. Trading and investment decisions should not be based solely on this application. Always consult with qualified financial professionals and understand the risks involved in trading financial instruments.


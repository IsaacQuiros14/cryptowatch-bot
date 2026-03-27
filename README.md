CryptoWatch Bot
Description
A professional-grade cryptocurrency monitoring system built in Python that implements a complete ETL (Extract, Transform, Load) pipeline. The application fetches real-time price data from the CoinGecko API, validates data integrity through a specialized quality assurance layer, and persists information in dual storage formats (CSV and SQLite) for historical tracking and advanced analytics.

Technical Features
Architecture and Design
Modular Architecture: Strict separation of concerns with dedicated modules for API integration, data collection, processing, storage, and utilities.

Data Quality Layer: Robust validation system designed to detect outliers, API anomalies, and edge cases before persistence.

Dual Persistence Strategy: Implementation of flat files (CSV) for portability and a relational database (SQLite) for high-performance queries.

Performance and Optimization
SQL Query Optimization: Composite indexing on (symbol, timestamp) to ensure sub-second response times for time-series queries.

Concurrency Management: SQLite configured with WAL (Write-Ahead Logging) mode to support simultaneous read/write operations.

Batch Processing: Efficient bulk insertion methods using parameterized queries to ensure data security and prevent SQL injection.

Engineering Best Practices
ETL Pipeline: Industry-standard Extract-Transform-Load workflow with dedicated data validation middleware.

Error Handling: Custom exception hierarchy and comprehensive edge case management for system resilience.

Type Safety: Full implementation of Python type hints to improve code maintainability and documentation.

Project Structure
main.py: System orchestrator and ETL entry point.

src/api/: Low-level API client for external communication.

src/collectors/: Data ingestion and gathering layer.

src/processors/: Business logic, data validation, and analytical filtering.

src/storage/: Persistence handlers for both SQL and CSV formats.

data/: Local storage for processed datasets (Ignored by version control).

Installation
Clone the repository:
git clone https://github.com/IsaacQuiros14/cryptowatch-bot.git

Create a virtual environment:
python -m venv venv

Activate the virtual environment:

Windows: venv\Scripts\activate

Linux/macOS: source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Usage
Execute the primary ETL pipeline to fetch and persist data:
python main.py

Database Schema
The system utilizes a central table crypto_prices with the following optimized structure:

id: Primary key (Integer).

timestamp: Data collection time (Datetime).

symbol: Cryptocurrency identifier (Text).

price: Value in USD (Real).

Indexes: Composite index idx_symbol_timestamp on (symbol, timestamp DESC).

License
This project is open-source and available under the MIT License.

Author
Isaac Quiros
GitHub: @IsaacQuiros14
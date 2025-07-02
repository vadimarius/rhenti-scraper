# 🏡 Rhenti Real Estate Scraper

A Python scraper for extracting rental property data from [mynd.rhenti.com](https://mynd.rhenti.com) via their public API.

## 🔍 Features:
- Parses rental property listings across the USA.
- Handles grid-based pagination and avoids duplicates.
- Automatically splits overloaded map areas for complete data extraction.
- Saves data to CSV with fields:
  - Address
  - City
  - Price
  - Bedrooms
  - Bathrooms
  - Amenities
  - Listing URL

## 🛠️ Technologies:
- Python 3
- Requests
- CSV module
- Random/Time (for rate limiting)

## 🚀 How to Run:
1. Install Python 3.
2. Clone the repository.
3. Run the script:
```bash
python main.py

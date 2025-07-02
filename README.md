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
- CSV module (built-in)
- Random/Time (built-in, for rate limiting)

## 🚀 How to Run:
1. Install **Python 3**.  
2. Clone the repository:  
```bash
git clone https://github.com/vadimarius/rhenti-scraper.git
cd rhenti-scraper

#Install dependencies:
pip install -r requirements.txt

#Run the script:
python main.py

#Data will be saved to rentals_usa.csv.

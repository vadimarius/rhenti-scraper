import requests
import csv
import time
import random

def frange(start, stop, step):
    while start < stop:
        yield round(start, 6)
        start += step

def get_rentals(lat1, lng1, lat2, lng2):
    url = (
        f"https://api.rhenti.com/properties?"
        f"bottomLeftCorner={lng1}&bottomLeftCorner={lat1}&"
        f"topRightCorner={lng2}&topRightCorner={lat2}&"
        "whitelabel=65b2823e90769e8db5543c1a"
    )
    response = requests.get(url, headers=headers, timeout=15)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code} when requesting: {url}")
        return []

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://mynd.rhenti.com",
    "Referer": "https://mynd.rhenti.com/",
    "x-language": "en",
    "x-white-label": "mynd"
}

output_path = "rentals_usa.csv"
collected_ids = set()

def main():
    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Address", "City", "Price", "Bedrooms", "Bathrooms", "Amenities", "Listing URL"])

        lat_min, lat_max = 24.5, 49.5
        lng_min, lng_max = -125, -66.5
        step = 1.0

        for lat in frange(lat_min, lat_max, step):
            for lng in frange(lng_min, lng_max, step):
                rentals = get_rentals(lat, lng, lat+step, lng+step)
                print(f"Received {len(rentals)} rentals for square ({lat}, {lng})")
                if len(rentals) > 30 and step > 0.2:
                    # If too many, split the square into 4 and process with a smaller step!
                    small_step = step / 2
                    for lat2 in frange(lat, lat+step, small_step):
                        for lng2 in frange(lng, lng+step, small_step):
                            sub_rentals = get_rentals(lat2, lng2, lat2+small_step, lng2+small_step)
                            print(f"  > [Detailing] {len(sub_rentals)} for sub-square ({lat2}, {lng2})")
                            for item in sub_rentals:
                                listing_id = item.get("_id")
                                if listing_id in collected_ids:
                                    continue
                                collected_ids.add(listing_id)
                                address = item.get("full_address", "N/A")
                                city = item.get("address_details", {}).get("city", "N/A")
                                price = item.get("price", "N/A")
                                bedrooms = item.get("bedrooms", "N/A")
                                bathrooms = item.get("bathrooms", "N/A")
                                amenities = [a.get("name") for a in item.get("amenities_list", [])]
                                amenities_str = ", ".join(amenities)
                                listing_url = f"https://mynd.rhenti.com/#/property/{listing_id}"
                                writer.writerow([address, city, price, bedrooms, bathrooms, amenities_str, listing_url])
                            time.sleep(random.uniform(0.5, 1.2))
                else:
                    for item in rentals:
                        listing_id = item.get("_id")
                        if listing_id in collected_ids:
                            continue
                        collected_ids.add(listing_id)
                        address = item.get("full_address", "N/A")
                        city = item.get("address_details", {}).get("city", "N/A")
                        price = item.get("price", "N/A")
                        bedrooms = item.get("bedrooms", "N/A")
                        bathrooms = item.get("bathrooms", "N/A")
                        amenities = [a.get("name") for a in item.get("amenities_list", [])]
                        amenities_str = ", ".join(amenities)
                        listing_url = f"https://mynd.rhenti.com/#/property/{listing_id}"
                        writer.writerow([address, city, price, bedrooms, bathrooms, amenities_str, listing_url])
                time.sleep(random.uniform(0.7, 1.5))

if __name__ == "__main__":
    main()

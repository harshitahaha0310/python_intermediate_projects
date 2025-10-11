import requests

def get_crypto_price(crypto_symbol):
    """
    Fetches the current cryptocurrency price using the CoinGecko API.
    Handles request and response errors.
    """
    try:
        # API endpoint (public, no API key required)
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies=usd"
        
        # Sending GET request
        response = requests.get(url)
        
        # Check if the response was successful
        response.raise_for_status()
        
        # Parse JSON data
        data = response.json()
        
        # Validate and display fetched data
        if crypto_symbol in data:
            price = data[crypto_symbol]['usd']
            print(f"\n💰 Current price of {crypto_symbol.capitalize()} is: ${price:,}")
        else:
            print("⚠️ Invalid cryptocurrency symbol or data not found.")
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")
    except ValueError:
        print("❌ Error parsing response from API.")
    except Exception as e:
        print(f"⚠️ Unexpected error occurred: {e}")

# Main program
if __name__ == "__main__":
    print("=== Cryptocurrency Price Checker ===")
    crypto = input("Enter cryptocurrency name (e.g., bitcoin, ethereum, dogecoin): ").lower().strip()
    get_crypto_price(crypto)

from conversion import convert_currency
from utils import validate_currency_code, get_currency_flag

def main():
    print("Welcome to the Currency Converter! Valid currencies: USD, EUR, GBP, INR, AUD, CAD, SGD, JPY, CNY, CHF ")
    
    while True:
        from_currency = input("Enter the currency code you want to convert from: ").upper()
        to_currency = input("Enter the currency code you want to convert to: ").upper()
        amount = float(input("Enter the amount you want to convert: "))

        try:
            validate_currency_code(from_currency)
            validate_currency_code(to_currency)

            # Get the flags for the currencies
            from_flag = get_currency_flag(from_currency)
            to_flag = get_currency_flag(to_currency)
            
            # Convert the currency
            converted_amount = convert_currency(from_currency, to_currency, amount)

            # Print result with flags
            print(f"{amount} {from_currency} {from_flag} = {converted_amount:.2f} {to_currency} {to_flag}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Ask if the user wants to perform another conversion
        again = input("Do you want to perform another conversion? (yes/no): ").lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()

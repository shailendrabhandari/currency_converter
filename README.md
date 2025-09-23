
# **Currency Converter**

This project is a Python-based currency converter that allows users to convert currencies in real time using the CurrencyLayer API. It includes additional features such as displaying country flags, comparing multiple currencies at once, and allowing the user to perform continuous conversions in a loop.

## **Features**
- **Real-Time Currency Conversion**: Convert any amount from one currency to another using live exchange rates.
- **Country Flags**: Display country flags next to the currency codes for easy recognition.
- **Compare Multiple Currencies**: Compare one currency to multiple other currencies in a single operation.
- **Interactive Loop**: After each conversion, the program asks if the user wants to continue or exit.
- **Supported Currencies**: USD, EUR, GBP, INR, AUD, CAD, SGD, JPY, CNY, CHF.

## **Prerequisites**
- Python 3.x installed on your system.
- Internet connection (for fetching live exchange rates).
- [CurrencyLayer API](https://currencylayer.com/) API key (replace the placeholder in `api.py` with your key).

## **Installation**

1. **Clone the Repository** (or download the files):
   ```bash
   git clone https://github.com/your_username/currency_converter.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd currency_converter
   ```

3. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment**:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies**:
   - Install the required libraries using the `requirements.txt` file:
     ```bash
     pip install -r requirements.txt
     ```

6. **Update API Key**:
   - In the file `api.py`, replace `your_api_key_here` with your actual API key from CurrencyLayer.
   - Free Forex API (Totally Free) I used this API
   - URL: [Free Forex API](https://www.exchangerate-api.com/)



## **Usage**

1. **Run the Main Script**:
   ```bash
   python src/main.py
   ```

2. **Input the following**:
   - **Currency Code to Convert From**: Enter the code of the currency you want to convert from (e.g., `USD`).
   - **Currency Code to Convert To**: You can enter a single currency or multiple currencies, separated by commas (e.g., `EUR,GBP,CAD`).
   - **Amount**: Enter the amount you want to convert.

3. **View the Result**:
   - The program will display the converted amount(s) with the corresponding country flags.

4. **Continue or Exit**:
   - After each conversion, the program will ask if you want to perform another conversion. Enter `yes` to continue or `no` to exit.

## **Example of Usage**

```
Welcome to the Currency Converter!
Enter the currency code you want to convert from: USD
Enter the currency code(s) you want to convert to (comma-separated): EUR,GBP
Enter the amount you want to convert: 100
1 USD 🇺🇸 = 0.85 EUR 🇪🇺
1 USD 🇺🇸 = 0.75 GBP 🇬🇧
Do you want to perform another comparison? (yes/no): yes
```

## **Project Structure**

```
Currency_converter/
├── src/
│   ├── api.py               # Handles API calls to fetch exchange rates
│   ├── conversion.py         # Logic for converting currencies
│   ├── utils.py              # Utility functions (validation, flags)
│   └── main.py               # Main script that ties everything together
├── tests/
│   ├── test_api.py           # Unit tests for API functions
│   ├── test_conversion.py     # Unit tests for conversion functions
│   └── test_utils.py          # Unit tests for utility functions
├── requirements.txt          # List of dependencies
└── README.md                 # Project documentation
```

## **Modules**

- **`api.py`**: Handles API requests to get exchange rates.
- **`conversion.py`**: Performs the actual currency conversion based on fetched rates.
- **`utils.py`**: Contains utility functions like currency validation and displaying country flags.
- **`main.py`**: The main script that interacts with the user and coordinates currency conversions.

## **Additional Features to Add**
- **Historical Exchange Rates**: You can extend the project to support fetching historical exchange rates for a specific date.
- **Currency Alerts**: Add functionality to notify users when a certain currency reaches a desired threshold.

## **Dependencies**

- `requests`: For making API calls.
- `emoji`: For displaying country flags.

Install dependencies with:
```bash
pip install -r requirements.txt
```

## **Contributing**

1. Fork the repository.
2. Create a new branch (`git checkout -b new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin new-feature`).
5. Create a pull request.

## **License**

This project is licensed under the Apache License Version2.0.

---

### **Future Enhancements**

- Support for more currencies.
- A graphical user interface (GUI) using `tkinter` or a web-based interface using `Flask`.
- Store and load conversion history in a file.

---

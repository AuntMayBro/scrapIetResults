# IET-DAVV Result Scraper

A Python script to programmatically fetch student results from the official IET-DAVV results website and compile them into a single Excel spreadsheet.

## Description

This script automates the process of checking academic results for students of the Institute of Engineering & Technology, DAVV, Indore. It constructs roll numbers based on predefined batch codes and number ranges, sends requests to the results portal, parses the HTML response to extract relevant data, and saves the collected information into a structured Excel file.

## Features

- **Batch Processing**: Fetches results for entire batches of students automatically.
- **Data Extraction**: Scrapes key information including Student Name, Enrollment Number, Roll Number, SGPA, and Final Result (Pass/Fail).
- **Error Handling**: Gracefully handles cases where a student's result is not declared, the roll number does not exist, or a network error occurs.
- **Structured Output**: Organizes all the fetched data into a clean, easy-to-read Excel file (`.xlsx`).
- **Customizable**: Easily configurable to target different batches, years, or specific ranges of roll numbers.

## Prerequisites

Before running the script, you need to have Python installed. Additionally, you'll need the following Python libraries:

- `requests`: For making HTTP requests to the website.
- `beautifulsoup4`: For parsing HTML and extracting data.
- `pandas`: For creating and managing the data in a DataFrame.
- `openpyxl`: Required by pandas to write to `.xlsx` files.

## Installation

1.  **Clone the repository or download the script.**

2.  **Install the required libraries using pip:**
    ```bash
    pip install requests beautifulsoup4 pandas openpyxl
    ```

## How to Use

1.  **Configure the Batches**:
    Open the script file and locate the `roll_number_batches` dictionary. You can modify this dictionary to specify the batches and roll number ranges you want to scrape. The `a` variable is a base number added to the range.

    ```python
    # Base number for roll numbers
    a = 4000 

    # Dictionary of batches to scrape
    roll_number_batches = {
        "23C": range(1, 190),  # Scrapes 23C4001 to 23C4189
        "23I": range(1, 190),  # Scrapes 23I4001 to 23I4189
        "23E": range(1, 100),  # Scrapes 23E4001 to 23E4099
        "23V": range(1, 60),   # Scrapes 23V4001 to 23V4059
    }
    ```

2.  **Run the Script**:
    Execute the script from your terminal:
    ```bash
    python scrapResult.py
    ```
    *(Replace `scrapResult.py` with the actual name of your file.)*

    The script will print the progress in the console, indicating which roll number it is currently fetching.

## Output

Once the script finishes execution, it will generate an Excel file named `student_results.xlsx` in the same directory. The file will contain the following columns:

-   `Name`
-   `Enrollment No.`
-   `Roll No`
-   `SGPA`
-   `Result`

For roll numbers where a result could not be found or an error occurred, the `Name` column will contain a status message (e.g., "Not found or result not declared for: 23C4099").

## Disclaimer

-   This script is intended for educational and personal use only.
-   The functionality of this scraper is dependent on the structure of the IET-DAVV results website. Any changes to the website's HTML layout may break the script.
-   Please use the script responsibly and avoid sending an excessive number of requests in a short period to prevent overloading the server.


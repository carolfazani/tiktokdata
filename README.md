# TikTok Data Extraction Project

## Overview

This project aims to extract TikTok video data using Selenium for web automation, clean the data, and store it in a MySQL database. The code is structured into several classes to modularize functionality:

1. **Mydb**: Handles MySQL connections and operations.
2. **Requester**: Navigates and fetches data from TikTok.
3. **GeTData**: Extracts specific data from TikTok pages.
4. **SaveSQL**: Saves cleaned data into MySQL database.
5. **Cleandata**: Cleans and processes the extracted data.

## Requirements

- Python 3.x
- MySQL
- Selenium
- Tqdm
- Pandas
- Json
- MySQL Connector

## Installation

1. Clone the repository:

```bash
git clone https://github.com/carolfazani/tiktokdata.git

cd tiktok-data-extraction
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

## Configuration

Make sure to set up your environment variables for MySQL connection:

```bash
export host='your_host'
export port='your_port'
export user='your_user'
export passwd='your_password'
export database='your_database'
```

## Code Structure

### Class Mydb

The `Mydb` class manages the MySQL database connection.

#### Methods:

- **`open`**: Opens a connection to the database.
- **`close`**: Closes the database connection.
- **`query`**: Executes an SQL query.

### Class Requester

The `Requester` class sets up and initializes the browser to fetch data from TikTok.

#### Methods:

- **`__init__`**: Initializes the class with query and number of pages to load.
- **`get_url`**: Navigates to the TikTok search URL.

### Class GeTData

The `GeTData` class inherits from `Requester` and performs extraction of video data from TikTok.

#### Methods:

- **`get_data`**: Extracts specific data from TikTok videos and saves it into a JSON file.
- **`close_url`**: Closes the browser.

### Class SaveSQL

The `SaveSQL` class saves cleaned data into the MySQL database.

#### Methods:

- **`__init__`**: Initializes the database connection and loads the dataframe with cleaned data.
- **`tk_content`**: Inserts data into the MySQL database.

### Class Cleandata

The `Cleandata` class cleans and processes the extracted data.

#### Methods:

- **`__init__`**: Initializes the dataframe with data from the JSON file.
- **`content`**: Retains the `content` column.
- **`views`**: Converts views to integers.
- **`fetch_date`**: Converts fetch date to datetime format.
- **`content_date`**: Converts content date to datetime format.
- **`offset_days`**: Calculates days offset between fetch date and content date.
- **`daily_views`**: Calculates daily views.
- **`datacsv`**: Saves cleaned data to a CSV file.
- **`dataframe`**: Returns the processed dataframe.

## Usage

1. **Data Extraction**: Execute the following command to start extracting data from TikTok:

```python
from geTData import GeTData
data_extractor = GeTData(query="your_query", loadmore=10)
data_extractor.get_data()
```

2. **Data Cleaning and Saving**: After extraction, run the code to clean and save data to MySQL:

```python
savesql = SaveSQL()
savesql.tk_content()
```

## Contribution

Feel free to contribute to this project. Open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.


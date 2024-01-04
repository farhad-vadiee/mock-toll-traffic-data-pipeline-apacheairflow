# Educational Project: National Highways Traffic Data Consolidation

## Project Overview
This educational project is designed to simulate the analysis of road traffic data to mitigate congestion on national highways. The scenario involves handling traffic data from multiple toll plazas, each operating with different IT systems and file formats. The goal is to standardize and consolidate this data into a single file format for analysis. Note that the data used in this project is synthetic and intended for educational purposes only.

## File Descriptions
- `vehicle-data.csv`: Synthetic CSV file with traffic data fields such as Row ID, Timestamp, Anonymized Vehicle Number, and Vehicle Type.
- `tollplaza-data.tsv`: A tab-separated values file with mock Toll Plaza ID and Code.
- `payment-data.txt`: A fixed-width file containing fictional data on the Type of Payment Code and Vehicle Code.

## Data Processing Steps
1. **Unzip Data**: Extract the contents from a zipped data archive.
2. **Extract CSV Data**: Isolate specific fields from `vehicle-data.csv` for analysis.
3. **Extract TSV Data**: Retrieve toll-related information from `tollplaza-data.tsv`.
4. **Extract Fixed Width Data**: Parse `payment-data.txt` for payment method data.
5. **Consolidate Data**: Merge the extracted information into one consolidated CSV file.
6. **Transform Data**: Standardize certain data fields, such as converting the Vehicle Type to uppercase, for consistency across the dataset.

## DAG Configuration (Directed Acyclic Graph)
- **DAG ID**: `ETL_toll_data`
- **Schedule**: Set to run daily
- **Default Arguments**:
  - Owner: `DummyName`
  - Start Date: `today`
  - Email: `dummy@example.com`
  - Email on Failure: `True`
  - Email on Retry: `True`
  - Retries: `1`
  - Retry Delay: `5 minutes`
- **Description**: An Apache Airflow DAG designed to automate the ETL process for consolidating fabricated toll data.

## Tasks in the DAG
1. **unzip_data**: Unzip the dataset into a working directory.
2. **extract_data_from_csv**: Extract and save required fields from `vehicle-data.csv`.
3. **extract_data_from_tsv**: Isolate and store relevant fields from `tollplaza-data.tsv`.
4. **extract_data_from_fixed_width**: Extract and save specific data from `payment-data.txt`.
5. **consolidate_data**: Aggregate data from various sources into a single file.
6. **transform_data**: Transform and stage the data for further analysis.

## Usage Instructions
1. Set up Apache Airflow and configure the `ETL_toll_data` DAG with the provided Python script.
2. Initiate the DAG run manually or wait for the scheduled execution.
3. Upon completion, verify the `transformed_data.csv` file in the designated staging area.

## Requirements
- Python 3.x
- Apache Airflow

## Contributing
Contributions to this educational project are welcome. Please fork the repository, make your changes, and submit a pull request.

## License
MIT License

## Contact
- Name: [Farhad Vadiee]
- Email: [farhad.vadiee@gmail.com]

This project is a part of an educational course and is for demonstration purposes only. The data and scenarios depicted are fictitious. No real data is used or analyzed in this project. Please refer to `fileformats.txt` and `ETL_toll_data.py` for detailed mock data formats and extraction logic.

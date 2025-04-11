#main_pipeline.py

from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data_to_s3
from datetime import datetime


def main():
    # Step 1: Extract data
    print("Starting extraction process...")
    data = extract_data()

    if data:
        # Step 2: Transform data
        print("Starting transformation process...")
        transformed_data = transform_data(data)

        # Step 3: Load data into S3
        if transformed_data:
            print("Starting loading process...")


            load_data_to_s3(transformed_data)
        else:
            print("No transformed data to load.")
    else:
        print("No data extracted to transform.")


if __name__ == "__main__":
    main()
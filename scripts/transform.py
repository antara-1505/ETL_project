import json


def transform_data(data):
    """
    Transform the raw data to a more structured format for further processing.

    Args:
        data (dict): Raw data extracted from the URL.

    Returns:
        dict: Transformed data with structured fields.
    """

    # Step 1: Clean up data (remove unwanted newline characters, etc.)
    def clean_list(input_list):
        """ Helper function to clean lists by removing unwanted newline characters and extra spaces. """
        return [item.replace('\n', '').strip() for item in input_list if item.strip()]

    # Step 2: Transform the data
    transformed_data = {
        "catalogs": clean_list(data.get("catalogs", [])),
        "contributors": clean_list(data.get("contributors", [])),
        "product_types": clean_list(data.get("producttypes", [])),
        "event_types": clean_list(data.get("eventtypes", [])),
        "magnitude_types": clean_list(data.get("magnitudetypes", [])),
    }

    # You could also add more transformations, such as:
    # - Creating categories or statistics about the events
    # - Filtering events based on certain conditions
    # - Structuring data for visualization, etc.

    return transformed_data
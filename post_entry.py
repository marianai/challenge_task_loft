"""
NetBox API POST request.
Python script to add a journal entry to a device using NetBox API.
"""

import requests


def add_journal_entry(
        url: str, token: str, data: dict,
        ) -> None:
    """
    This function is adding a new journal entry to a device.

    Parameters:
       - url (str): The URL of the NetBox instance.
       - token (str): The NetBox API token for authentication.
       - data(dict): The new journal entry of the device.

    Returns:
       None: Prints the result of the POST request.
    """

    # Inserted headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {token}",
    }

    response = requests.post(url, json=data, headers=headers)
    # Check if new entry is created or failed
    if response.status_code == 201:
        print(response.json)
    else:
        print(f"Status code: {response.status_code} and {response.text}")


def main():
    """
    This function is main function of the script.

    Returns:
        None
    """

    # Formated netbox_url for correct endpoint
    url = "http://localhost:8000/api/dcim/journal-entries/"
    token = "18f87a99ade85efb4e92de4ee1631838b0dfedca"

    # Journal entry data
    journal_entry = {
        "assigned_object_type": "ipam.ipaddress",
        "assigned_object_id": "123",
        "comments": "Adding new object ipam.ipaddress with ID of 123.",
    }
    # Call the add_journal_entry function
    add_journal_entry(url, token, journal_entry)


if __name__ == "__main__":

    # Calls the main function.
    main()

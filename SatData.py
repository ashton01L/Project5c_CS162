# Author: Ashton Lee
# Github User: ashton01L
# Date: 10/30/2024
# Description:
import json


class SatData:
    """



    """
    def __init__(self, filepath):
        """



        :param filepath:
        """
        with open("sat.json", 'r') as file:
            data = json.load(file)

        # Extract the relevant data
        self._data = []
        for entry in data["data"]:
            self._data.append({
                "DBN": entry[8],  # DBN is at index 8
                "School Name": entry[9],  # School Name is at index 9
                "Number of SAT Test Takers": entry[10],  # Number of Test Takers is at index 10
                "SAT Critical Reading Avg. Score": entry[11],  # Critical Reading Mean is at index 11
                "SAT Math Avg. Score": entry[12],  # Mathematics Mean is at index 12
                "SAT Writing Avg. Score": entry[13]  # Writing Mean is at index 13
            })

    def save_as_csv(self, dbns):
        """



        :param dbns:
        :return:
        """
        import csv

        # Define the column headers
        headers = [
            "DBN", "School Name", "Number of SAT Test Takers",
            "SAT Critical Reading Avg. Score", "SAT Math Avg. Score", "SAT Writing Avg. Score"
        ]

        # Filter the data based on the DBNs provided and sort by DBN
        filtered_data = sorted(
            [entry for entry in self._data if entry["DBN"] in dbns],
            key=lambda x: x["DBN"]
        )

        # Write to CSV
        with open("output.csv", "w", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(filtered_data)

# Sample usage
sat_data = SatData("sat.json")
dbns = ["02M303", "02M294", "01M450", "02M418"]
sat_data.save_as_csv(dbns)
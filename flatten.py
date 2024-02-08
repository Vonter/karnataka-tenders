import csv
import numpy as np
import os
import pandas as pd
import re
import sys

import json

csvColumns = ["Tender Number", "Status", "Estimated Value", "Title", "Department", "Location", "Category", "Description", "Published Date"]
tenderScheduleColumns = ["tenderNumber", "status", "ecv", "title", "deptName", "locationName", "category", "description"]
noticeInvitingTenderDTOColumns = ["publishedDate"]
jsonColumns = {"tenderSchedule": tenderScheduleColumns, "noticeInvitingTenderDTO": noticeInvitingTenderDTOColumns}

tendersDataFrame = pd.DataFrame()

def flatten_data():

    # Initialize an empty list to hold DataFrames
    dfs = []

    # Iterate over JSON files
    for root, dirs, files in os.walk("./raw"):
        for file in files:
            if file.endswith('.json'):

                # Initialize an empty list to hold tender details
                tender = []

                # Parse the JSON file
                try:
                    with open(os.path.join(root, file), 'r') as file_h:
                        data = json.load(file_h)
                        for columnList in jsonColumns.keys():
                            for column in jsonColumns[columnList]:
                                tender.append(data[columnList][column])
                except KeyboardInterrupt:
                    raise
                except Exception as err:
                    print("ERROR: Failed to process {}/{}".format(root, file))
                    continue

                # Create a DataFrame using the list
                df = pd.DataFrame(data=[tender], columns=csvColumns)
                dfs.append(df)

    # Combine tenders across directories into a tendersDataFrame
    tendersDataFrame = pd.concat(dfs, ignore_index=True)

    # Configure the datatype of columns in the tendersDataFrame
    tendersDataFrame['Estimated Value'] = np.floor(tendersDataFrame['Estimated Value'].astype(float)).astype(int)
    tendersDataFrame['Published Date'] = pd.to_datetime(tendersDataFrame['Published Date'])

    # Sort the DataFrame by the 'Published Date' column in descending order
    tendersDataFrame = tendersDataFrame.sort_values(by='Published Date', ascending=False)

    # Save the tendersDataFrame as a CSV file
    tendersDataFrame.to_csv("csv/AllTenders.csv", index=False, sep=";", quoting=csv.QUOTE_ALL)

    # Save the latest 5000 tenders separately
    tendersDataFrame = tendersDataFrame.head(5000)
    tendersDataFrame.to_csv("csv/LatestTenders.csv", index=False, sep=";", quoting=csv.QUOTE_ALL)

flatten_data()

import json
import pandas as pd
import matplotlib.pyplot as plt
import os

def read_covid_data(directory):
    all_covid_data=[]
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                filepath=os.path.join(root,file)
                with open(filepath,"r") as jsonfile:
                    data=json.load(jsonfile)
                    all_covid_data.append(data)
    return all_covid_data

def calculate_stats(covid_data):
    stats=[]
    for data in covid_data:
        confirmed_cases=data["confirmed_cases"]["total"]
        deaths=data["death"]["total"]
        recovered=data["recovered"]["total"]
        active_cases=confirmed_cases-deaths-recovered

        stats.append({
            "Country":data["country"],
            "Total Confirmed Cases": confirmed_cases,
            "Total Deaths":deaths,
            "total recovered cases": recovered,
            "total active cases":active_cases,

        })

    return stats

def generate_summary_report(stats):
    with open("covid19_summary.json","w") as jsonfile:
        json.dump(stats,jsonfile,indent=2)


if __name__=="__main__":
    covid_data_directory="data.json"
    covid_data=read_covid_data(covid_data_directory)
    stats=calculate_stats(covid_data)

    sorted_stats=sorted(stats, key=lambda x: x["Total Confirmed Cases"], reverse=True)
    top_5_highest_cases=sorted_stats[:5]
    top_5_lowest_cases=sorted_stats[-5:][::-1]

    generate_summary_report(stats)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import webbrowser
import os

examName = "my-2nd-sem"
# examName = "my-1st-sem"


def printPassFailCount(data):
    Failed = sum([1 for i in data.keys() if data[i]['Result'] == "FAIL"])
    Passed = len(data)-Failed
    print("Total : " + str(len(data)))
    print("Passed : " + str(Passed))
    print("Failed : " + str(Failed))


def printGrandTotalCompareInHTML(data):
    totals = [data[i]["Grand Total"] for i in data.keys()]
    names = [data[i]["Student Name"] for i in data.keys()]
    str = "<table><tr><th>Name</th><th>Grand Total</th></tr>"
    for i in range(len(names)):
        str += "<tr><td>"+names[i]+"</td><td>"+totals[i]+"</td></tr>"
    str += "</table>"
    f1 = open("report1.html", 'w+')
    f1.write(str)
    f1.close()
    webbrowser.get('windows-default').open(os.path.realpath('report1.html'))


f = open('rtu-data\\'+examName+".json", 'r')
data = json.loads(f.read())
f.close()

# printPassFailCount(data)
# printGrandTotalCompare(data)

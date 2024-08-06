# Python program to read
# json file

import json
import os

# Opening JSON file
f = open('artifacts/16.1.0/oc-ibm-pak.json')

# returns JSON object as 
# a dictionary
data = json.load(f)

## list of pages
components = ["navigator",
              "asset-repo",
              "apiconnect",
              "appconnect",
              "mq",
              "ep",
              "flink",
              "eventstreams",
              "eem",
              "datapower",
              "aspera",
              "common-services"
]

for x in components:
    os.system("oc ibm-pak get " + data[x]["package"] + " --version " + data[x]["version"] )
    os.system("oc ibm-pak generate mirror-manifests " + data[x]["package"] + " icr.io --version " + data[x]["version"])

# Iterating through the json
# list
 
 

# Closing file
f.close()
with open('evaluation/agglomerative.json', 'r') as file:
    agglomerative = json.load(file)

with open('evaluation/dbscan.json', 'r') as file:
    dbscan = json.load(file)

with open('evaluation/hdbscan.json', 'r') as file:
    hdbscan = json.load(file)

with open('evaluation/optics.json', 'r') as file:
    optics = json.load(file)

with open('evaluation/meanshift.json', 'r') as file:
    meanshift = json.load(file)

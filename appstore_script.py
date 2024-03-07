import requests

def find_bundle_ids(app_names):
    bundle_ids = []
    for app_name in app_names:
        url = f"https://itunes.apple.com/search?term={app_name}&entity=software&limit=1"
        response = requests.get(url)
        data = response.json()
        
        if data["resultCount"] > 0:
            bundle_id = data["results"][0]["bundleId"]
            bundle_ids.append((app_name, bundle_id))
    
    return bundle_ids

# Read app names from a text file
with open("app_names.txt", "r") as file:
    app_names = file.read().splitlines()

bundle_ids = find_bundle_ids(app_names)

if bundle_ids:
    with open("bundle_ids.txt", "w") as file:
        for app_name, bundle_id in bundle_ids:
            file.write(f"App Name: {app_name}\n")
            file.write(f"Bundle ID: {bundle_id}\n")
            file.write("\n")
    print("App names and bundle IDs exported to bundle_ids.txt file.")
else:
    print("Bundle IDs not found for the entered app names.")
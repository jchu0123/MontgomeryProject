import urllib.request
import os

urls = {
    "search_results.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sX2MzNDAzZTQyNDRiMjQ4ZjBiZWY0MTFjNTMyY2ViMjFjEgsSBxDpvbvmoQgYAZIBJAoKcHJvamVjdF9pZBIWQhQxNDQyODUwMTQxMjk3MjA5NDQ4Nw&filename=&opi=89354086",
    "school_details_1.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sXzEzOGI5ODMxM2RmYzQ4MmQ4ZWNlOWYzZGRiNDY5YjQ0EgsSBxDpvbvmoQgYAZIBJAoKcHJvamVjdF9pZBIWQhQxNDQyODUwMTQxMjk3MjA5NDQ4Nw&filename=&opi=89354086",
    "school_details_2.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sX2I5Zjk0M2ZjMjExZTRmZDNhZTg2OTMxMzAxZGY4MWVkEgsSBxDpvbvmoQgYAZIBJAoKcHJvamVjdF9pZBIWQhQxNDQyODUwMTQxMjk3MjA5NDQ4Nw&filename=&opi=89354086",
    "home.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sXzc5ZDMyODk0NWY3MDQzYzBiZTI1NzY4OTdmZTdjNmUyEgsSBxDpvbvmoQgYAZIBJAoKcHJvamVjdF9pZBIWQhQxNDQyODUwMTQxMjk3MjA5NDQ4Nw&filename=&opi=89354086"
}

os.makedirs("SchoolBrowser", exist_ok=True)
for filename, url in urls.items():
    filepath = os.path.join("SchoolBrowser", filename)
    print(f"Downloading {filename}...")
    try:
        urllib.request.urlretrieve(url, filepath)
        print(f"Saved to {filepath}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")

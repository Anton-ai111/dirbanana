import requests

def find_directories(url, directories):
    found_directories = []
    
    for directory in directories:
        full_url = f"{url.rstrip('/')}/{directory}"
        response = requests.get(full_url)
        if response.status_code == 200:
            found_directories.append(full_url)
            print(f"Found: {full_url}")
        else:
            print(f"Not Found: {full_url}")
    
    return found_directories
common_directories = ['admin', 'images', 'uploads', 'css', 'js', 'login', 'dashboard']
url = input("Enter the website URL: ")
found = find_directories(url, common_directories)
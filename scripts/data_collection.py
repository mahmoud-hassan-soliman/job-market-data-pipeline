import requests
import json

url = "https://remotive.com/api/remote-jobs"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    jobs = data['jobs']

    print("Total jobs:", len(jobs))

    for job in jobs[:5]:
        print(job['title'], "-", job['company_name'])

    with open("jobs.json", "w") as f:
        json.dump(jobs, f, indent=2)

else:
    print("Failed to fetch data")

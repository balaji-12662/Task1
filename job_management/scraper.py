# # scraper.py

# import requests
# from bs4 import BeautifulSoup

# def scrape_job_description(job_title):
#     # Example URL format for LinkedIn job search (check if it's the correct one)
#     url = f'https://www.linkedin.com/jobs/search/?keywords={job_title}'

#     # Make the request
#     response = requests.get(url)
    
#     if response.status_code != 200:
#         return f"Failed to retrieve data. Status code: {response.status_code}"
    
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # Example of scraping logic
#     job_listings = []
#     for job in soup.find_all('li', {'class': 'result-card'}):
#         job_data = {
#             'job_title': job.find('h3').get_text(strip=True),
#             'company_name': job.find('h4').get_text(strip=True),
#             'location': job.find('span', {'class': 'job-result-card__location'}).get_text(strip=True),
#         }
#         job_listings.append(job_data)
    
#     if job_listings:
#         return job_listings
#     else:
#         return "No job listings found."

import logging
import requests
from bs4 import BeautifulSoup
import time


def scrape_job_description(job_title):
    url = f"https://www.linkedin.com/jobs/search/?keywords={job_title}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return f"Failed to retrieve data. Status code: {response.status_code}"

    soup = BeautifulSoup(response.content, 'html.parser')

    print(soup.prettify()[:1000])  # Debugging: Output the first 1000 characters of the HTML

    job_listings = soup.find_all('div', class_='job-card-container')
    if job_listings:
        job_data = []
        for job in job_listings:
            title = job.find('h3', class_='job-card-list__title')
            company = job.find('h4', class_='job-card-list__company-name')
            location = job.find('span', class_='job-card-list__location')

            if title and company and location:
                job_data.append({
                    'title': title.get_text(strip=True),
                    'company': company.get_text(strip=True),
                    'location': location.get_text(strip=True)
                })

        print(job_data)  # Debugging: Output the scraped job data
        if job_data:
            return job_data
        else:
            return "No job listings found."
    else:
        return "No job listings found."

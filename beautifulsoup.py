from bs4 import BeautifulSoup
import requests

url = "https://www.irs.gov/e-file-providers/foreign-country-code-listing-for-modernized-e-file-mef"

response = requests.get(url)

content = response.text

soup = BeautifulSoup(content, 'lxml')

# print(soup.prettify())

countries = soup.find_all('td')
# print(countries)

country_list = []
# Iterate through the 'td' elements
for i in range(0, len(countries), 2):
    country_name = countries[i].get_text(strip=True)
    country_code = countries[i + 1].get_text(strip=True)
    country_list.append(f"{country_code}: {country_name}")

# Write the country names and codes to a file
with open("countries.txt", "w") as file:
    for country in country_list:
        file.write(country + "\n")

print("Country data saved to countries.txt")

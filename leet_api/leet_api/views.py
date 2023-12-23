# yourapp/views.py
from django.http import JsonResponse
import requests 
from bs4 import BeautifulSoup
def ma(username):
    data = {}
    url = f'https://leetcode.com/{username}/'
    # Send a GET request to the URL
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'lxml')

        try:
            # Extract Rank
            tags_rank = soup.find_all('span', class_='ttext-label-1')
            if tags_rank:
                data['rank'] = int(tags_rank[0].text.replace('Rank ', '').replace(',', ''))

            # Extract Solved
            tags_solved = soup.find_all('div', class_='text-[24px] font-medium text-label-1 dark:text-dark-label-1')
            if tags_solved:
                data['Solved'] = int(tags_solved[0].text.split('/')[0])

            # Extract Easy, Medium, and Hard
            tags_all = soup.find_all('span', class_='mr-[5px] text-base font-medium leading-[20px] text-label-1 dark:text-dark-label-1')

            for index, tags in enumerate(tags_all):
                taxt = tags.text
                text = taxt.split('/')

                if index == 0:
                    data['Easy'] = int(text[0])
                elif index == 1:
                    data['Medium'] = int(text[0])
                elif index == 2:
                    data['Hard'] = int(text[0])

            # Extract Rating
            tags_rating = soup.find_all('div', class_='text-label-1 dark:text-dark-label-1 flex items-center text-2xl')
            if tags_rating:
                data['rating'] = int(''.join(c for c in tags_rating[0].text if c.isdigit()))

        except Exception as e:
            print(f"Error extracting data: {e}")

        # Return the data dictionary
        return data

    else:
        print(f"Failed to fetch content. Status code: {response.status_code}")
        # Return an empty dictionary if the request fails
        return {}


def leetcode_data(request, username):
    if request.method == 'GET':
        data = ma(username)
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'GET request required.'})

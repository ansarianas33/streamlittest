import requests
import streamlit as st

API_KEY = '871a09e5c981848880b9563ce55a2eb0307cdde9d5f69dbb1db3cef0f8a5da6d'
BASE_URL = 'https://serpapi.com/search.json'

COUNTRY_CODES = {
    'United States': 'us',
    'United Kingdom': 'uk',
    'Canada': 'ca',
    'Australia': 'au'
}

def fetch_search_results(query, location, url):
    params = {
        'q': query,
        'location': location,
        'google_domain': 'google.com',
        'api_key': API_KEY,
        'uule': url
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    st.title('Search Engine Rank Tracker')

    query = st.text_input('Enter a search query')
    country = st.selectbox('Select a country', list(COUNTRY_CODES.keys()))
    url = st.text_input('Enter the website URL')

    if st.button('Submit'):
        if query and country and url:
            location = COUNTRY_CODES[country]
            results = fetch_search_results(query, location, url)
            if results:
                st.write(results)
            else:
                st.error('Error fetching search results')
        else:
            st.warning('Please fill in all the fields')

if __name__ == '__main__':
    main()

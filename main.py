import requests
import json

def write_movies(movies, user, title_type):
    filename = f'export_{title_type}.csv'
    with open(filename, 'a', encoding='utf-8') as f:
        for m in movies:
            title = '"' + m['title'] + '"'
            year = m['year']
            rating = m['rating_scores'][user]
            imdbID = m['imdb_id']
            line = f'\n{title},{year},{rating},{imdbID}'
            if m['type'] == title_type:
                f.write(line)

# for movie in response['results']:
#     print(movie['original_title'])

if __name__ == '__main__':
    title_type = 'series'
    filename = f'export_{title_type}.csv'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('Title,Year,Rating10,imdbID')
    
    user = '896acc70-8385-44b2-a660-a704dca97b54'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'}
    next_url = 'https://atlas.playpilot.tech/api/v1/titles/browse/?region=no&include_count=false&exclude_hidden_titles=true&language=en-US&page=1&ordering=-rated_at,-score&rated_by=896acc70-8385-44b2-a660-a704dca97b54&include_ratings_by=896acc70-8385-44b2-a660-a704dca97b54&no_region_filter=true'

    count = 0
    while next_url is not None:
        response = json.loads(requests.get(next_url, headers=headers).text)
        next_url = response['next']
        write_movies(response['results'], user, title_type)
        count += len(response['results'])
        print(count)
        

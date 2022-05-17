import requests
import json

file_path = "./language_info.json"

# ISO 3166-1 변환용 json
with open(file_path, 'r') as file:
    language_info = json.load(file)


# data['key'] 형태의 딕셔너리의 키값을 찾는 형태에서 data.get('key')로 변경
# key값이 없을때 나는 에러 처리

def get_movie_datas():
    data = []
    print('인기 영화 목록')
    print('--------------------------------------------------------------')
    cnt = 1
    character_id = 1
    counrty_rel_id = 1

    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(1, 2):
        

        # popular api
        request_url = f"{BASE_URL}/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()


        
        for movie in movies.get('results'): 
            movie_id = movie.get('id')
            movie_name = movie.get('title')
            print(f'#{cnt} {movie_name}')
            cnt += 1
            


            # 디테일 api
            request_url_detail = f"{BASE_URL}/{movie_id}?api_key={TMDB_API_KEY}&language=ko-KR"
            movie = requests.get(request_url_detail).json()

            # 장르 id
            genre_ids = []
            for genre in movie.get('genres'):
                genre_ids.append(genre.get('id'))

            # 제작 국가 정보
            countries = []
            for country in movie.get('production_countries'):
                country_name = country.get('iso_3166_1')
                country_id = language_info[country_name.lower()]
                countries.append(country_id)

                movie_country.append({
                        'model': 'movies.productioncountry',
                        'pk': country_id,
                        'fields': {
                            'name': country_name,
                        }
                    })

                movie_country_rel.append({
                        'model': 'movies.moviecountry',
                        'pk': counrty_rel_id,
                        'fields': {
                            'movie_id': movie_id,
                            'country_id': country_id,
                            'country_name': country_name,
                        }
                    })
                counrty_rel_id += 1

            # 트레일러 api
            request_url_trailer = f'{BASE_URL}/{movie_id}/videos?api_key={TMDB_API_KEY}&language=ko-KR'
            trailer = requests.get(request_url_trailer).json()
            

            # 트레일러 key
            trailer_key = ''
            if trailer.get('results'):
                trailer_item = trailer.get('results')[0]
                trailer_key = trailer_item.get('key')

            
            # credit api
            request_url_credit = f'{BASE_URL}/{movie_id}/credits?api_key={TMDB_API_KEY}&language=ko-KR'
            credits = requests.get(request_url_credit).json()

            actors_list = credits.get('cast')
            crew_list = credits.get('crew')


            # 배우 id
            actors = []
            for actor in actors_list:
                if actor.get('order') < 6:
                    actor_id = actor.get('id')
                    actors.append(actor_id)
                    actors_id.add(actor_id)
                    
                    castings.append({
                        'model': 'movies.characters',
                        'pk': character_id,
                        'fields': {
                            'movie_id': movie_id,
                            'actor_id': actor_id,
                            'character_name': actor.get('character'),
                        }
                    })
                    character_id += 1
                else:
                    break

            # 감독 id
            director = []
            for direct in crew_list:
                if direct.get('job') == 'Director':
                    director_id =  direct.get('id')
                    director.append(director_id)
                    directors_id.add(director_id)
                    break

            
            # 비슷한 영화 api
            request_url_similar= f'{BASE_URL}/{movie_id}/similar?api_key={TMDB_API_KEY}&language=ko-KR&page=1'
            movie_similars = requests.get(request_url_similar).json()

            # 비슷한 영화 id
            similar_movies = []
            for similar in movie_similars.get('results'):
                similar_movies.append(similar.get('id'))

            
            fields = {
                'title': movie_name,
                'released_date': movie.get('release_date'),
                'popularity': movie.get('popularity'),
                'vote_avg': movie.get('vote_average'),
                'overview': movie.get('overview'),
                'poster_path': movie.get('poster_path'),
                'adult': movie.get('adult'),
                'production_countries': countries,
                'runtime': movie.get('runtime'),
                'status': movie.get('status'),
                'tagline': movie.get('tagline'),
                'genre_ids': genre_ids,
                'trailer_youtube_key': trailer_key,
                'actors': actors,
                'director': director,
                'movie_similar': similar_movies,
            }
            record = {
                'model': 'movies.movie',
                'pk': movie_id,
                'fields': fields,
            }
            data.append(record)
        popular_movies.extend(data)

def get_person_datas(person_ids, model):
    person_list = []
    cnt = 1

    print(model)
    print('-----------------------------------------------------------')

    for person_id in person_ids:
        request_url_person = f'https://api.themoviedb.org/3/person/{person_id}?api_key={TMDB_API_KEY}&language=ko-KR'
        person = requests.get(request_url_person).json()
        name = person.get('name')
        print(f'#{cnt} {name}')
        cnt += 1

        record = {
            'model': f'movies.{model}',
            'pk': person.get('id'),
            'fields': {
                'name': name,
                'profile_path': person.get('profile_path'),
            },
        }
        person_list.append(record)

    return person_list


def write_json_file(filename, total_data):
    with open(filename, 'w', encoding='UTF8') as file:
        json.dump(total_data, file, ensure_ascii=False, indent=2)


TMDB_API_KEY =  '9a1be42b20cb9255e18beb22379b225e' 
BASE_URL = 'https://api.themoviedb.org/3/movie'

actors_id = set()
directors_id = set()

movie_country = []
popular_movies = []
castings = []
movie_country_rel = []

get_movie_datas()

write_json_file('country_rel.json', movie_country_rel)
write_json_file('country.json', movie_country)
write_json_file('movies.json', popular_movies)
write_json_file('castings.json', castings)

print('\n')

actors = get_person_datas(actors_id, 'actor')

print('\n')

directors = get_person_datas(directors_id, 'director')

write_json_file('actors.json', actors)
write_json_file('directors.json', directors)

print('-----------------------------------------------------------')
print(f'인기 영화 : {len(popular_movies)}')
print(f'배우 : {len(actors)}')
print(f'감독 : {len(directors)}')
print('-----------------------------------------------------------')
# views.py

from banjo.urls import route_get, route_post
from settings import BASE_URL
from .models import Quotes
from fuzzywuzzy import fuzz
#Route to create a new quote with difficulty answers categories.
@route_post(BASE_URL + 'newquote', args={'quote':str, 'difficulty': str, 'answer': str, 'category':str})
def new_quote(args):
    new_quote = Quotes(
        quote = args['quote'],
        difficulty = args['difficulty'],
        answer = args['answer'],
        category = args['category'],
        likes = 0,
    )

    new_quote.save()

    return {'Quote': new_quote.json_response()}
#Route to find all quotes
@route_get(BASE_URL + 'all')
def all_quotes(args):
    quote_list = []

    for quote in Quotes.objects.all():
        quote_list.append(quote.json_response_answerless())

    return {'quotes':quote_list}

#Route for user to guess quote
@route_post(BASE_URL + 'guess', args={'guess': str, 'id': int})
def guess_quote(args):
    if Quotes.objects.filter(id=args['id']).exists():
        one_quote = Quotes.objects.get(id=args['id'])

        if one_quote.check_guess(args['guess']) == True:
            return {'Quote': one_quote.json_response_correct_guess()}
        
        else:
            return {'Quote': one_quote.json_response_incorrect_guess()}
        
    else:
        return{'error': 'quote not found, please try again.'}
#Route for all quotes but with answers    
@route_get(BASE_URL + 'all_answers')
def all_quotes(args):
    quote_list = []

    for quote in Quotes.objects.all():
        quote_list.append(quote.json_response())

    return {'quotes':quote_list}
#Route for finding quotes with a certain difficulty
@route_get(BASE_URL + 'difficultysearch', args={'difficulty':str})
def difficultyfinder(args):
    quote_list = []

    for difficultyfinder in Quotes.objects.filter(difficulty__contains= args['difficulty']):
       quote_list.append(difficultyfinder.json_response_answerless())
    
    return {'quotes':quote_list}

#Route to add hint
@route_post(BASE_URL + 'add_hint', args={'id':int, 'new_hint':str})
def add_hints(args):
    if Quotes.objects.filter(id=args['id']).exists():
        add_hints = Quotes.objects.get(id=args['id'])
        add_hints.add_hint(args['new_hint'])
        return {'Quote': add_hints.json_response_answerless()}
    else:
        return{'error': 'Unable to add hint, please try again.'}
    
#Route to find quotes from a specific person author or answer
@route_get(BASE_URL + 'specific_person', args={'author':str})
def personsearch(args):
    quote_list = []
   
    for personsearch in Quotes.objects.filter(answer__contains=args['author']):
        quote_list.append(personsearch.json_response_answerless())
    
    return {'quotes': quote_list}


#Route to like a certain quote
@route_post(BASE_URL + 'like', args={'id':int})
def increase_likes(args):
    if Quotes.objects.filter(id=args['id']).exists():
        increase_likes = Quotes.objects.get(id=args['id'])
        increase_likes.increase_likes()

        return {'Quotes': increase_likes.json_response_answerless()}
    else:
        return {'error': 'Unable to like, please try again' }
#Route to find all categories
@route_get(BASE_URL + 'categories')
def all_categories(args):
    category_list = ['Sports','Lyrics','Movies', 'Influential figures']
    return {'categories':category_list}

#Route to find all quotes with specific category
@route_get(BASE_URL + 'specific_category', args={'category':str})
def category_search(args):
    quote_list = []

    for category_search in Quotes.objects.filter(category__contains=args['category']):
        quote_list.append(category_search.json_response_answerless())
    
    return {'quotes': quote_list}

#Route to find leaderboard with the most likes
@route_get(BASE_URL + 'popularity_leaderboard')
def famous_quote(args):
    quote_list = []
    for quote in Quotes.objects.order_by('-likes'):
        quote_list.append(quote.json_response_answerless())

    return {'quote_leaderboard':quote_list}
#Route to replace a quote, difficulty, answer and category
@route_post(BASE_URL + 'replace_quote', args={'id':int, 'new_quote':str, 'new_answer':str, 'new_difficulty':str, 'new_category': str})
def quote_change(args):
    if Quotes.objects.filter(id=args['id']).exists():
        quote_change = Quotes.objects.get(id=args['id'])
        quote_change.change_quote(
            new_quote = args['new_quote'],
            new_answer = args['new_answer'],
            new_difficulty = args['new_difficulty'],
            new_category = args['new_category']
        )
        return {'Replaced_quote': quote_change.json_response()}
    else:
        return {'error': 'Unable to change quote, please try again' }

#Route to find a random quote
@route_get(BASE_URL + 'random')
def random_quote(args):
    if Quotes.objects.all().exists():
        random_quote = Quotes.objects.order_by('?').first()
        return {'Random_quote': random_quote.json_response_answerless()}
    else:
        return {'error': 'Unable to fetch random quote, please try again' }
    



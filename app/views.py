# views.py

from banjo.urls import route_get, route_post
from settings import BASE_URL
from .models import Quotes
from fuzzywuzzy import fuzz

@route_post(BASE_URL + 'newquote', args={'quote':str, 'difficulty': str, 'answer': str})
def new_quote(args):
    new_quote = Quotes(
        quote = args['quote'],
        difficulty = args['difficulty'],
        answer = args['answer'],
        likes = 0,
    )

    new_quote.save()

    return {'Quote': new_quote.json_response()}

@route_get(BASE_URL + 'all')
def all_quotes(args):
    quote_list = []

    for quote in Quotes.objects.all():
        quote_list.append(quote.json_response_answerless())

    return {'quotes':quote_list}


@route_post(BASE_URL + 'guess', args={'guess': str, 'id': int})
def guess_quote(args):
    if Quotes.objects.filter(id=args['id']).exists():
        one_quote = Quotes.objects.get(id=args['id'])

        if one_quote.check_guess(args['guess']) == True:
            return {'Quote': one_quote.json_response_correct_guess()}
        
        else:
            return {'Quote': one_quote.json_response_incorrect_guess()}
        
    else:
        return{'error': 'no such quote'}
    
@route_get(BASE_URL + 'allanswers')
def all_quotes(args):
    quote_list = []

    for quote in Quotes.objects.all():
        quote_list.append(quote.json_response())

    return {'quotes':quote_list}

@route_get(BASE_URL + 'difficultysearch', args={'difficulty':str})
def difficultyfinder(args):
   quote_list = []

   for difficultyfinder in Quotes.objects.filter(difficulty__contains= args['difficulty']):
       quote_list.append(difficultyfinder.json_response_answerless())
    
       return {'quotes':quote_list}

   else:
       return {'error': 'no riddle exists'}

@route_post(BASE_URL + 'add_hint', args={'id':int, 'new_hint':str})
def add_hints(args):
    if Quotes.objects.filter(id=args['id']).exists():
        add_hints = Quotes.objects.get(id=args['id'])
        add_hints.add_hint(args['new_hint'])
        return {'Fortune': add_hints.json_response_answerless()}
    

@route_get(BASE_URL + 'specificperson', args={'author':str})
def personsearch(args):
   quote_list = []

   for personsearch in Quotes.objects.filter(answer__contains= args['author']):
       quote_list.append(personsearch.json_response_answerless())
    
       return {'quotes':quote_list}

   else:
       return {'error': 'no riddle exists'}

@route_post(BASE_URL + 'like', args={'id':int})
def increase_likes(args):
    if Quotes.objects.filter(id=args['id']).exists():
        increase_likes = Quotes.objects.get(id=args['id'])
        increase_likes.increase_likes()

        return {'Quotes': increase_likes.json_response_answerless()}
    
@route_get(BASE_URL + 'categories')
def all_categories(args):
    category_list = ['Athletes,Artists,Movies,Celebrities']

    for category in Quotes.objects.all():
        category_list.append(category.json_response_answerless())

    return {'categories':category_list}

# @route_get(BASE_URL + 'popularity_leaderboard')
# def famous_quote(args):
#     for famous_quotes in Quotes.objects.all():
#         return {'Quotes':famous_quotes.json_response_answerless()}
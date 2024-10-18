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

@route_get(BASE_URL + 'difficultychange', args={'difficulty':str})
def searchword(args):
   quote_list = []

   for searchword in Quotes.objects.filter(difficulty__contains= args['difficulty']):
       quote_list.append(searchword.json_response_answerless())
    
       return {'quotes':quote_list}

   else:
       return {'error': 'no riddle exists'}

@route_post(BASE_URL + 'addhint', args={'id':int, 'new_hint':str})
def add_hints(args):
    if Quotes.objects.filter(id=args['id']).exists():
        add_hints = Quotes.objects.get(id=args['id'])
        add_hints.add_hint(args['new_hint'])
        return {'Fortune': add_hints.json_response_answerless()}
# views.py

from banjo.urls import route_get, route_post
from settings import BASE_URL
from .models import Quotes

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
        quote_list.append(quote.json_response())

    return {'quotes':quote_list}


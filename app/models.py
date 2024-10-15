# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField

class Quotes(Model):
    quote = StringField()
    hint = StringField()
    likes = IntegerField()
    difficulty = StringField()
    correct_percentage = FloatField()
    answer = StringField()
    guesses = IntegerField()
    correct = IntegerField()


    def json_response(self):
            
            return {
                'id': self.id,
                'quote': self.quote,
                'likes': self.likes,
                'difficulty': self.difficulty,
            }
    
    def json_response_answerless(self):
        return {
            "id": self.id,
            "quote": self.quote,
            "correct": self.correct,
            "guesses": self.guesses
        }
    
    def json_response_incorrect_guess(self):
        return(
            {'id': self.id,
            'question': self.quote,
            'guesses': self.guesses,
            'correct': False}
        )
    
    def json_response_correct_guess(self):
        return(
            {'id': self.id,
            'question': self.quote,
            'guesses': self.guesses,
            'correct': True}
        )
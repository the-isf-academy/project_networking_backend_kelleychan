# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField
from fuzzywuzzy import fuzz

class Quotes(Model):
    quote = StringField()
    hint = StringField()
    likes = IntegerField()
    difficulty = StringField()
    correct_percentage = FloatField()
    answer = StringField()
    guesses = IntegerField()
    correct = IntegerField()

    MIN_FUZZ_RATIO = 80



    def json_response(self):
            
            return {
                'id': self.id,
                'quote': self.quote,
                'likes': self.likes,
                'difficulty': self.difficulty,
                'guesses' : self.guesses,
                'answer' : self.answer
            }
    
    def increase_likes(self):
        self.likes += 1
        self.save()

    def json_response_answerless(self):
        return {
            "id": self.id,
            "quote": self.quote,
            "correct": self.correct,
            'difficulty': self.difficulty,
            'hint' : self.hint,
            'likes' : self.likes,
            'guesses': self.guesses

        }
    
    def json_response_incorrect_guess(self):
        return(
            {'id': self.id,
            'question': self.quote,
            'guesses': self.guesses,
            'difficulty': self.difficulty,
            'correct': False}
        )
    
    def json_response_correct_guess(self):
        return(
            {'id': self.id,
            'question': self.quote,
            'guesses': self.guesses,
            'difficulty': self.difficulty,
            'correct': True}
        )
    def check_guess(self, guess):

        self.guesses += 1
        similarity = fuzz.ratio(guess.lower(), self.answer.lower())
            
        if similarity >= self.MIN_FUZZ_RATIO:
            self.correct+= 1
            self.save()
            return True
        else:
            self.save()
            return False
            
    def add_hint(self, new_hint):
            self.hint = new_hint
            self.save()

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
    category = StringField()

    MIN_FUZZ_RATIO = 80


    # this shows a quote with answer
    def json_response(self):
            
            return {
            "id": self.id,
            "quote": self.quote,
            'difficulty': self.difficulty,
            'category': self.category,
            'answer': self.answer,
            'hint' : self.hint,
            'likes' : self.likes,
            'guesses': self.guesses,
            "correct": self.correct,
            'correct_percentage': self.correct_percent()
                
            }
    #increases like by 1
    def increase_likes(self):
        self.likes += 1
        self.save()
    #shows quote without answer
    def json_response_answerless(self):
        return {
            "id": self.id,
            "quote": self.quote,
            "correct": self.correct,
            'difficulty': self.difficulty,
            'hint' : self.hint,
            'likes' : self.likes,
            'guesses': self.guesses,
            'category': self.category,
            'correct_percentage': self.correct_percent()

        }
    #What it shows when user guesses wrong
    def json_response_incorrect_guess(self):
        return(
            {'id': self.id,
            'question': self.quote,
            'guesses': self.guesses,
            'difficulty': self.difficulty,
            'correct': False}
        )
    #What it shows when user guesses correctly
    def json_response_correct_guess(self):
        return(
            {'id': self.id,
            'question': self.quote,
            'guesses': self.guesses,
            'difficulty': self.difficulty,
            'correct': True}
        )
    #This is how it checks if its correct
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
    
    #Model to add hint        
    def add_hint(self, new_hint):
            self.hint = new_hint
            self.save()
    #Model to change quote
    def change_quote(self, new_quote, new_answer, new_difficulty, new_category):
        self.quote = new_quote
        self.answer = new_answer
        self.difficulty = new_difficulty
        self.category = new_category
        self.save()
    #Model to find the correct percentage
    def correct_percent(self):
        if self.guesses == 0:
            return 0.0
        return (self.correct / self.guesses)* 100
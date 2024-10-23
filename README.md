# Project Networking


> **Don't forget to edit this `README.md` file**
>
> If you're interested in how to format markdown, click [here](https://www.markdownguide.org/basic-syntax/#images-1)

# Unit 0 Project: Animation
>
> This was written in Markdown. If you're interested in how to format Markdown, click [here](https://www.markdownguide.org/basic-syntax/#images-1)
Description: In this game, you're given a quote ranging from many categories such as movies, celebrities, athletes, etc. The objective of the game is to guess where or who the quote came from.

Planning document:
| Method name        | Parameter                                         | What it does                                                    |
|--------------------|---------------------------------------------------|-----------------------------------------------------------------|
| Add_likes          | Likes                                             | Increase likes by 1                                             |
| Add_hint           | Hint                                              | User adds hint to chosen quote                                  |
| Difficulty         | Old difficulty, New difficulty                    | Sets difficulty on quote                                        |
| Correct_percentage | Total guesses, Correct guesses, Incorrect guesses | Calculates the percentages of correct guess of a specific quote |
| Replace_quote      | New quote, Old quote                              | Replaces existing quote with a new quote                        |

| Route name             | HTTP Method | Payload                                | Success JSON                                                                                                     | Error JSON                                                  |
|------------------------|-------------|----------------------------------------|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Categories             | Get         | None                                   | Categories: [Athletes,Artists,Movies,Celebrities]                                                                | Error:"Unable to fetch categories, please try again."       |
| today_quote            | Get         | None                                   | Quote: "I have a dream" Author: Martin Luther King                                                               | Error:"Unable to fetch quote of the day, please try again." |
| popularity_leaderboard | Get         | None                                   | Leaderboard:  Quote: "I have a dream" Likes: 223 Quote " You must be the change you wish to be" Likes:153        | Error:"Unable to fetch leaderboard, please try again."      |
| specific_person        | Get         | person: albert einstein , payload: str | "Imagination is everything" Likes 53 "If you cant explain it simply you dont understand it well enough" Likes 27 | Error:"Unable to find specific person, please try again."   |
| all                    | Get         | None                                   | All quotes                                                                                                       | Error:"Unable to fetch all quotes, please try again."       |
| increase_likes         | Post        | id:int                                 | message: "likes increased successfully" likes:15                                                                 | Error:"Unable to like, please try again."                   |
| add_hint               | Post        | id:int hint:str                        | message: "Hint added successfully" hint: "This quote is from a famous play"                                      | Error:"Unable to add hint, please try again."               |
| New_quote              | Post        | Quote:str                              | message: "Quote added successfully" id:12                                                                        | Error:"Failed to add quote, please try again."              |
| guess                  | Post        | id:int guess:str                       | correct:true message: "Correct! the quote is from Romeo and Juliet."                                             | Error:"Quote not found, please try again."                  |


- `README.md` You're looking at it, or at least the formatted version. (Click "raw" to see the unformatted version.) Every project has a README explaining what it is.
- `project.py` When this is run, it should draw your project. (If your project is well-organized, there might not be much code in `project.py`. Instead, it might import functions from other modules.)




---

## Setup

### Contents

Here's what is included:
- `\app`
    - `models.py` - `Fortune` model
    - `views.py` - endpoints
- `database.sqlite`  
- `README.md` 

**To start a Banjo server:** `banjo` 
- [Banjo Documentation](https://the-isf-academy.github.io/banjo_docs/)




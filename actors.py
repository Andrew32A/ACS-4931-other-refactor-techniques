# by Kami Bigdely
# Extract class

class Actor:
    def __init__(self, first_name, last_name, birth_year, movies, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email

    def is_eligible_for_hiring(self):
        return self.birth_year > 1985

    def send_hiring_email(self):
        print("email sent to: ", self.email)

    def display_info_and_send_email(self):
        if self.is_eligible_for_hiring():
            print(f"{self.first_name} {self.last_name}")
            print('Movies Played: ', end='')
            for m in self.movies:
                print(m, end=', ')
            print()
            self.send_hiring_email()

actors = [
    Actor('elizabeth', 'debicki', 1990, ['Tenet', 'Vita & Virgina', 'Guardians of the Galaxy', 'The Great Gatsby'], 'deb@makeschool.com'),
    Actor('Jim', 'Carrey', 1962, ['Ace Ventura', 'The Mask', 'Dumb and Dumber', 'The Truman Show', 'Yes Man'], 'jim@makeschool.com')
]

for actor in actors:
    actor.display_info_and_send_email()

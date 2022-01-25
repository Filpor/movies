class movies:
    def __init__(self,title,year,category):
        self.title=title
        self.year=year
        self.category=category
        self.views=0
    def __str__(self):
        return f'{self.title} , {self.year}'
    def play(self,step=1):
        self.views+=step
class serial(movies):
        def __init__(self,seasion,episode,*args, **kwargs):
            super().__init__(*args, **kwargs)
            self.seasion=seasion
            self.episode=episode
        def __str__(self):
            return f'{self.title} S{self.seasion} E{self.episode}'
movie1=movies(title="Pulp Fiction", year=1997, category="Dramat")
movie2=movies(title="Zielona Mila", year=1999, category="Dramat")
movie3=movies(title="Matrix", year=1999, category="Si-Fi")
movie4=movies(title="Milczenie owiec", year=1991, category="Thiller")
movie5=movies(title="Shrek", year=2001, category="Komedia")
serial1=serial(title="After Life", year=2018, category="Dramat Komediowy", seasion="01", episode="01" )
serial2=serial(title="Dr house", year=2004, category="Dramat", seasion="02", episode="08")
serial3=serial(title="Breakning Bad", year=2008, category="Kryminał", seasion="03", episode="05")
serial4=serial(title="Sherlock", year=2010, category="Kryminał", seasion="01", episode="03")
serial5=serial(title="Przyjaciele", year=1994, category="Komedia", seasion="07", episode="10")
list1=[serial1,movie1,serial2,movie2,serial3,movie3,serial4,movie4,serial5,movie5]


       

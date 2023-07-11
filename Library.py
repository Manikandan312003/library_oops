class libraryItem():
    def __int__(self):
        self.__id=0;
        self.__title='';
        self.__year=0;

    def getid(self):
        return self.__id

    def gettitle(self):
        return self.__title

    def getyear(self):
        return self.__year

    def setid(self,id):
        self.__id=id

    def settitle(self,title):
        self.__title=title

    def setyear(self,year):
        self.__year=year





class Book(libraryItem):
    def __int__(self):
        self.author=''

    def dispBook(self, id, title, year, author):
        print(id,title,year,author)





class Magazie(libraryItem):
    def __int__(self):
        self.issue=0

    def dispMagazie(self, id, title, year, issue):
        print(id,title,year,issue)



alchemist = Book()
alchemist.setid (123)
alchemist.settitle ('The Alchemist')
alchemist.setyear (2001)
alchemist.author = ('Paul')
alchemist.dispBook(alchemist.getid(), alchemist.gettitle(), alchemist.getyear(), alchemist.author)

fortNight=Magazie()
fortNight.setid( 12)
fortNight.settitle( 'The FortNight')
fortNight.setyear( 1992)
fortNight.issue = 7
fortNight.dispMagazie(fortNight.getid(), fortNight.gettitle(), fortNight.getyear(), fortNight.issue)

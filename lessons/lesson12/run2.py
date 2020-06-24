from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///library1.db', echo=True)

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship(Author, backref=backref('books', order_by=title))

    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author


    def __str__(self):
        return f"{self.id} {self.title} {self.description} {self.author}"
    def __repr__(self):
        return f"{self.id} {self.title}"


# Base.metadata.create_all(engine)  # create tables

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)  # bound session
session = Session()
# author_1 = Author('Richard Dawkins')
# author_2 = Author('Matt Ridley')
# book_1 = Book('The Red Queen', 'A popular science book', author_2)
# book_2 = Book('The Selfish Gene', 'A popular science book', author_1)
# book_3 = Book('The Blind Watchmaker', 'The theory of evolutio', author_1)
# session.add(author_1)
# session.add(author_2)
# session.add(book_1)
# session.add(book_2)
# session.add(book_3)
# # or simply session.add_all([author_1, author_2, book_1, book_2, book_3])
# print(book_3)
# session.commit()
# book_3.description = 'The theory of evolution'  # update the object
# # book_3 in session  # check whether the object is in the session
# # True
# print(book_3)
# session.commit()


query = session.query(Book).order_by(Book.id)
print(query)
books = query.all()
print(books)
for book in books:
    print(book)
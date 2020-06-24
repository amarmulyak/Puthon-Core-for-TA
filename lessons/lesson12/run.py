# import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('sqlite:///library.db', echo=True)
from sqlalchemy.orm import mapper, relation, backref

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text

metadata = MetaData()

authors_table = Table('authors',
                      metadata,
                      Column('id', Integer, primary_key=True),
                      Column('name', String))
books_table = Table('books',
                    metadata,
                    Column('id', Integer, primary_key=True),
                    Column('title', String),
                    Column('description', String),
                    Column('author_id', ForeignKey('authors.id')))
# Column('name', String(50)) is possible
metadata.create_all(engine) # creates the tables

class Author:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Book:
    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author

    def __repr__(self):
        return self.title


mapper(Book, books_table)
mapper(Author, authors_table, properties={
                'books': relation(Book, backref='author')})


insert_stmt = authors_table.insert(bind=engine)
print(type(insert_stmt))
print (insert_stmt)
# INSERT INTO authors (id, name) VALUES (:id, :name)
compiled_stmt = insert_stmt.compile()
print(compiled_stmt.params)
# {'id': None, 'name': None}
insert_stmt.execute(name='Alexandre Dumas') # insert a single entry
insert_stmt.execute([{'name': 'Mr X'}, {'name': 'Mr Y'}]) # a list of entries
metadata.bind = engine # no need to explicitly bind the engine from now on
select_stmt = authors_table.select(authors_table.c.id==2)
result = select_stmt.execute()
print("result start")
print(result)
print("result end")
result.fetchall()
print("result start")

print(result)
print("result end")

# [(1, u'Mr X')]
del_stmt = authors_table.delete()
del_stmt.execute(whereclause=text("name='Mr Y'"))
del_stmt.execute() # delete all

# from sqlalchemy.orm import relationship, backref

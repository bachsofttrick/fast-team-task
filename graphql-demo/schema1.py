import typing
import strawberry

@strawberry.type
class Book:
    title: str
    author: str

@strawberry.type
class BookQuery:
    @strawberry.field
    def books(self) -> typing.List[Book]:
        return get_books()

def get_books():
    return [
        Book(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
        ),
    ]

@strawberry.type
class Query:
    @strawberry.field
    def books_nested_query(self) -> BookQuery:
        return BookQuery()
    
    books: typing.List[Book] = strawberry.field(resolver=get_books)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str) -> Book:
        print(f"Adding {title} by {author}")

        return Book(title=title, author=author)
    
    @strawberry.mutation
    def restart(self, has: str) -> None:
        print(f"Restarting the server", has)

schema = strawberry.Schema(query=Query,mutation=Mutation)
  
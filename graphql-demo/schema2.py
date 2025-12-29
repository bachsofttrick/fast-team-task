import typing
import strawberry

def get_author_for_book(root) -> "Author":
    return Author(name="Michael Crichton")

@strawberry.type
class Book:
    title: str
    author: "Author" = strawberry.field(resolver=get_author_for_book)

def get_books_for_author(root) -> typing.List[Book]:
    return [Book(title="Jurassic Park")]


@strawberry.type
class Author:
    name: str
    books: typing.List[Book] = strawberry.field(resolver=get_books_for_author)


def get_authors(root) -> typing.List[Author]:
    return [Author(name="Michael Crichton")]


@strawberry.type
class Query:
    authors: typing.List[Author] = strawberry.field(resolver=get_authors)
    books: typing.List[Book] = strawberry.field(resolver=get_books_for_author)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str) -> Book:
        # print(f"Adding {title} by {author}")

        return Book(title=title, author=author)
    
    @strawberry.mutation
    def restart(self, has: str) -> None:
        print(f"Restarting the server")

schema = strawberry.Schema(query=Query,mutation=Mutation)
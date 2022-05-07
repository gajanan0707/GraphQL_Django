import decimal
from itertools import product
import graphene
from graphene_django import DjangoObjectType
from .models import Category, Book, Grocery


# "This is a GraphQL type that maps to the Category Django model."
# The CategoryType class inherits from DjangoObjectType, which is a helper class that wraps a Django
# model and provides a GraphQL type for it
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'title')


# The BookType class is a DjangoObjectType that maps the Book model to a GraphQL type
class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'isbn',
            'pages',
            'price',
            'quantity',
            'description',
            'imageurl',
            'status',
            'date_created',
        )


class GroceryType(DjangoObjectType):
    class Meta:
        model = Grocery
        fields = (
            'product_tag',
            'name',
            'category',
            'price',
            'quantity',
            'imageurl',
            'status',
            'date_created',
        )


class Query(graphene.ObjectType):
    # Defining the fields that can be queried.
    categories = graphene.List(CategoryType)
    books = graphene.List(BookType)
    groceries = graphene.List(GroceryType)

    """
    The resolve_books function is a resolver function that returns a list of all the books in the
    database
    
    :param root: The root of the query
    :param info: This is the context of the query. It contains the schema, the query, the variables,
    and the operation name
    :return: A list of all the objects in the database.
    """
    def resolve_books(root, info, **kwargs):
        # Querying a list
        return Book.objects.all()

    def resolve_categories(root, info, **kwargs):
        # Querying a list
        return Category.objects.all()

    def resolve_groceries(root, info, **kwargs):
        # Querying a list
        return Grocery.objects.all()


# Creating a schema that maps the Query class to the root query.
schema = graphene.Schema(query=Query)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        """
        `UpdateCategory` is a mutation that takes in a title and an id, and returns a category with the
        updated title

        :param cls: The class that is being used to create the mutation
        :param root: The root object, which in this case is the Query object
        :param info: This is the context of the request. It contains the request, the user, and the
        schema
        :param title: The title of the category
        :param id: The ID of the category to update
        :return: The category object
        """
        # Mutation to update a category
        title = graphene.String(required=True)
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title, id):
        category = Category.objects.get(pk=id)
        category.title = title
        category.save()

        return UpdateCategory(category=category)


class CreateCategory(graphene.Mutation):
    class Arguments:
        """
        The `mutate` function takes in the arguments defined in the `Arguments` class, and returns the
        fields defined in the `CreateCategory` class

        :param cls: The class of this mutation
        :param root: The root value, which in this case is None
        :param info: This is the context of the query. It contains the request, the user, and the schema
        :param title: The title of the category
        :return: The CreateCategory class is being returned.
        """
        # Mutation to create a category
        title = graphene.String(required=True)

    # Class attributes define the response of the mutation
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title):
        category = Category()
        category.title = title
        category.save()

        return CreateCategory(category=category)

# The BookInput class is a subclass of graphene.InputObjectType. It has the same fields as the Book
# class, but they are all optional
class BookInput(graphene.InputObjectType):
    title = graphene.String()
    author = graphene.String()
    pages = graphene.Int()
    price = graphene.Int()
    quantity = graphene.Int()
    description = graphene.String()
    status = graphene.String()


class CreateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)

    book = graphene.Field(BookType)

    """
    We create a new book object, assign the input values to the book object, and save the book
    object to the database
    
    :param cls: The class itself
    :param root: The root value, which in this case is the Query class
    :param info: This is the context of the query. It contains the request, the schema, and the
    current user
    :param input: The input parameters that were passed to the mutation
    :return: The CreateBook class is being returned.
    """
    @classmethod
    def mutate(cls, root, info, input):
        book = Book()
        book.title = input.title
        book.author = input.author
        book.pages = input.pages
        book.price = input.price
        book.quantity = input.quantity
        book.description = input.description
        book.status = input.status
        book.save()
        return CreateBook(book=book)


# The UpdateBook class is a mutation that takes in an input and an id, and returns a book
class UpdateBook(graphene.Mutation):
    class Arguments:
        """
        The function takes in a book id, and a BookInput object, and returns an UpdateBook object
        
        :param cls: The class of the mutation
        :param root: The root object, which in this case is None because it's the first resolver in the
        chain
        :param info: This is the context of the request. It contains the request object, the current
        user, and the schema
        :param input: The input argument is the input object that we defined earlier
        :param id: The ID of the book to be updated
        :return: The book object is being returned.
        """
        input = BookInput(required=True)
        id = graphene.ID()

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, input, id):
        book = product.objects.get(pk=id)
        book.name = input.name
        book.description = input.description
        book.price = decimal.Decimal(input.price)
        book.quantity = input.quantity
        book.save()
        return UpdateBook(book=book)


# The Mutation class is a subclass of graphene.ObjectType. It contains the fields that are used to
# create and update the data in the database
class Mutation(graphene.ObjectType):
    update_category = UpdateCategory.Field()
    create_category = CreateCategory.Field()
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()


# Creating a schema that maps the Query class to the root query, and the Mutation class
# to the root mutation.
schema = graphene.Schema(query=Query, mutation=Mutation)

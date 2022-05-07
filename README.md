# GraphQL_Django
Integrating GraphQL API into a Django application

# Setup

The first thing to do is to clone the repository:

```sh
$ git clone git@github.com:gajanan0707/GraphQL_Django.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
Let’s check our URL http://120.0.0.1:8000/graphql
```
# GraphQL Query
Let’s try some features to query the data in our database. We’ll do this by using the GraphQL preview which is the play button at the top left of the navigation bar.
```sh
{
  books{
      id
      title
      author
      isbn
      pages 
      price
      quantity
      description
      status
    }
}
```

```sh
mutation {
 create_category:createCategory(title :"Science Fictions") {
  category {
   id,
   title,
  }
 }
}

mutation {
  create_book: createBook(input: {title:"The stranger things", author: "starnge", pages: 80, price: 1200, quantity: 4, description:"a brief description", status: "True"}){
    book {
      id,
      title,
      author,
      pages,
      price,
      quantity,
      description,
      status
    }
  }
}
```

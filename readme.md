## Description

This is a project I made for one of my university classes. It's a simple program
emulating a virtual library. User can borrow and return books from the library. If 
ran with the -f option, you can load custom csv library file instead of the
default one.
<br/><br/>
One "advanced" feature of the app is how the book search was implemented. I chose
the [Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance) algorithm
due to its simplicity.
<br/><br/>
The project also contains some unit tests, but since it was intended to be just a simple 
demonstration, so are the tests. For example even though the UI class is 100% testable, I decided not to write any unit
tests for it, also not every method of the Library class is covered.


## Architectural considerations

I decided to raise errors in case something goes wrong - a book is not found or it's not possible
to return a book, etc. However, even though raising errors was the pythonic way to go when I was learning Python, 
now when the Python lang supports advanced type hinting (unions) I think that an equally valid solution
would be to leverage that fact and return TheExpectedType | TheErrorType and pattern match
on it on the client side - maybe using unions would even be better, as it's more visible
than raising errors.


## How to run the app

1. Install Python v 3.10.4 (add it to PATH)
2. Run: pip install virtualenv
3. Go into the source folder (where the main.py file resides) in the console
   and run python -m venv .\venv
4. In the console type in: venv\Scripts\activate
5. Run python main.py (-f option if you want to import your own library)

## How to run the tests

If you're using PyCharm, it's as simple as right-clicking on the test module and choosing the "Run 'Python tests 
in test...'" option.
<br/><br/>
If you want to run the tests from the console just type in python -m unittest 

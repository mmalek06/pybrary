## Description

This is a project I made for one of my university classes. It's a simple program
emulating a virtual library. User can borrow and return books from the library. If 
run with the -f option, you can load custom csv library file instead of the
default one.
<br/>
The project also contains some unit tests, but since the project was intended to be just a simple 
demonstration, so are the tests.

## How to run it

1. Install Python v 3.10.4 (add it to PATH)
2. Run: pip install virtualenv
3. Go into the source folder (where the main.py file resides) in the console
   and run python -m venv .\venv
4. Run python main.py (-f option if you want to import your own library)

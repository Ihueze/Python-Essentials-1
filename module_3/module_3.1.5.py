"""
Making use of the answers
What can you do with the answer (i.e., the result of a comparison operation) you get from the computer?

There are at least two possibilities: first, you can memorize it (store it in a variable) and make use of it later. How do you do that? Well, you use an arbitrary variable like this:


answer = number_of_lions >= number_of_lionesses
 
The content of the variable will tell you the answer to the question asked.

The second possibility is more convenient and far more common: you can use the answer you get to make a decision about the future of the program.

You need a special instruction for this purpose, and we'll discuss it very soon.

Now we need to update our priority table, and put all the new operators into it. It now looks as follows:

unary operators: +, -, ~
binary operators: +, -, *, /, //, %, **, ==, !=, > >=, <, <=
ternary operator: if ... else ...

"""

Code a program that receives as input a text file (expressions.txt) that contains arithmetic expressions. The program will print a table with every recognized token and its type in the same order as they were found.

 

Types of Tokens

The arithmetic expressions should only contain the following tokens:

Positive integer numbers  (integer)
Positive real numbers  (float)
Operators:
=  (assignment)
+  (sum)
-  (subtract)
*  (product)
/  (division)
Identifiers:
variable
Special symbols:
(   (left parenthesis)
)   (right parenthesis)
 

Main function

You can code any auxiliary function you want but the main function must have the following signature (could change depending on the programming language):

void lexer(string filepath):

where filepath is the pth to the file that contains the expressions, for exaple, expressions.txt.

You can use any programmingn language (except Java). You must check that the code runs in  ReplitLinks to an external site.. Include a folder with all the required files to run the program in replit. 

 

Input

A text file with arithmetic expressions (example below).
There may or may not be space(s) between tokens.
example:

b=7

a = 32.4 *(-8.6 - b)/       6.1

d = a * b

 

Output

Your program should print:

Token

Type

b

variable

=

assignment

7

integer

a

variable

=

assignment

32.4

float

*

product

(

left parenthesis

-

subtract

8.6

float

-

subtract

b

variable

)

right parenthesis

/

division

6.1

float

d

variable

=

assignment

a

variable

*

product

b

variable

 

Rules of tokens

variable names:
Only lower case letters.
Only contain letters. No numbers, underscores, etc.
All numbers are positive.
 

Algorithm

The lexical analyzer must be implemented using a transition table or a graph.
The design of the automaton is a crucial part of the documentation. Use a software tool to draw it (not  by hand). 
Deliverables:

In a zip file named "project1-N.zip" where N is your team number add the following:

Diagram of the automaton (diagram.pdf).
User manual (manual.pdf). Indicating how to run the program and what programming language was used.
The code in a folder that can be uploaded to Replit and an example expressions.txt file with test arithmetic expressions.
The professor may ask during class any team member to explain how the program works.
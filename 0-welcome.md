## Introduction

Welcome to Tyler Donison's Introduction to Data Structures. In the repository, I will attempt to teach about three specific data structures, providing example code using the structures and example problems and solutions.

## O-Notation

One of the most important concepts concerning data structures, and to programing as a whole, is O-Notation. When you are attempting to make a program, it is important to make it efficient and for it to take as little time as possible. O-Notation refers to how efficient a program is.

Let's take the game, Guess Who, for example. It is a game where each player chooses one character out of a pool of 24, and attempts to guess the other player's character.

If we were to write a program to find the correct answer, what would be the most efficient? What would be the least efficient?

The least efficient, would be to iterate through each of the character names, asking, "Is it [name]?" etc. At most this would take as many guesses as there are characters, or an efficiency of O(n), where n is the number of characters. If there were thousands of different characters for example, this would take a very long time. Clearly this would not lead to many wins.

The most efficient, would be if we could ask questions that were to split the number of remaining guesses in half every time. Asking questions that apply to half the group, would reduce the pool by half every time, instead of by 1.

If the pool were 24 characters, the worst-case scenario would look like this:

24 remaining (start)
12 remaining (after 1 question)
6 remaining (after 2 questions)
3 remaining (after 3)
2 remaining (after 4)
1 remaining (after 5, we have the answer)

In the worst-case scenario, this strategy takes, at most, 5 guesses, whereas guessing name by name in the worse scenario would take 24 guesses. Instead of O(n) efficiency, we have O(log n), where log n is where the search is continually divided in half. This notation, O(log n) is the most efficient in programming, allowing our programs to take much less time in the worst-case scenarios. Every "for loop" that we write however (as you would for searching name by name) increases inefficiency by the product of n. A program with a nested for loop for example, would have O(n^2), which is terribly inefficient. The closer we can get to O(log n) or O(1) the better.

## Contact Information

If you have any questions or comments, please feel free to contact me in the following ways:

* Email: tylerdonison@gmail.com
* Linkedin: https://www.linkedin.com/in/tyler-donison-23432b242/

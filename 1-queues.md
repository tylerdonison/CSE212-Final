# Queues

## Introduction

In a restaurant, there is a need to rotate stock to make sure that the oldest food is used first. If they do not do this, food will go bad and money will be wasted. Typically a "First in, First Out" or FIFO system is used. This is where boxes are dated and the oldest stock is rotated to be used first, etc. This structure is used in programming too, and it is called a queue. A queue is a data structure where the oldest stock, or the first position of the data structure is used first, then the next, ect.

![Chicken Nugget Queue](pictures/queue_pic_1.png)

## Disney Land: Queues in Action

An example of this can also be seen in amusement parks, such as Disney Land. Every ride in an amusement part typically has a line of people wanting to ride the ride. This line is a queue. It can be simulated in Python in the following code. This code has a loop that will add 0-1 people to the queue, then, if the roller coaster is at the starting position, it will take the first person in the queue and run the ride. The ride will run while the queue is potentially being added to. The park will eventually close, not allowing more people to queue, and will empty out the queue from the front.

```python
import random
from time import sleep
RIDE_TIME = 2 #how long a ride takes to complete
coaster_progress = RIDE_TIME #where the coaster is, if it equals ride time then it can go again.
ride_queue = []
park_open = 0 #determines when the park is closing, not allowing more queues
park_close = 10
roller_coaster_run = True
max_added = 1
import sys

def add_people_to_queue():
    names = ["Amber", "Bob", "Cathy", "Dude", "Ellen", "Fred", "Greg", "Hannah", "Isaiah", "Jake", "Karen", "Laurel", "Maggie",
    "Nate", "Oliver", "Pete", "Quinn", "Rex", "Steven", "Tyler", "Umbra", "Victor", "Wendy", "Xander", "Yoshi", "Zack"]
    
    added_people = random.randint(0,max_added)
    people = []
    if added_people != 0:
        for i in range(0, added_people):
            person = random.choice(names)
            ride_queue.append(person)
            people.append(person)
        print(f"{people} added to queue.")
    else:
        print("No one was added to the queue.")

def ride_roller_coaster():
    global ride_queue, coaster_progress, RIDE_TIME, roller_coaster_run
    if park_open == park_close and len(ride_queue) == 0: #The park is closed and the queue is empty.
        print("There is no one left in the queue.")
        print("The park is closed.")
        sys.exit()
    elif len(ride_queue) == 0 and RIDE_TIME == coaster_progress: #if there is no one in the queue but the part is open
        print("There is no one in the queue.")
    elif coaster_progress == RIDE_TIME: #if the coaster is back at the start
        person_riding = ride_queue.pop(0) #remove someone from the queue
        coaster_progress = 0 #begin the coaster
        print(f"{person_riding}: Wheee! I'm riding the roller coaster!")
    else:
        coaster_progress += 1 #progress the coaster forward
        print(f"Ride is still in progress: {coaster_progress}")

def main():
    global park_open, park_close   
    while roller_coaster_run:
        if park_open != park_close:
            add_people_to_queue()
            park_open +=1
        else:
            print("The park is closing.")
        ride_roller_coaster()
        print("The following are in the queue:")
        print(ride_queue)
        print()
        sleep(3)

if __name__ == "__main__":
    main()
```
Example output:

![Example Output](pictures/queue_pic_2.png)

## Queues in Programming:

Queues in programming are particularly useful when muliple programs or threads are trying to use the same information. Without a queue of some sort, reading and writing could be a mess. Say we have a variable, X, where we want multiple threads to add to this varible. The left side of the following is likely to occur without queues, whereas the right side is a way that queues solves the issue.

![Programming Read/Write](pictures/queue_pic_3.png)

In a read/write scenario if multiple reads are happening at the same time, then the x variable can be overwritten and data can be scewed. However, if the threads are put in a queue as shown, the data is written and then the queues read it.

## Problem to Solve: Roller Coaster with Multiple Passengers and Cars.

Take the Disney Land code from above and change the max_added variable from line 9 and change it to a 5.

How would you change the program if each roller coaster could take up to 4 riders?

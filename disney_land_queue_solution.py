import random
from time import sleep
RIDE_TIME = 2 #how long a ride takes to complete
coaster_progress = RIDE_TIME #where the coaster is, if it equals ride time then it can go again.
ride_queue = []
park_open = 0 #determines when the park is closing, not allowing more queues
park_close = 10
roller_coaster_run = True
import sys
max_added = 5

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
        if len(ride_queue) <= 4:
            for _ in range (0, len(ride_queue)):
                person_riding = ride_queue.pop(0) #remove someone from the queue
                coaster_progress = 0 #begin the coaster
                print(f"{person_riding}: Wheee! I'm riding the roller coaster!")
        
        else:
            for _ in range(0,4):
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
            RIDE_TIME = 0
        ride_roller_coaster()
        print("The following are in the queue:")
        print(ride_queue)
        print()
        sleep(3)

if __name__ == "__main__":
    main()
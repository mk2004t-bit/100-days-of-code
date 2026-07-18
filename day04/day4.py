# randomisation in python

import random
import mymodule
N = random.randint(0,1)
if N == 0:
  print("Head")
else:
  print("Tales")

# who pays bill using list and randomisation

people = mymodule.people
paid = mymodule.paid

random_index = random.randint(0,5)
print(random_index)
print(people[random_index])
paid.append(people[random_index])

print(paid)
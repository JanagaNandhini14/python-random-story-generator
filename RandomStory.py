import random

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On Monday']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['Ali', 'Maya', 'John', 'Lilly', 'Tom']
residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university', 'school', 'laundry', 'park']
happened = ['made a lot of friends', 'learned Python', 'ate a burger', 'found a treasure', 'wrote a book']

print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) +
      ', went to the ' + random.choice(went) + ' and ' + random.choice(happened) + '.')

import copy
import random

class Hat: 
  
  def __init__(self, **colors):
    self.contents = [] 

    for key, value in colors.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, num):
    self.drawn_items = []
    n = min(num, len(self.contents))

    for i in range(n):
      drawn_item = self.contents.pop(random.randrange(len(self.contents)))
      self.drawn_items.append(drawn_item)
    
    return self.drawn_items

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  for i in range(num_experiments):
    copy_hat = copy.deepcopy(hat)
    balls_drawn = copy_hat.draw(num_balls_drawn)
    balls_req = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
    m += 1 if balls_req == len(expected_balls) else 0

  return m / num_experiments  
     
import random

class SantaList:
  def __init__(self):
    self.participants = []
    self.assignments = {}

  def addParticipant(self, name):
    self.participants.append(name)

  def assignGifters(self):
    if len(self.participants) < 2:
      print('Not enough participants')
      return
      
    ## Randomize order of participants
    random.shuffle(self.participants)
    ## Reset assignments
    self.assignments = {}
    for i in range(len(self.participants) - 1):
      self.assignments[self.participants[i]] = self.participants[i + 1]
    self.assignments[self.participants[-1]] = self.participants[0]

  def printAssignments(self):
    for key in self.assignments:
      print(key + ' is assigned to ' + self.assignments[key])

  def validPermutation(self):
    gifters = {}
    receivers = {}

    for key in self.assignments:
      if key == self.assignments[key]:
        return False
      gifters[key] = 0
      receivers[self.assignments[key]] = 0

    if((len(gifters) != len(self.participants)) or (len(receivers) != len(self.participants))):
      return False
      
    return True

# Author: Cole Carter ctc5367@psu.edu
# Collaborator: Mark Del Grande mxd5728@psu.edu
# Collaborator: Zak Young zjy5116@psu.edu
# Collaborator: Ethan Moyer epm5482@psu.edu
# Section: 5
# Breakout: 4

def getLetterGrade(grade):
  if grade >= 93.0:
    print("Your letter grade for CMPSC 131 is A.")
  elif grade >= 90.0:
    print("Your letter grade for CMPSC 131 is A-.")
  elif grade >= 87.0:
    print("Your letter grade for CMPSC 131 is B+.")
  elif grade >= 83.0:
    print("Your letter grade for CMPSC 131 is B.")
  elif grade >= 80.0:
    print("Your letter grade for CMPSC 131 is B-.")
  elif grade >= 77.0:
    print("Your letter grade for CMPSC 131 is C+.")
  elif grade >= 70.0:
    print("Your letter grade for CMPSC 131 is C.")
  elif grade >= 60.0:
    print("Your letter grade for CMPSC 131 is D.")
  else:
    print("Your letter grade for CMPSC 131 is F.")

def run():
  grade = input("Enter your CMPSC 131 grade: ")
  getLetterGrade(float(grade))

if __name__ ==  "__main__":
  run()

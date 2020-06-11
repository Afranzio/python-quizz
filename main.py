import requests
import json
from random import shuffle

va = requests.get('https://opentdb.com/api.php?amount=10&category=18&difficulty=medium')

valu = va.text

value = json.loads(valu)

values = value["results"]

score = 0

n = 0

#options =  values[n]["correct_answer"] + values[n]["incorrect_answer"]

while n<10:

  for each in values:

    option= values[n]["incorrect_answers"]

    crct = values[n]["correct_answer"] 

    lists = []

    lists.append(crct)

    for each in option:

      lists.append(each)

      shuffle(lists)

    print(values[n]["question"])

    #print("options : ", option)

    #print(values[n]["correct_answer"])

    print(lists)

    ans  = int(input("enter index of answer : "))

    if lists[ans - 1] == crct:
      score+=1
      print("your score is = " , score ,'\n')

    else:

      print("Noooo!!!" , '\n')

    n+=1

else:

  final_score = ""

  if score == 10:
    final_score = "Your Awesome!!"
  elif score >= 7:
    final_score = "Good"
  elif score >=4:
    final_score = "Better"
  else:
    final_score = "Do well"

  print("Your Quizz is over and your score is : " , score, "\n")
  print(final_score)
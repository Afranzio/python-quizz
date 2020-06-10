import requests
import json

va = requests.get('https://opentdb.com/api.php?amount=10&category=18&difficulty=easy')

valu = va.text

value = json.loads(valu)

values = value["results"]

score = 0

n = 0

#options =  values[n]["correct_answer"] + values[n]["incorrect_answer"]

while n<=10:

  for each in values:

    option= values[n]["incorrect_answers"]

    crct = values[n]["correct_answer"] 

    for each in option:

      lists = []

      lists.append(each)

      lists.append(crct)

    print(values[n]["question"])

    #print("options : ", option)

    #print(values[n]["correct_answer"])

    print(lists)

    ans  = int(input("enter index of answer : "))

    if lists[ans - 1] == crct:
      score+=1
      print("your score is = " , score)

    else:

      print("Noooo!!!")

    n+=1
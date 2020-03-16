import json
import requests
import pprint
import html
import random
ansnum=1
url="https://opentdb.com/api.php?amount=10&category=10&difficulty=easy&type=multiple"
end=""
score=0

while end != "quit":
    r=requests.get(url)
    if (r.status_code != 200):
        print("error in connection")
    else:
        
        data = json.loads(r.text)
        qus = data['results'][0]['question']
        ans = data['results'][0]['incorrect_answers']
        corr_ans = data['results'][0]['correct_answer']
        ans.append(corr_ans)
        random.shuffle(ans)

        print(html.unescape(qus) +"\n")
        
        for ansa in ans:
            print(str(ansnum) + "-" +html.unescape(ansa) + "\n")
            ansnum +=1
        usrans=input("Type the correct answer ")
        a=int(usrans)
        if ((a <= 0) and (a < 4)):
            print("enter a valide number  ")
            continue
        else:
            usrans=ans[int(usrans)-1]

            if usrans == corr_ans:
                print("you answerd correctly ")
                ansnum=1
                score +=1
                print('your score is '+ str(score))
            else:
                print("sorry answer is wrong ")
                ansnum=1
                print('your score is'+ str(score))
            end = input("\n press enter to play again enter 'quit' to exit. ")
print("thanks for playing") 

questions = [
    ["How many runs does a team get when the bowler bowls a wide ball?", "1run", "2run", "3run", "0run", 1],
    ["How many runs does a team get when the bowler bowls a NO ball?", "1run", "2run", "3run", "0run", 1],
    ["How many runs does a team get when the bowler bowls a FREE HIT ball?", "0run", "2run", "3run", "1run", 4],
    ["How many runs does a batsman get when he hits directly above the boundary?", "1run", "6run", "1run", "0run", 2],
    ["How many runs does a batsman get when he hits a boundary-touch shot?", "4run", "1run", "3run", "0run", 1]
]

levels = [1000, 2000, 3000, 4000, 5000]

for i in range(len(questions)):
    question = questions[i]
    print(question[0])
    print(f"1. {question[1]}    2. {question[2]}")
    print(f"3. {question[3]}    4. {question[4]}")
    
    choice = int(input("Enter your option (1-4): "))
    
    if choice == question[5]:
        print("Correct Answer!")
        print(f"You won {levels[i]} points!\n")
    else:
        print("Wrong Answer! Game Over.")
        break
if levels[i]!=5000:
    print("your total winnig is: 0")
else:
   print(f"your total winning amount is :{levels[i]}")

   
        
        
       

        
      
            
      

      




    
   
   
            

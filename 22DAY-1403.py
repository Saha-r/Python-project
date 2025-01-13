
correct_answers = ["yes", "no" , "no", "yes", "yes"]
your_answer = []
result =[]

print("answer the below question with yes or no")
Q1 = input("What is ..... ?").lower()
Q2 = input("What is ..... ?").lower()
Q3 = input("What is ..... ?").lower()
Q4 = input("What is ..... ?").lower()
Q5 = input("What is ..... ?").lower()

your_answer = Q1 + "," + Q2 + "," + Q3 + "," + Q4 + "," + Q5
print(your_answer)



def check_answer(your_answer):
    for element in your_answer:
        if your_answer == correct_answers:
            result = print("correct")
    
            # print("correct")
            
        elif your_answer!= correct_answers:
            result = print("incorrect")
        # element++ 
        
# check_answer()
check_answer(your_answer)
print(result)












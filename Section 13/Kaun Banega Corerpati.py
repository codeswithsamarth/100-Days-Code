question = [
    ["Which Indian Festival Celebrate the return of lord rama to Ayodhya?", "Holi", "Navaratri", "Diwali", "Makar Sankrati", 3],
    ["Who Wrote Mahabharata?", "Tulsidas", "Kalidas", "Valmiki", "Ved Vyasa", 4],
    ["Which River is Considered the Most sacred in Hinduism?", "Yamuna", "Ganga", "Saraswati", "Narmada", 2],
    ["Who Is the Current Prime Minister of India?", "Rahul Gandhi", "Arvind Kejriwal", "Narendra Modi", "Yogi Adityanath", 3],
    ["Subash Chandra Bose is Also Known by which Title?", "Sardar", "Netaji", "Maharaja", "Veer", 2],
    ["Which City is Also called the Pink City of India?", "Jodhpur", "Jaipur", "Mysore", "Pune", 2],
    ["Who Founded the Maratha Empire?", "Shivaji Maharaj", "Sambhaji Maharaj", "Aurangzeb", "Bajirao Peshwa", 1],
    ["Who Is Iron Man of India?", "Bhagat Singh", "Subash Chandra Bose", "Sardar Vallabhai Patel", "Jawaharlal Nehru", 3],
    ["Where The Famous Kedarnath Temple of Lord Shiva Located?", "Gujarat", "Tamil Nadu", "Uttarakhand", "Madhya Pradesh", 3]
]

prizes = [10000,20000,40000,80000,160000,320000,640000,1250000,2500000]
won = 0
for questions in question:
    print("\n" + questions[0])
    print(f"a. {questions[1]}")
    print(f"b. {questions[2]}")
    print(f"c. {questions[3]}")
    print(f"d. {questions[4]}")
    a = int(input("Enter your answer (1 for a, 2 for b, 3 for c, 4 for d): "))
    if questions[5] == a:
        print("✅ Correct Answer!")
        for i in prizes:
            won += prizes[0]
            print(f"You Won {won}rs")
            del prizes[0]
            break
    else:
        print("Better Luck Next Time!")
        break

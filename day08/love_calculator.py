def calculate_love_score(name1,name2):
    true = 0
    love = 0
    name = name1+name2
    for letter in name:
        if letter in "true":
            true+=1
        if letter in "love":
            love+=1
    print(f"{str(true)+str(love)}")

calculate_love_score(name1="prabhas",name2="anuskha")
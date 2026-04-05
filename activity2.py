amount=int(input("please enter amount to wihtdraw " ))

note_1= amount//100
note_2= (amount%100)//50
note_3= ((amount%100)%50)//10

print("the amount of notes you can have of 100's are", note_1)
print("the amount of notes you can have of 50's are", note_2)
print("the amount of notes you can have of 10's are", note_3)


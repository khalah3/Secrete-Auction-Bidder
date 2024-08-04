from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
print("Welcome to the secret auction program")

complete_dic={}
def parameters():
 name=input("what is your name?")
 bid=int(input("what is your bid?"))
 other_bidders=input("Are there any other bidders? Type 'yes' or 'no'\n")
 dic={name:bid}
 complete_dic.update(dic)
 num_of_bidders=1
 if other_bidders.lower()=="yes":
   clear()
   num_of_bidders+=1
   parameters()
 else:
   print(complete_dic)
   max_bid=max(complete_dic.values())

   def get_key(complete_dic,max_bid):
     for key,value in complete_dic.items():
       if value==max_bid:
         return key
   winner_name=get_key(complete_dic,max_bid)
   print(f"The winner is {winner_name} with a bid of ${max_bid}")

  
parameters() 








  


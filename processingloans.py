print("--------------SATHVIK FINANCE LIMITED----------")
#Created variables according to the criteria required to apply for loan 
income=int(input("Enter your income :")) #taking details for aproving the loan 
credit_score=int(input("Enter your credit score :"))
Amount=int(input("Enter required loan amount"))
#Making the conditions for conforming the loan 
if income>=100000 and credit_score>=750:
    print("you was eligible to laon ")
    print("------------Enter your account number---------------- :")
    number=int(input("Enter your account number :"))
    print(f"{Amount} was succesfully credited in your account : {number}")
#Made the statement if user not sutitable to our conditions 
else:
    print("You are not eligible to the Loan ! ")
    print("==Beacuse your creditscore and income is not sufficient to taken loan== ")
    
print("visit again ")
 
     
    

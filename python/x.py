'''
def arraySum():
    # Write your code here
    n=int(input("list of numbers:"))
    numbers = []
    for i in range(n):
        num=int(input("enter number {} ".format(i+1)))
        
        numbers.append(num) 
        print(num)
        
        
    
    total =sum(numbers)
    return total
result = arraySum()
print("sum of ", result)'''


with open("D:/xampp/htdocs/python/document.txt","rb") as file:
    txt =  file.read()
 

print(txt)
    

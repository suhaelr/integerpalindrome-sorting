#Determine Integer Palindrome 
#Using while loop method
number=int(input("Enter any number :"))
#simpan copy dari dari angka 
temp=number
#menghitung reverse
reverse_num=0
while(number>0):
    #mengekstrak digit terakhir
    digit=number%10
    #append digit dalam kondisi reversed
    reverse_num=reverse_num*10+digit
    #floor divide the number leave out the last digit from number
    number=number//10
#membandingkan digit reverse ke original number
if(temp==reverse_num):
    print("The number is palindrome!")
else:
    print("Not a palindrome!") 

#masukkan angka untuk menentukan apakah bilangan tersebut merupakan integer palindrome atau bukan

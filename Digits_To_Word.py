words_upto_19 = ['','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT',
                 'NINE','TEN','ELEVEN','TWELVE','THIRTEEN','FOURTEEN','FIFTEEN',
                 'SIXTEEN','SEVENTEEN','EIGHTEEN','NINETEEN']
words_upto_tens = ['','','TWENTY','THIRTY','FOURTY','FIFTY','SIXTY',
                  'SEVENTY','EIGHTY','NINETY']

n = int(input("Enter a digit from 0-99: "))
output=''
if n==0:
    output='ZERO'
elif n<=19:
    output=words_upto_19[n]
elif n<=99:
    output = words_upto_tens[n//10]+" "+words_upto_19[n%10]
else:
    print("Please enter value from 0-99 only...")
print(output)

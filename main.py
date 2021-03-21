g = dict()                                                                          
inp = open('sample_input.txt','r')                                                  

for line in inp:                                                             
    if line != '\n':                                                               
        arr = line.split(":")                                                         
        arr[1] = arr[1][1:]                                                             
        if arr[1] != "":                                                              
            if arr[1][-1] == "\n":                                                    
                arr[1] = arr[1][:-1]
            g[arr[0]] = int(arr[1])                                                                 
inp.close()                                                                  
m = int(input("Enter the number of employees :  "))                                                 
s = sorted(g.values())                                                            
l=len(s)                                                                          
min = s[-1] - s[0]                                                              
f=0                                                                                 
for i in range((l-m)+1):                                                         
    k = s[i+(m-1)] - s[i]                                                       
    if k<min:                                                                      
        min=k                                                                      
        f=i                                                                                 
out= open('sample_output.txt','w')                                                 
out.write("The goodies selected for distribution are:\n")                   
out.write("\n")
for i in range(f,f+m):                                                              
    for j in g.keys():                                                                                                                       
        if g[j] == s[i]:                                                          
            out.write(j+": ")                                               
            out.write(str(g[j]))                                           
            out.write("\n")
            break
out.write("\n")
out.write("And the difference between the chosen goodie with highest price and the lowest price is ")
out.write(str(min))
print("\ndifference is "+str(min))
out.close()

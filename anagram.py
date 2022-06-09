q1={}
q2={}
def anagrams(str1,str2):
        if len(str1)!=len(str2):
                return False
        else:
                num=0
                for x in str1:
                        q1[num]=x
                        num+=1
                num=0
                for x in str2:
                        q2[num]=x
                        num+=1
                x=sorted(q1.values())
                y=sorted(q2.values())
                if x==y:
                        return True
                else:
                        return False
string1=input("Enter the string")
string2=input("Enter the string to find wheather it is anagram")
print(anagrams(string1,string2))
                

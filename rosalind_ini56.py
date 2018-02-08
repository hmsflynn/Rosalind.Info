#rosalindpx.py

#Given: A file containing at most 1000 lines.

#Return: A file containing all the even-numbered lines from
#        the original file. Assume 1-based numbering of lines.

##

ab= open("rosalind_ini5.txt",'r')
i=0
for i in ab:
    a=ab.readlines()
d=0
e=[]
ab.close()
for d in range(len(a)):
    if d%2==0:
        e.append(a[d])
end = " ".join(e)

bb=open("rosalind_ini6.txt",'a')
bb.writelines(end)
bb.close()

#marks analysis report
s=int(input("enter the no.of students: "))
m=[]
for i in range(1,s+1):
    ma=int(input(f"enter the student {i} marks"))
    m.append(ma)
for i in m:
    print(i)
print("...........marks analysis report..........")
print("Total students",s)
print("Heighest marks",max(m))
print("Lowest marks",min(m))
print("Total marks",sum(m))
print("Average marks",sum(m)/s)



import numpy as np
data=np.array([[101,89,56,45],
               [102,56,89,56],
               [103,78,89,98],
               [104,56,67,44],
               [105,78,56,98],
               [106,76,56,45],
               [107,78,89,56],
               [108,67,56,65]])
print("Students data is\n",data)
total=np.sum(data[:,1:],axis=1)
print("Total marks =\n",total)
avg=np.mean(data[:,1:],axis=1)
print("Average =\n",avg)
print("1st mark=",max(total))
print("last mark=",min(total))
passed=data[total>=200]
pass_count=len(passed)
print(passed)
print("Passed students=",pass_count)
failed=data[total<200]
print(failed)
print("failed students=",len(failed))
pass_percentage=(pass_count/len(total)*100)
print("pass percentage=",pass_percentage)
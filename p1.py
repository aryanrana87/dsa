# Sort the given array.
# Calculate the sanity of an element in the array, which is defined as the sum of its original index (before sorting) 
# and the index of its last occurrence in the new array (after sorting).
a=[32,13,24,4]
b=sorted(a)
x=0
for i in range(len(a)):
    for j in range(len(a)-1,-1):
        if a[i]==b[j]:
            x+=(j+i)
            break
print(x)
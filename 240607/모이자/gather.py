n=5
arr = [1,2,3,2,6]
max_sum=0
for i in range(n):
    sum_of_distance = 0
    sum_of_min = 0
    for j in range(n): 
        sum_of_distance+=abs(arr[i]-arr[j])  
    
        sum_of_min=min(sum_of_min,sum_of_distance)
    

print(sum_of_distance)
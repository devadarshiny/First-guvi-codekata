def firstElement(arr, n, k): 
    count_map = {}; 
    for i in range(0, n): 
        if(arr[i] in count_map.keys()): 
            count_map[arr[i]] += 1
        else: 
            count_map[arr[i]] = 1
        i += 1
      
    for i in range(0, n):  
        if (count_map[arr[i]] == k): 
            return arr[i] 
        i += 1
              
    return -1
  
if __name__=="__main__": 
  
    arr = [1, 7, 4, 3, 4, 8, 7]; 
    n = len(arr) 
    k = 2
    print(firstElement(arr, n, k)) 

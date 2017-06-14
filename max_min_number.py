def find_max_min(num_list):
    for i in num_list:
        max_num = max(num_list) #finds the maximum number on the list
        min_num = min(num_list) #finds the minimum number on the list
        # assigns to variable max_min_num the list of the result of max_num and min_num
        max_min_num = [min_num, max_num] 
        if max_num == min_num:
            num_element = [num_list.count(i)]
            return num_element
        print(max_min_num)
  
'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):

    new_arr = []

    for index, item in enumerate(nums):

        if (index + k) > len(nums):
                continue

        comparison_arr = []

        for i in range(index, index + k):
            comparison_arr.append(nums[i])
        
        highest = comparison_arr[0]
        for i in comparison_arr:
            if i > highest:
                highest = i
        new_arr.append(highest)

    return new_arr




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

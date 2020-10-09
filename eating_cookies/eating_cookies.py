'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    n = n + 1
    if n < 2:
        return 1
    return eating_cookies(n-1) + eating_cookies(n-2)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

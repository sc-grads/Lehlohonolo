# 2. Create a tuple called nums_tuple from the nums_list using the tuple() constructor.
nums_tuple = tuple(nums_list)

# 3. Create a set called nums_set from the nums_list using the set() constructor. Print the set.
nums_set = set(nums_list)
print(nums_set)
# 4. Given the following list, create a new list called unique_ip that contains only unique values in the ip list.
# Print the unique_ip list.
ip = ['10.0.0.1', '10.0.0.2', '10.0.0.1', '10.0.0.3', '10.0.0.1', '10.0.0.2']
unique_ip = list(set(ip))
print(unique_ip)

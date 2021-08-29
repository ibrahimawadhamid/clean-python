def use_list_comprehension():
    numbers = [10, 23, 24, 76, 80, 91]
    filtered_data = [num for num in numbers if num % 2 == 0]
    print(filtered_data)

def use_zip_for_list_processing():
    users = ["Abe", "Larry", "John"]
    salaries = ["1M", "2M", "1M"]
    users_salary = []
    for user, salary in zip(users, salaries):
        users_salary.append((user, salary))
    users_salary = [item for item in zip(users, salaries)]
    return users_salary

use_list_comprehension()
print(use_zip_for_list_processing())
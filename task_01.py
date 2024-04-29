# the function takes a file location as an argument and returns a tuple
# with the total and average salaries
def total_salary(path):
    try:
        with open(path, 'r', encoding="UTF-8") as salaries:  # opens the file in the read-only mode
            total_sal = 0
            el_digit_count = 0
            for line in salaries:  # cleans the text file from spaces, new line symbols and commas
                line = line.strip().split(',')
                total_sal += float(line[-1])
                el_digit_count += 1
            average_sal = round((total_sal / el_digit_count), 2)  # counts the average salary
            return total_sal, average_sal
    except (FileNotFoundError, ZeroDivisionError) as error:
        print(error)


try:
    total, average = total_salary("salaries.txt")
    print(f"Total salary: {total}. Average salary: {average}")
except (ValueError, TypeError) as err:
    print(err)
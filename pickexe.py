import csv
 
def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
 
    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)
 
    return "Users updated: {}.".format(count)

update_users("Grace","Hopper", "Hello", "World")

with open("users.csv", "w", newline="") as file: #USE THIS to not get spaces

## delete
import csv
 
def delete_users(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
 
    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == first_name and row[1] == last_name:
                count += 1
            else:
                csv_writer.writerow(row) # THE ELSE RE-WRITES the whole thing not including first name and last name
 
    return "Users deleted: {}.".format(count)

# def update_users(o_first, o_last, n_first, n_last):


# def add_user(first_name, last_name):
#     with open("users.csv", "a") as file:
#     	csv_writer = writer(file)
#     	csv_writer.writerow([first_name, last_name])

# new = [x for x in data if "Colt" and "Steele" in x]	
# 	new = [x for x in data if "Joe" and "Six" in x]



import os

path = r"C:\Users\kapil\OneDrive\Desktop\class\employee_details"

os.chdir(path)

print(os.getcwd())
print(os.listdir())

emp_list = ["aman", "shivam", "shubham", "anshu", "kamal"]

for emp in emp_list:
    file_path = os.path.join(path, f"{emp}.txt")

    with open(file_path, "w") as file:
        file.write(f"Employee Name: {emp}")

    print(f"{emp}.txt created")
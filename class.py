class Employee:
    no_of_employees = 0  # data member

    def __init__(self, name, family_name, salary,
                 department):  # constructor to initialize name, family_name,salary,department
        self.name = name
        self.family_name = family_name
        self.salary = salary
        self.department = department
        Employee.no_of_employees += 1

    @staticmethod
    def average_salary(employees):  # function to calculate average salary

        sum = 0
        for employee in employees:
            sum += employee.salary
        return sum / Employee.no_of_employees


class FulltimeEmployee(Employee):  # FulltimeEmployee class inheriting the Employee class

    def __init__(self, name, family_name, salary, department):
        super().__init__(name, family_name, salary, department)

    def full_time_benefits(self):
        print("Few benefits as full time employee.")


def main():
    employees = []
    f1 = FulltimeEmployee("sneha", "kusuma", 50000, "software")
    f1.full_time_benefits()
    employees.append(f1)
    f2 = FulltimeEmployee("mahi", "pulagam", 180000, "civil engineering")
    employees.append(f2)
    e1 = Employee("ramya", "vengal", 160000, "automobile")
    employees.append(e1)
    e2 = Employee("deepika", "thota", 135000, "engineering")
    employees.append(e2)
    print("Average salary : ", FulltimeEmployee.average_salary(employees))


if __name__ == "__main__":
    main()
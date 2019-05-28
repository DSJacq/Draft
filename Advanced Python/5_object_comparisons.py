# OBJECT COMPARISON

# use special methods to compare cobject to each other


class Employee():
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsService

    # implement comparison function by emp level
    def __ge__(self, other):
        if (self.level == other.level):
            return self.level >= other.level
        return self.level >= other.level

        
    def __gt__(self, other):
        if (self.level == other.level):
            return self.level > other.level
        return self.level > other.level

    def __lt__(self, other):
        if (self.level == other.level):
            return self.level < other.level
        return self.level < other.level
    
    def __le__(self, other):
        if (self.level == other.level):
            return self.level <= other.level
        return self.level <= other.level

    def __eq__(self, other):
        pass


def main():
    # define some employees
    dept = []
    dept.append(Employee("Tim", "Sims", 5, 9))
    dept.append(Employee("John", "Doe", 4, 12))
    dept.append(Employee("Jane", "Smith", 6, 6))
    dept.append(Employee("Rebecca", "Robinson", 5, 13))
    dept.append(Employee("Tyler", "Durden", 5, 12))
    
    # who is more senior?
    print(dept[0] > dept[2])
    print(dept[4] < dept[3])

    # sort the items
    emps = sorted(dept)
    for emp in emps:
        print(emp.lname)


if __name__ == "__main__":
    main()
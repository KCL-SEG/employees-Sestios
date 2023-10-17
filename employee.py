"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    # type_of_contract can be "monthly salary" or "contract"
    # commission_type can be "Fixed", "Contract-Based" or "None"
    def __init__(self, name, type_of_contract, monthly_salary, hours_worked, hourly_wage, commission_type, contracts_finished, bonus_per_contract_finished, fixed_bonus):
        self.name = name
        self.type_of_contract = type_of_contract
        self.monthly_salary = monthly_salary
        self.hours_worked = hours_worked
        self.hourly_wage = hourly_wage
        self.commission_type = commission_type
        self.contracts_finished = contracts_finished
        self.bonus_per_contract_finished = bonus_per_contract_finished
        self.fixed_bonus = fixed_bonus

    def get_pay(self):
        total_salary = 0
        if self.type_of_contract == "monthly salary":
            total_salary += self.monthly_salary
        else:
            total_salary += self.hours_worked*self.hourly_wage
        # Next is the bonus calculation
        if self.commission_type == "Fixed":
            total_salary += self.fixed_bonus
        elif self.commission_type == "Contract-Based":
            total_salary += self.contracts_finished*self.bonus_per_contract_finished
        return total_salary

    def __str__(self):
        result_string = f"{self.name} works on a "
        if self.type_of_contract == "monthly salary":
            result_string += f"monthly salary of {self.monthly_salary}"
        else:
            result_string += f"contract of {self.hours_worked} hours at {self.hourly_wage}/hour"
        # Next is the bonus calculation string
        if self.commission_type == "Fixed":
            result_string += f" and receives a bonus commission of {self.fixed_bonus}"
        elif self.commission_type == "Contract-Based":
            result_string += f" and receives a commission for {self.contracts_finished} contract(s) at {self.bonus_per_contract_finished}/contract"
        # Finishing touches
        result_string += f". Their total pay is {self.get_pay()}."
        return result_string

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "monthly salary", 4000, 0, 0, "None",0,0,0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',"contract", 0, 100, 25, 0,0,0,0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',"monthly salary",3000,0,0,"Contract-Based",4,200,0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',"contract",0,150,25,"Contract-Based",3,220,0)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',"monthly salary",2000,0,0,"Fixed",0,0,1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',"contract",0,120,30,"Fixed",0,0,600)

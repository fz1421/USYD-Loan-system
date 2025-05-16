class Person:
    def __init__(self,name, age, salary, company_rate, credit_history_score):
        self.name=name
        self.salary=salary
        self.company_rate=company_rate
        self.credit_history_score=credit_history_score
        self.age=age
    
    
    def calculate_base_credit_score(self):
        
        weight_salary=0.0
        if self.salary>=100000 and self.salary<=999999:
            weight_salary=self.salary/10**6
        elif self.salary>999999:
            weight_salary=30
        else:
            weight_salary=0
            
        total_score=weight_salary*0.3+self.company_rate*0.2+self.credit_history_score*0.4+self.age*0.1
        return total_score
        
    
    def is_eligible(self,min_age, min_credit_score):
        if self.age<min_age or self.credit_history_score<min_credit_score:
            return False
        return True
            
    
    
    def update_salary(self,new_salary):
        self.salary=new_salary
        return self.salary
    
    def update_company_rate(self,new_rate):
        self.company_rate=new_rate
        return self.company_rate
    
    def __str__(self):
        return f'Your status:age:{self.age}, salary: {self.salary},company_rate: {self.company_rate}, credit_history_score: {self.credit_history_score}'
        

    
        

    
if __name__ == "__main__":
    
    
    
    pass
    
    
    
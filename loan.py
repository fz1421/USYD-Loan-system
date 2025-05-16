from person import Person


class Loan:
    def __init__(self,applicant,requested_amount,term_months):
        self.applicant=applicant
        self.requested_amount=requested_amount
        self.approved_amount=0
        self.interest_rate=0.05
        self.term_months=term_months
        self.monthly_payment=0.0
        self.status='approved'
        self.rejection_reason = ""
    
    
    
    
    def determine_interest_rate(self):
        score=self.applicant.calculate_base_credit_score()
        if score>=13.5:
            return self.interest_rate-0.02
        elif score>10 and score<13.5:
            return self.interest_rate
        else:
            return self.interest_rate+0.02
            
    
    
    def calculate_max_loan_amount(self):
        score=self.applicant.calculate_base_credit_score()
        if score>=13.5:
            max_loan=self.applicant.salary*0.3
        else:
            max_loan=self.applicant.salary*0.2
        return max_loan
    
    
    
    
    def evaluate(self,requested_amount,term_months):
        if self.applicant.is_eligible(18,10):
            if requested_amount<=self.calculate_max_loan_amount() and term_months<=12:
                self.status='approved'
                self.approved_amount=requested_amount
                self.term_months=term_months
                self.interest_rate=self.determine_interest_rate()
                
            else:
                self.status='denied'
                self.approved_amount=0
                if requested_amount > self.calculate_max_loan_amount():
                    self.rejection_reason = f"Requested amount (${requested_amount}) exceeds maximum eligible amount (${self.calculate_max_loan_amount():.2f})"
        else:
            self.status='denied'
            self.rejection_reason = "Basic eligibility criteria not met"
            
    
                
        
    def calculate_monthly_payment(self):
        if self.status=='approved':
            monthly_payment=(self.approved_amount*self.interest_rate*(1+self.interest_rate)**self.term_months)/((1+self.interest_rate)**self.term_months-1)
            return monthly_payment
        else:
            return 0
        
    def calculate_total_payment(self):
        if self.status=='approved':
            total_payment=self.calculate_monthly_payment()*self.term_months
            return total_payment
        else:
            return 0
        pass
    
    
    
    
    def display_terms(self):
        pass

def main():
    print('Welcome to our Professional Loan Application System!')
    while True:
        command = input('Please enter "start" to begin or "quit" to exit: ')
        if command == 'quit':
            break
        elif command == 'start':
            name = input('Please enter your full name: ')
            print(f'Welcome, {name}!\n')
            
            while True:
                try:
                    age = int(input('Please enter your age: '))
                    if age <= 18:
                        print('We apologize, but you are not eligible for a loan at this time. Reason: Age requirement not met.')
                        break
                    elif age > 60:
                        print("We regret to inform you that according to our company policy, we cannot process your loan application. Reason: Age restriction.")
                        break
                    else:
                        while True:
                            try:
                                salary = int(input('Please enter your ANNUAL salary (1000-1000000): '))
                                if salary >= 1000000:
                                    print('We appreciate your interest, but our services are designed for different financial needs.')
                                    return
                                elif salary <= 1000:
                                    print('We regret to inform you that your current income level does not meet our minimum requirements.')
                                    return
                                break
                            except ValueError:
                                print('Invalid input! Please enter a valid number for salary.')
                        break
                except ValueError:
                    print('Invalid input! Please enter a valid number for age.')
                    continue
            while True:
                try:
                
                    company_rate = int(input('Please rate your company\'s stability (1-10): '))
                    while company_rate <=0 or company_rate > 10:
                        print('Invalid input! Please enter a number between 1 and 10.')
                        company_rate = int(input('Please rate your company\'s stability (1-10): '))
                except:
                    print('Invalid input! Please enter a valid number for company rate or credit history score.')
                    continue
                break
                
            while True:
                try:
                        
                    credit_history_score = int(input('Please enter your credit history score (1-10): '))
                    while credit_history_score <= 0 or credit_history_score > 10:
                        print('Invalid input! Please enter a number between 1 and 10.')
                        credit_history_score = int(input('Please enter your credit history score (1-10): '))
                        
                    person = Person(name, age, salary, company_rate, credit_history_score)
                    print('Your information has been successfully recorded.\n')                
                    
                    print("Let's proceed with your loan application details.\n") 
                except:
                    print('Invalid input! Please enter a valid number for company rate or credit history score.')
                    continue
                break
                    
    
            
            while True:
                try:
                    amount = int(input('Please enter your requested loan amount: '))
                    if amount <= 0:
                        print('Invalid input! Loan amount must be greater than 0.')
                        continue
                    month = int(input('Please specify the loan term in months: (1-12): '))
                    if month <= 0 or month > 12:
                        print('Invalid input! Loan term must be greater than 0 and less than 12.')
                        continue
                    break
                except ValueError:
                    print('Invalid input! Please enter valid numbers for loan amount and term.')
                    continue
                
            loan = Loan(applicant=person, requested_amount=amount, term_months=month)
            loan.evaluate(amount, month)
            if loan.status == 'approved':
                pay_by_month = loan.calculate_monthly_payment()
                total_pay = loan.calculate_total_payment()
                print(f'Congratulations! Your loan has been approved.')
                print(f'Monthly payment: ${pay_by_month:.2f}')
                print(f'Total payment: ${total_pay:.2f}')
                break
            else:
                print("We regret to inform you that your loan application has been declined.")
                print(f"Reason: {loan.rejection_reason}")
                print("Thank you for considering our services. We wish you the best in your financial journey.")
                print(person)
                break
        else:
            print('Invalid command. Please enter "start" to begin or "quit" to exit.')
            continue
                                                                    
    

if __name__ == "__main__":
    
    main()
    
    
# Loan Application System

A simple loan application system written in Python that evaluates loan applications based on various criteria.

## Project Files
- `loan.py`: Main program file (Run this file to start the application)
- `person.py`: Person class implementation

## Project Specifications
This project uses only Python's built-in libraries. No external dependencies are required.

### Libraries Used
- Standard Python libraries only
- No external libraries required
- No graphics libraries used
- No GUI implementation
- No audio/video processing
- No web-based or networking features

## Features

- Age verification (18-60 years)
- Salary validation (1000-1000000)
- Company stability rating (1-10)
- Credit history score (1-10)
- Loan amount and term evaluation
- Interest rate calculation based on credit score
- Monthly payment calculation

## Requirements

- Python 3.x
- No additional installations required

## How to Run

1. Ensure you have Python 3.x installed
2. Download both `loan.py` and `person.py` files
3. Run the program:
```bash
python loan.py
```

## Program Flow

1. Enter personal details:
   - Name
   - Age (must be between 18-60)
   - Annual salary (must be between 1000-1000000)

2. Enter evaluation criteria:
   - Company stability rating (1-10)
   - Credit history score (1-10)

3. Enter loan details:
   - Requested loan amount
   - Loan term in months (1-12)

4. The system will evaluate your application and provide:
   - Approval status
   - Approved amount (if approved)
   - Monthly payment amount (if approved)
   - Total payment amount (if approved)

## Note for Tutors
- The program uses only Python's standard libraries
- No special environment setup is required
- The program can be run directly in Ed's environment
- All input validation is handled within the program
- No external dependencies or special configurations needed 
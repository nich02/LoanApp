## LoanApp

In banking sector, credit risk is a critical business issue which makes sure that bank has sufficient capital to protect depositors from credit, market and operational risks. During the process, its role is to work for bank in compliance to central bank regulations.

There're different ways to assess the credit risk of customers in banking industry. 

1. Probability of Default (PD) tells us the likelihood that a borrower will default on the debt (loan or credit card). In simple words, it returns the expected probability of customers fail to repay the loan.
2. Loss Given Default (LGD) is a proportion of the total exposure when borrower defaults. It is calculated by (1 - Recovery Rate). For example someone takes $200,000 loan from bank for purchase of flat. He/She paid some installments before he stopped paying installments further. When he defaults, loan has an outstanding balance of $100,000. Bank took possession of flat and was able to sell it for $90,000. Net loss to the bank is $10,000 which is 100,000-90,000, and the LGD is 10% i.e. $10,000/$100,000.
3. Exposure at Default (EAD) is the amount that the borrower has to pay the bank at the time of default. In the above example shown in LGD, outstanding balance of $100,000 is EAD

For this project, the data scientist used the first technique (PD) on data provided then developed an end point, or deployed the model to a web application using a python streamlit library. This project includes members loan dataset collected to predict the credit worthness of the members. 

The hosted application is found in this link https://tranquil-bayou-89446.herokuapp.com/

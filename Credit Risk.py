

#1 What is the distribution of High Risk vs Low Risk customers?
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"credit_risk_dataset (1).csv")

print(df['risk_category'].value_counts())





#2 What is the average credit score for each risk category?
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"credit_risk_dataset (1).csv")

print(df.groupby('risk_category')['credit_score'].mean())




#3 Which employment status has the highest credit risk?
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"credit_risk_dataset (1).csv")

print(pd.crosstab(df['employment_status'],df['risk_category']))





#4 Does annual income affect credit risk?
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"credit_risk_dataset (1).csv")

print(df.groupby('risk_category')['annual_income'].mean())





#5 Compare average outstanding debt by risk category.
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"credit_risk_dataset (1).csv")

print(df.groupby('risk_category')['total_outstanding_debt'].mean())





#6 What is the average loan application amount by risk category?
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"credit_risk_dataset (1).csv")

print(df.groupby('risk_category')['loan_application_amount'].mean())





#7 Does late payment count influence credit risk?
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"credit_risk_dataset (1).csv")

print(df.groupby('risk_category')['late_payment_count'].mean())





#8 Relationship between loan default history and risk.
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"credit_risk_dataset (1).csv")

print(pd.crosstab(df['loan_default_history'],df['risk_category']))




#9 Which gender has the highest proportion of risky customers?
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"credit_risk_dataset (1).csv")

print(pd.crosstab(df['gender'],df['risk_category']))





#10 Compare average monthly balance across risk categories.
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"credit_risk_dataset (1).csv")

print(df.groupby('risk_category')['avg_monthly_balance'].mean())





#11 Compare debit card spending between risk groups.
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"credit_risk_dataset (1).csv")

print(df.groupby('risk_category')['debit_card_spending'].mean())






#12 Which customers use mobile banking the most?
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"credit_risk_dataset (1).csv")

print(df.groupby('risk_category')['mobile_banking_logins'].mean())





#13 Compare ATM withdrawal frequency.
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"credit_risk_dataset (1).csv")

print(df.groupby('risk_category')['atm_withdrawal_frequency'].mean())




#14 Compare online transfer frequency.
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"credit_risk_dataset (1).csv")

print(df.groupby('risk_category')['online_transfer_frequency'].mean())




#15 Which employment status has the highest annual income?
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"credit_risk_dataset (1).csv")

print(df.groupby('employment_status')['annual_income'].mean())





#16 What is the average number of open loans by risk category?
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"credit_risk_dataset (1).csv")

print(df.groupby('risk_category')['num_open_loans'].mean())





#17 Fraud flag analysis.
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"credit_risk_dataset (1).csv")

print(pd.crosstab(df['fraud_flag'],df['risk_category']))




#18 Top 10 customers with the highest outstanding debt.
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"credit_risk_dataset (1).csv")

print(df[['total_outstanding_debt']].sort_values('total_outstanding_debt', ascending=False).head(10))









































































































































#1
SELECT scheme_name,fund_house,aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

#2
SELECT scheme_name,sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

#3
SELECT amfi_code,ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC;

#4
SELECT state,COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

#5
SELECT transaction_type,COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY transaction_type;

#6
SELECT scheme_name,expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

#7
SELECT age_group,ROUND(AVG(amount_inr),2) AS avg_investment
FROM fact_transactions
GROUP BY age_group
ORDER BY avg_investment DESC;

#8
SELECT kyc_status,COUNT(*) AS investors
FROM fact_transactions
GROUP BY kyc_status;

#9
SELECT scheme_name,return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;

#10
SELECT scheme_name,alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 5;
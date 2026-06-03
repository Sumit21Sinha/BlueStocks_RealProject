# Data Dictionary

## dim_fund

| Column | Description |
|----------|----------|
| amfi_code | Unique AMFI fund code |
| scheme_name | Mutual fund name |
| fund_house | Asset Management Company |
| category | Fund category |

## fact_nav

| Column | Description |
|----------|----------|
| amfi_code | Fund identifier |
| date | NAV date |
| nav | Daily NAV value |

## fact_transactions

| Column | Description |
|----------|----------|
| investor_id | Investor identifier |
| transaction_type | SIP/Lumpsum/Redemption |
| amount_inr | Transaction amount |

## fact_performance

| Column | Description |
|----------|----------|
| sharpe_ratio | Risk-adjusted return |
| alpha | Excess return |
| beta | Market sensitivity |
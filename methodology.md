
# Wallet Risk Scoring Methodology

## Data Collection Method
Transaction data was retrieved using The Graph protocol for AAVE V2, querying borrow, repay, liquidation, and collateral transactions.

## Feature Selection Rationale
- Total borrowed amount: Indicates risk exposure.
- Repayment ratio: A measure of responsibility.
- Liquidation events: Direct risk indicator.
- Collateral-to-loan ratio: Measures asset backing.

## Scoring Method
A weighted scoring system (0–1000) was used:
- Repayment history (40%)
- Liquidation count (30%)
- Collateral ratio (20%)
- Borrow volume (10%)

## Justification of Risk Indicators
These indicators collectively measure the creditworthiness and behavior of the wallet on AAVE protocol.

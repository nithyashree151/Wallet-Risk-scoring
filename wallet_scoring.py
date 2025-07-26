
import pandas as pd

# Load wallet data
wallets = pd.read_csv('wallet_scores.csv')

# Simple mock scoring logic (just for demonstration)
wallets['score'] = 1000 - wallets.index * 10

# Save updated scores
wallets.to_csv('wallet_scores.csv', index=False)

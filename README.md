## ⚙️ How It Works

### Step 1: Data Loading
The script reads a CSV (`wallet_scores.csv`) that contains wallet addresses.

### Step 2: Scoring (Mock Logic)
A basic scoring formula is applied:
```python
score = 1000 - (index * 10)

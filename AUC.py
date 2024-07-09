import pandas as pd
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

# Read data from final_ranking.txt
data = []
with open('final_ranking.txt', 'r') as file:
    for line in file:
        parts = line.strip().split(' -> ')
        compound = parts[0]
        score_str = parts[1].split(' ')[0]  # Extract the numeric part of the score
        score = float(score_str)
        # Determine if it's a ligand or decoy based on the name
        label = 1 if compound.startswith('ligand') else 0
        data.append({'compound': compound, 'score': score, 'label': label})

# Create DataFrame
df = pd.DataFrame(data)

# Calculate ROC Curve
fpr, tpr, thresholds = roc_curve(df['label'], df['score'], pos_label=1)
roc_auc = auc(fpr, tpr)

# Plot ROC Curve
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()

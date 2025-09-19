import pandas as pd
#opens file
df = pd.read_csv('student_exam_scores.csv')

#df['Car'] = df['Manufacturer'] + " " + df['Model'] + " " + df['Price'].astype(str)
#averagecars = df['Car'].value_counts().head(3)



#find best
best = df.sort_values(by='exam_score',ascending=False).head(5)
#find worst
worst = df.sort_values(by='exam_score',ascending=True).head(5)
#find average
average = df['exam_score'].mean()

print("Best scores are:")
print(best)

print(f"\nAverage score is: {average:.2f}")

print("\nWorst scores are:")
print(worst)
import pandas as pd
df = pd.read_csv(r'seo.csv')
df.drop(columns=['Device Category'], inplace=True)

#ZONE 1
filtered_df1 = df[(df['CTR'] > 0.1921) & (df['Average Position'] < 5.82)]
sorted_filtered_df1 = filtered_df1.sort_values(by='Clicks', ascending=False)
sorted_filtered_df1

#ZONE 4
filtered_df4 = df[(df['CTR'] < 0.1921) & (df['Average Position'] < 5.82)]
sorted_filtered_df4 = filtered_df4.sort_values(by='Clicks', ascending=False)
sorted_filtered_df4

#ZONE 2
filtered_df2 = df[(df['CTR'] > 0.1921) & (df['Average Position'] > 5.82)]
sorted_filtered_df2 = filtered_df2.sort_values(by='Clicks', ascending=False)
sorted_filtered_df2

#ZONE 3
filtered_df3 = df[(df['CTR'] < 0.1921) & (df['Average Position'] > 5.82)] 
sorted_filtered_df3 = filtered_df3.sort_values(by='Clicks', ascending=False) 
sorted_filtered_df3

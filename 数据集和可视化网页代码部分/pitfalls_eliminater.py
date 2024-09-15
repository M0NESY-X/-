import pandas as pd
points = pd.read_csv('sparse_points.csv')
i = 0
j = 1
a = points.index.values.max()
while i<a and j<=a: 
    dist=(points.at[i,'lat']-points.at[j,'lat'])*(10000)+(points.at[i,'lng']-points.at[j,'lng'])*(10000)
    if dist > 15:
        print (points.loc[i])
        print (points.loc[j])
        points.drop(index = i,inplace = True)
        points.drop(index = j,inplace = True)
        i = i + 2
        j = j + 2
    else:
        i = i + 1
        j = j + 1
points.to_csv('sparse_points_modified.csv',sep=',',index=False)
import pandas as pd
import numpy as np

mnames=['movies_id','title','genres']
read=pd.read_table('F:/DATA SCIENCE BOOKS/pydata-book-2nd-edition/datasets/movielens/movies.dat',sep='::',header=None, names=mnames)
print(read[:10])

all_genres=[]
for x in read.genres:
    all_genres.extend(x.split('|'))

genres=pd.unique(all_genres)
print(genres)

zero_matrix=np.zeros((len(read),len(genres)))
print(zero_matrix)

dummies=pd.DataFrame(zero_matrix,columns=genres)
print(dummies)
print(read.genres[0])
print(read.genres[0].split('|'))
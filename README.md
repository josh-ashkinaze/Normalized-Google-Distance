# Normalized Google Distance


## About 
The Normalized Google Distance (NGD) is a semantic similarity measure, 
calculated based on the number of hits returned by Google for a set of 
keywords. If keywords have many pages in common relative to their respective, 
independent frequencies, then these keywords are thought to be semantically 
similar. 

If two search terms w1 and w2 never occur together on the same web 
page, but do occur separately, the NGD between them is infinite. 

Conversely, if both terms always occur together, their NGD is zero.

## Methods <a name = "data"></a>

### Simple NGD

To compute the NGD between two word: 

``` Python
ngd = calculate_NGD(w1, w2)
```


### Pairwise NGD

#### As a dictionary
To compute pairwise NGDs (ex: computing the NGD for a matrix of political candinates)

``` Python
distances = pairwise_NGD(w1, w2)
```
This will return a nested dictionary, where ```distances[i][j] = NGD(i, j)```

#### As a dataframe
To return the matrix as a dataframe: 
``` Python
distances = pairwise_NGD(w1, w2)
matrix_df = pairwise_NGD_to_df(distances)
```

This will return a dataframe object where ```matrix_df[i][j] = NGD(i, j)```


## Warnings <a name = "data"></a>

* Using this script may be in violation of Google's TOS. Please use this script for research purposes only. 
** And on a related note, queries are somewhat slow because I put in calls to ```sleep()``` to space out requests. You can change these, but I do not reccomend doing so. 

* When dealing with Pairwise NGDs, the number of queries blows up very quickly. For a set of size ```n``` there are ```[(n-1)(n)]/2```distinct comparisons. 

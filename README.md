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
calculate_NGD(w1, w2)
```


### Pairwise NGD

To compute pairwise NGDs (ex: computing the NGD for a matrix of political candinates)

``` Python
pairwise_NGD(w1, w2)
```

To return the matrix as a dataframe: 
``` Python
matrix = pairwise_NGD(w1, w2)
matrix_df = pairwise_NGD_to_df(matrix)
```



# Normalized Google Distance
Read Formal Writeup of the original paper: https://arxiv.org/pdf/cs/0412098.pdf

# About
The Normalized Google Distance (NGD) is a semantic similarity measure, calculated based on the number of hits returned by Google for a set of keywords. If keywords have many pages in common relative to their respective, independent frequencies, then these keywords are thought to be semantically similar.

If two search terms `w1` and `w2` never occur together on the same web page, but do occur separately, the NGD between them is infinite.

Conversely, if both terms always occur together, and only occur together, their NGD is zero.

This script provides some useful functions for working with NGD. 

# Methods
## Simple NGD
To compute the NGD between two words:

``` Python
ngd = calculate_NGD("w1", "w2")
```

## Pairwise NGD
### As a dictionary

To compute pairwise NGDs (ex: computing the NGD for a matrix of political candidates)
``` Python
L = ["w1", "w2", "w3"]
distances = pairwise_NGD(L)
```
This will return a nested dictionary, where ```distances[i][j] = NGD(L_i, L_j)```

### As a dataframe
To return the above matrix as a dataframe:
``` Python
distances = pairwise_NGD(L)
matrix_df = pairwise_NGD_to_df(distances)
```

# Warnings
* Using this script may be in violation of Google's TOS. Please use this script for research purposes only.
* And on a related note, queries are somewhat slow because I put in calls to sleep() to space out requests. You can change these, but I do not recommend doing so. You'll get flagged quickly.
* When dealing with pairwise NGDs, the number of queries blows up fast. For a set of size ```n``` there are ```[(n-1)(n)]/2``` distinct comparisons.

# Case Study
Here's a [case study I did](https://www.joshash.space/data-science/clusters-of-democratic-candidates-1
), looking at how the media talks about political candidates. 

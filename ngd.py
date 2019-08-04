import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import math, sys, time, random, collections
import numpy as np
import pandas as pd

""" 
A python script to calculate Normalized Google Distance 

The Normalized Google Distance (NGD) is a semantic similarity measure, 
calculated based on the number of hits returned by Google for a set of 
keywords. If keywords have many pages in common relative to their respective, 
independent frequencies, then these keywords are thought to be semantically 
similar. 

If two search terms w1 and w2 never occur together on the same web 
page, but do occur separately, the NGD between them is infinite. 

If both terms always occur together, their NGD is zero.
"""

def NGD(w1, w2):
  """
  Returns the Normalized Google Distance between two queries.

  Params:
   w1 (str): word 1
   w2 (str): word 2
  Returns:
   NGD (float)
  """
  N = 25270000000.0 # Number of results for "the", proxy for total pages
  N = math.log(N,2) 
  if w1 != w2:
    f_w1 = math.log(number_of_results(w1),2)
    f_w2 = math.log(number_of_results(w2),2)
    f_w1_w2 = math.log(number_of_results(w1+" "+w2),2)
    NGD = (max(f_w1,f_w2) - f_w1_w2) / (N - min(f_w1,f_w2))
    return NGD
  else: 
    return 0
 
def calculate_NGD(w1, w2, n_retries=10):
  """ 
  Attempt to calculate NGD. 

  We will attempt to calculate NGD, trying `n_retries`. (Sometimes Google throws
  captcha pages. But we will just wait and try again). Iff all attempts fail, 
  then we'll return NaN for this pairwise comparison. 

  Params: 
    w1 (str): word 1 
    w2 (str): word 2
    retries (int): Number of attempts to retry before returning NaN 
  Returns:
    if succesful:
      returns NGD
    if not succesful:
      returns np.NaN
  """

  for attempt in range(n_retries):
    try:
      return NGD(w1, w2)
    except Exception as e:
      print("Trying again...")
      print(e)
  else: 
    print("Sorry. We tried and failed. Returning NaN.")
    return np.NaN

def pairwise_NGD(element_list, retries=10):
  """Compute pairwise NGD for a list of terms"""
  distance_matrix = collections.defaultdict(dict) # init a nested dict
  for i in element_list:
    sleep(5, 10)
    for j in element_list:
      try: # See if we already calculated NGD(j, i)
        print(i, j)
        distance_matrix[i][j] = distance_matrix[j][i]
      except KeyError: # If not, calculate NGD(i, j)
        distance_matrix[i][j] = calculate_NGD(i, j, retries)
  return distance_matrix

def pairwise_NGD_to_df(distances):
  """Returns a dataframe of pairwise NGD calculations"""
  df_data = {} 
  for i in distances:
    df_data[i] = [distances[i][j] for j in distances]
  df = pd.DataFrame(df_data)
  df.index = distances
  return df 

def number_of_results(text):
  """Returns the number of Google results for a given query."""
  headers = {'User-Agent': UserAgent().firefox}
  sleep(5, 10)
  r = requests.get("https://www.google.com/search?q={}".format(text.replace(" ","+")), headers=headers)
  soup = BeautifulSoup(r.text, "lxml") # Get text response
  res = soup.find('div', {'id': 'resultStats'}) # Find result string 
  return int(res.text.replace(",", "").split()[1]) # Return result int

def sleep(alpha, beta):
  """Sleep for an amount of time in range(alpha, beta)"""
  rand = random.Random()
  time.sleep(rand.uniform(alpha, beta))

if __name__ == "__main__":
  print("This is a script for calculating NGD.")

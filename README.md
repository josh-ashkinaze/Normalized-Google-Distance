# Normalized Google Distance


## About 
The Normalized Google Distance (NGD) is a semantic similarity measure, 
calculated based on the number of hits returned by Google for a set of 
keywords. If keywords have many pages in common relative to their respective, 
independent frequencies, then these keywords are thought to be semantically 
similar. 

If two search terms w1 and w2 never occur together on the same web 
page, but do occur separately, the NGD between them is infinite. 

If both terms always occur together, their NGD is zero.Just as a 'color palette' describes the colors of some visual object, an 'emotion palette' describes the emotions felt from a visual object. An EmotaPal combines both pieces (visual and psychological) of information. 

## Core Data <a name = "data"></a>
Functionally, this library provides methods to associate emotions with colors through an EmotaPal object. That object relies on a KNN model which predicts emotions from colors. The model was trained on a dataset constructed by parsing the dominant color of 100 Google Image results for 264 emotions. 

[For more information on the data, please read here.](https://github.com/josh-ashkinaze/Emotion-Colors/blob/master/README.md)

## Use Cases <a name = "usecases"></a>

Maybe you are an artist and are deciding between what color palettes to use. This, in turn, could depend on the psychological associations a color palette provokes. EmotaPal's `from_colors()` constructor will return the emotions associated with colors in your color palettes. 

Maybe you started a brewery and are interested in how regional companies are positioning themselves. EmotaPal's `from_gimg()` constructor will allow you to construct an EmotaPal from google images, so you can "scrape" the probable affective responses to your competitor's logos. 

## Usage <a name = "usage"></a>
There are 4 ways to construct an EmotaPal. 

### Constructing an EmotaPal

``` Python
from emotapal import EmotaPal

e1 = EmotaPal().from_colors(color_list)
e2 = EmotaPal().from_image(some_image, ncolors)
e3 = EmotaPal().from_url(image_url, ncolors)
e4 = EmotaPal().from_gimg(query, nimages)
```


#### Constructing an EmotaPal from a list of colors. 
``` Python
"""
Params:
  clrs (list): A list of colors, each element either an RGB tupple or hex string 
  topn (int, optional):  Keep only the topn best (input color, emotion color) matches. 
  unique_words (bool, optional): Keep only the best (shortest distance) match if one emotion matches with
   two colors.
"""
ep = EmotaPal(topn=100, unique_words=False).from_colors(clrs)
```

#### Constructing an EmotaPal from an image. 
Note: Do not make ```ncolors``` too high or you'll pick up non-central colors of an image. 

``` Python
""" 
Params:
  img (image): An image object. 
  ncolors (int): Construct a palette from the topn most dominant colors of an image. 
  topn (int, optional): see above
  unique_words (bool, optional): see above
"""
ep = EmotaPal(topn=100, unique_words=False).from_image(img, ncolors)
```

#### Constructing an EmotaPal from a url pointing to an image. 

``` Python
""" 
Params:
  url (str): A url pointing to an image.
  ncolors (int): Construct a palette from the topn colors of an image. 
  topn (int, optional): see above
  unique_words (bool, optional): see above
"""
ep = EmotaPal(topn=100, unique_words=False).from_url(url, ncolors)
```

#### Constructing an EmotaPal from a Google Images query. 

``` Python
""" 
Params:
  query (str): A Google Images query. 
  nimages (int): The number of images to scrape.
  topn (int, optional): see above
  unique_words (bool, optional): see above
"""
ep = EmotaPal(topn=100, unique_words=False).from_gimages(query, nimages)
```

### EmotaPal information and methods
``` Python
ep = EmotaPal().from_url(url)
```
#### Return the info of an EmotaPal. 
An EmotaPal's info is a list of dictionaries, each element containing information on a color, its associated emotion, 
and the distance between the input color and emotion color. This dictionary is sorted by distance (ascending order), 
such that the first entry is the best match and last entry is worst match. 

``` Python
info = ep.info 
```
#### Words

``` Python
words = ep.words.text # return words of EmotaPal
sentiment = ep.words.sentiment # return sentiment of EmotaPal's words
```

#### Colors
``` Python
rgbs = ep.colors.as_rgb # return colors as rgb values
hexs = ep.colors.as_hex # return colors as strings of hex values
ep.colors.display(save_img=False) # display color palette with option to save image
```


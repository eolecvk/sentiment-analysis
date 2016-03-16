# sentiment-analysis

## Roadmap
    
### Sources

    Collect sentiment dictionnary
    - positive-words.txt
    - negative-words.txt
    
    Collect mapping stemmed word-unstemmed word
    - mxm_reverse_mapping.txt
    
    Collect lyrics bag-of-words data file
    - mxm_dataset.db
    
    
    
### `mood_df`
#### Map each stemmed word with a mood score if available
    
    * INPUTS
    
      + STEMMED   | UNSTEMMED    mxm_reverse_mapping.txt
      + UNSTEMMED | MOOD (=1)    positive-words.txt
      + UNSTEMMED | MOOD (=-1)   negative-words.txt
            
            
    * OUTPUT
    
      + STEMMED | MOOD
            
           
           
### `lyrics_df`
#### dataFrame with Tracks, Count positive, Count negative, Count no mood info

    * INPUTS
    
      + TRACK_ID | STEMMED | COUNT | ISTEST      mxm_dataset.db        
      + STEMMED | MOOD                           mood.df
           
           
    * OUTPUT:
    
      + TRACK_ID | COUNT_POSITIVE | COUNT_NEGATIVE | COUNT_OTHER


### `final_df`

    * INPUT
    
       + TRACK_ID | COUNT_POSITIVE | COUNT_NEGATIVE | COUNT_OTHER
      
      
    * OUTPUT
    
      + TRACK_ID | TRACK_MOOD  lyrics_terms_df


* OUTPUT:

  + TRACK_ID | COUNT_POSITIVE | COUNT_NEGATIVE | COUNT_OTHER
final_df
* INPUT

   + TRACK_ID | COUNT_POSITIVE | COUNT_NEGATIVE | COUNT_OTHER


* OUTPUT

  + TRACK_ID | TRACK_MOOD  lyrics_terms_df

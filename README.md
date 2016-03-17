# sentiment-analysis

### Inputs

1. Download sentiment lexicons [here](http://www.cs.uic.edu/~liub/FBS/opinion-lexicon-English.rar). Comes as two text files: `positive-words.txt` and `negative-words.txt`.
2. Download the mapping file stemmed words to unstemmed words: [mxm_reverse_mapping.txt](http://labrosa.ee.columbia.edu/millionsong/sites/default/files/mxm_reverse_mapping.txt) 
3. Download the lyrics bag-of-words SQLite database: [mxm_dataset.db](http://labrosa.ee.columbia.edu/millionsong/sites/default/files/AdditionalFiles/mxm_dataset.db)
    
    
    
### 1. Initialize mood data

Run `initialize_mood_data.py` to create `mood_df`.
`mood_df` is a Pandas DataFrame mapping each stemmed word with a mood score if available in the sentiment lexicons
    
Inputs:
* `STEMMED`   | `UNSTEMMED`    // `mxm_reverse_mapping.txt`
* `UNSTEMMED` | `MOOD` *(=1)*    // `positive-words.txt`
* `UNSTEMMED` | `MOOD` *(=-1)*   // `negative-words.txt`

Output:
* `STEMMED` | `MOOD`          // `mood_df`  


### 2. Retrieve lyrics data

Run `initialize_lyrics_data.py` to create `lyrics_df`.
`lyrics_df`is a Pandas DataFrame with the following fields: `track_ID`, `<word_1>`, ..., `<word_n>` and `count_others`.

`<word_1>`, ..., `<word_n>` are all the stemmed words retrieved from the sentiment lexicons and those field hold the count of each of those word for the corresponding `track_id`.
`count_others` hold the count value of all the words that are not listed in the sentiment lexicons for the corresponding `track_id`.


Run `fill_lyrics_data.py` to populate `lyrics_df`.

Inputs
* `TRACK_ID` | `STEMMED` | `COUNT` | `ISTEST`     // `mxm_dataset.db`    
* `STEMMED` | `MOOD`                              // `mood.df`
    
Output
* `TRACK_ID` | `<word_1>` | ... | `<word_n>` | `count_others`


### 3. Compute lyrics mood score

Inputs
* `TRACK_ID` | `COUNT_POSITIVE` | `COUNT_NEGATIVE` | `COUNT_OTHER`
    
Output
* `TRACK_ID` | `TRACK_MOOD` | `lyrics_terms_df`

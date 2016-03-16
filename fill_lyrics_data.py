import pandas as pd
import numpy as np
import pickle
import sqlite3
import itertools

lyrics_path = '/home/eolus/Documents/MA755_data/LyricsData'
pickle_path = '/home/eolus/Documents/MA755_data/myPickles'


# Open output DataFrame
try:
	# Open `full_df_lyrics.pkl` if exists
	lyrics_df = pd.read_pickle(pickle_path+'/full_df_lyrics.pkl')
except:
	# Open initialized `lyrics_df` otherwise
	lyrics_df = pd.read_pickle(pickle_path+'/df_lyrics.pkl')


# Access MXM data stored in SQLite using Python and Pandas
con = sqlite3.connect(lyrics_path +'/mxm_dataset.db')
c = con.cursor()

'''
#Count total# rows
#c.execute('SELECT COUNT(*) FROM lyrics')
#result = c.fetchone()
#print(result[0])
'''

# Get the remaining list of track_id to process
try:
	# Retrieve from pickle file if exists
	track_list = pickle.load(open(pickle_path + '/track_stack.pkl', 'rb')
except:
	# Generate from .db query otherwise
	c.execute('SELECT DISTINCT track_id FROM lyrics')
	data_track_id = c.fetchall()
	
	#Get set of unique track_id's
	track_set = set(itertools.chain.from_iterable(data_track_id))

	# Convert to list for slicing (create a buffer..)
	track_list = []
	track_list.extend(track_set)

	# Save to pickle
	pickle.dump(track_list, open(pickle_path + '/track_stack.pkl', 'wb'))


# Nightmarish while loop
while (len(track_list) > 0):

	# Select a bunch of track_id for processing: track_buffer
	if (len(track_list) >= 100):
		track_buffer = track_list[0:99]
	else:
		track_buffer = track_list

	# Query for track data in track_buffer
	placeholder= '?' # For SQLite. See DBAPI paramstyle.
	placeholders= ', '.join(placeholder for unused in track_buffer)
	query= 'SELECT * FROM lyrics WHERE track_id IN (%s)' % placeholders

	# Iterate through tokenized row object (tuple)
	#	[0]				[1]	   		[2]	  		[3]   	[4]
	# 	track_id	|	mxm_id	| 	word 	| 	count |	is_test	
	for row in c.execute(query, track_buffer):
		word = row[2].upper()
		track_id = row[0]

		try:
			lyrics_df.loc[track_id][word] += row[3]
		except:
			lyrics_df.loc[track_id]['COUNT_OTHER'] += row[3]


	# Save complete `lyrics_df` in pkl file
	lyrics_df.to_pickle(pickle_path+'/full_df_lyrics.pkl')

	# Remove buffered value from track_list
	track_list = track_list[len(track_buffer):]
	# Save to pickle
	pickle.dump(track_list, open(pickle_path + '/track_stack.pkl', 'wb'))

'''
# Retrieve `lyrics_df`
lyrics_df = pd.read_pickle(pickle_path+'/full_df_lyrics.pkl')
print(lyrics_df.head())

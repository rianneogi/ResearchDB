from Index import *

notify2.init("PyPapersDB")

load_json(gJSONfilename)
# gPapers = []

# for i in range(len(gPapers)):
	# gPapers[i]['tags'] = []

# print(getAuthorsInitials([{'family': 'K. Vishnoi', 'given': 'Nisheeth'}]))

# remove_unindexed_files()
# index_dir('/home/rian/Documents/Research Papers/TCS/')
index_dir('/home/rian/Documents/Books/TCS/')
# remove_nonexistent_files()
# index_with_semantic_scholar('/home/rian/Documents/Research Papers/Algorithms/')
# reparse_files()
# remove_dupes()
# query_semantic_scholar('budgeted maximum coverage problem')
# query_google_scholar('budgeted maximum coverage problem')


save_json(gJSONfilename)

# print(gPapers)
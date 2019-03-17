import pandas as pd
import numpy as np


def normalize_text(t):
    return t.split('(')[0].rstrip().lower()


def main():
	s_data = pd.read_csv('BookList.csv')[['Title']]
	b_data = pd.read_csv('books.csv')[['id', 'title']]
	r_data = pd.read_csv('ratings.csv')
	b_data['title'] = b_data['title'].apply(normalize_text)
	s_data['Title'] = s_data['Title'].apply(normalize_text)
	joined = s_data.set_index('Title').join(b_data.set_index('title'))
	joined.dropna(inplace = True)
	joined.reset_index(inplace=True)
	joined.rename(columns={'index':'title'}, inplace=True)
	joined['id'] = joined['id'].apply(lambda x: int(x))
	common_ids = set(joined['id'])
	data = r_data[r_data['book_id'].isin(common_ids)]
	data.to_csv('user_rating_data.csv', index=False)

if __name__ == '__main__':
	main()

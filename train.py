import pandas as pd
import numpy as np
from scipy.sparse import coo_matrix
from fancyimpute import MatrixFactorization

if __name__ == '__main__':
    data = pd.read_csv('user_rating_data.csv')
    u_user_id = np.array(list(data['user_id'].unique()))
    u_book_id = np.array(list(data['book_id'].unique()))

    def u_map(x):
        return np.where(u_user_id == x)[0][0]

    def b_map(x):
        return np.where(u_book_id == x)[0][0]

    data['book_id'] = data['book_id'].apply(b_map)
    data['user_id'] = data['user_id'].apply(u_map)
    matrix = coo_matrix((np.array(data['rating']), (np.array(data['user_id']), np.array(data['book_id']))))
    sparse = matrix.toarray()
    sparse = np.where(sparse == 0, np.nan, sparse)
    full_m = MatrixFactorization().fit_transform(sparse)
    np.save('sparse_matrix', sparse)
    np.save('full_matrix', full_m)
    np.save('u_user_id', u_user_id)
    np.save('u_book_id', u_book_id)

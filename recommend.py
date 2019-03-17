import numpy as np
import pandas as pd
if __name__ == '__main__':

    sparse = np.load('sparse_matrix.npy')
    full_m = np.load('full_matrix.npy')
    u_user_id = np.load('u_user_id.npy')
    u_book_id = np.load('u_book_id.npy')
    b_data = pd.read_csv('books.csv')[['id', 'title']]
    b_data['title'] = b_data['title']

    def u_map(x):
        return np.where(u_user_id == x)[0][0]

    def b_map(x):
        return np.where(u_book_id == x)[0][0]

    def recommend(user_id, full, sparse):
        i = u_map(user_id)
        mask = np.isnan(sparse[i,])
        j = np.argmax(full[i,][mask])
        book_id = u_book_id[j]
        return list(b_data[b_data['id'] == book_id]['title'])

    run = True
    
    while run:
        user_id = int(input('Please input valid user_id:'))
        if user_id in u_user_id:
            print(recommend(user_id, full_m, sparse))
            response = input('Run another query (y/n)?')
            while response not in ['y', 'n']:
                response = input('Please input y or n:')
            if response == 'n':
                run = False
    		



# import numpy as np
# import faiss
# import glob
# import h5py

# # Load dataset vectors
# vectors = []
# paths = []

# for h5file in glob.glob("preprocessed_data/*/AudioNet*.hdf5"):
#     with h5py.File(h5file, 'r') as f:
#         vec = f['data'][0, 0, 0]
#         vectors.append(vec)
#         paths.append(h5file)

# vectors = np.array(vectors).astype('float32')


# index = faiss.IndexFlatL2(8000)  # 8000 = vector length
# index.add(vectors)  # Add all vectors to index

# def search(query_vector, k=5):
#     query_vector = np.array([query_vector]).astype('float32')
#     distances, indices = index.search(query_vector, k)
#     return [(paths[i], distances[0][idx]) for idx, i in enumerate(indices[0])]

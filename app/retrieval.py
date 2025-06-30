import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import librosa
import os

# Load saved features and file paths only once
features = np.load("app/model/mfcc_index.npy")
file_paths = np.load("app/model/file_paths.npy", allow_pickle=True)

def extract_mfcc(file_path, sr=16000, n_mfcc=13):
    y, _ = librosa.load(file_path, sr=sr)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    return np.mean(mfcc.T, axis=0)

def retrieve_similar(file_path, top_k=5):
    query_vec = extract_mfcc(file_path).reshape(1, -1)
    similarities = cosine_similarity(query_vec, features)[0]
    top_indices = similarities.argsort()[-top_k:][::-1]

    return [
        {"file_path": str(file_paths[i]), "score": float(similarities[i])}
        for i in top_indices
    ]

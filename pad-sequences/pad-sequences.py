import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here

    mxlen =0
    if max_len is not None:
        mxlen = max_len
    else:
        for seq in seqs:
            mxlen = max(mxlen, len(seq))

    result = np.full((len(seqs),mxlen), pad_value, dtype=int)

    for i,seq in enumerate(seqs):

        data_to_copy = seq[:mxlen]

        result[i, :len(data_to_copy)] = data_to_copy
            

    return result
    pass
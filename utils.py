# IMPORTS
import pandas as pd

# def nbest(d, n=1, print=False):
#     """
#     get n max values from a dict
#     :param d: input dict (values are numbers, keys are stings)
#     :param n: number of values to get (int)
#     :param print: if True returns a Pandas DataFrame of the `nbest` tokens.
#     :return: dict of top n key-value pairs
#     """
#     sorted_items = dict(sorted(d.items(), key=lambda item: item[1], reverse=True)[:n])
#     if print is not None:
#         top_n_values = [sorted_items[item] for item in sorted_items]
#         top_n_values = pd.DataFrame(top_n_values, columns= ['Frequency'])
#         top_n_labels = [item for item in sorted_items]
#         top_n_labels = pd.DataFrame(top_n_labels, columns=['Word'])
#         top_n_df = pd.merge(top_n_values, top_n_labels, left_index=True, right_index=True)
#         return top_n_df
#     else:
#         return sorted_items

def nbest(d, n=1):
    """
    get n max values from a dict
    :param d: input dict (values are numbers, keys are stings)
    :param n: number of values to get (int)
    :return: dict of top n key-value pairs
    """
    top_n = dict(sorted(d.items(), key=lambda item: item[1], reverse=True)[:n])
    top_n_values = [top_n[item] for item in top_n]
    top_n_values = pd.DataFrame(top_n_values, columns= ['Frequency'])
    top_n_labels = [item for item in top_n]
    top_n_labels = pd.DataFrame(top_n_labels, columns=['Word'])
    top_n_df = pd.merge(top_n_values, top_n_labels, left_index=True, right_index=True)
    return top_n_df
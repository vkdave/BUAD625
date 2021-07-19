import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

import graphviz as graphviz
from sklearn.datasets import load_iris
from sklearn import tree
import streamlit as st

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))
# testing the remote
dot_data = tree.export_graphviz(clf, out_file=None, 
                                feature_names=columns,  
                                class_names=iris.target_names,
                                filled=True)

# Draw graph
graph = graphviz.Source(dot_data, format="png") 
graph
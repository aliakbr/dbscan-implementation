#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:01:09 2017

@author: aliakbar
"""

import pandas as pd
import numpy as np
from sklearn.neighbors import DistanceMetric
from sklearn import preprocessing

def gower_distance(X):
    """
    This function expects a pandas dataframe as input
    The data frame is to contain the features along the columns. Based on these features a
    distance matrix will be returned which will contain the pairwise gower distance between the rows
    All variables of object type will be treated as nominal variables and the others will be treated as 
    numeric variables.
    Distance metrics used for:
    Nominal variables: Dice distance (https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient)
    Numeric variables: Manhattan distance normalized by the range of the variable (https://en.wikipedia.org/wiki/Taxicab_geometry)
    """
    individual_variable_distances = []

    for i in range(X.shape[1]):
        feature = X.iloc[:,[i]]
        if feature.dtypes[0] == np.object:
            feature_dist = DistanceMetric.get_metric('dice').pairwise(pd.get_dummies(feature))
        else:
            feature_dist = DistanceMetric.get_metric('manhattan').pairwise(feature) / np.ptp(feature.values)

        individual_variable_distances.append(feature_dist)

    return np.array(individual_variable_distances).mean(0)

FILE_NAME = 'CensusIncome/CencusIncome.data.txt'

dataset = pd.read_csv(FILE_NAME, sep=', ', engine='python')

# Normalize the numerical data
fnlwgt_normalized = preprocessing.scale(dataset['fnlwgt'].values.astype('float'))
capital_gain_normalized = preprocessing.scale(dataset['capital-gain'].values.astype('float'))
capital_loss_normalized = preprocessing.scale(dataset['capital-loss'].values.astype('float'))
hours_per_week_normalized = preprocessing.scale(dataset['hours-per-week'].values.astype('float'))

dataset['fnlwgt'] = fnlwgt_normalized
dataset['capital-gain'] = capital_gain_normalized
dataset['capital-loss'] = capital_loss_normalized
dataset['hours-per-week'] = hours_per_week_normalized

distance_metric = gower_distance(dataset)
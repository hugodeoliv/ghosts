import unittest
from data_io import write
from model import model
import pickle
import numpy as np   # We recommend to use numpy arrays
from os.path import isfile
from sklearn.base import BaseEstimator
import tobit
import pandas as pd
import zePreproDeLaMort
from data_io import read_as_df


class Test(unittest):
    
    """
    On teste si les il y a des donnees cesurees apres le preprocessing
    """
    def testPrepro():
        filename1 = "public_data/Mortality_train.data"
        dataset = np.loadtxt(filename1, delimiter=" ")
        prepro = zePreproDeLaMort()
        fitTab = prepro.fit(dataset)
        transformTab = prepro.transform(fitTab)
        for i in transformTab:
            self.assertEqual(i, 1, msg="Censored")
        self.assertRaises(ValueError, prepro.transform(fitTab))
    """
    On verifie que chaque 
    """
    
    """
    def testPrediction():
        model_dir = 'sample_code_submission/'
        problem_dir = 'ingestion_program/'  
        score_dir = 'scoring_program/'
        data = read_as_df('public_data'  + '/' + data_name)
     """   
        
        
        
        
        
        
        
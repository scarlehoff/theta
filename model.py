#!/usr/bin/env sage
# -*- coding: utf-8 -*-

import numpy as np
import copy

class Model(object):
    
    def __init__(self):
        """ Init
        """
        self._layers = [] 
        
        self._Np = 0
   
    def add(self, L):
        
        if len(self._layers) == 0 or self._layers[-1].get_Nout()==L.get_Nin():
            # Add the layer
            self._layers.append(L)
            
            # Increase the parameter counter
            self._Np = self._Np + L.get_Nparameters()
            
            # Refresh the parameter bounds
            self.generate_bounds()
            
        else: 
            print("Input of layer does not match output of previous layer! => Add ignored")

    def feedthrough(self, X):
        """ Feeds the input X through all layers 
            Vectorized
        """ 

        x = X

        for L in self._layers:
            
            x = L.feedin(x)

        return x

    def __call__(self, data):
        """Evaluates the model for a given data array"""
    
        return self.feedthrough(data)

    def copy(self):
        return copy.deepcopy(self)
    
    def get_parameters(self):
        """ Collects all parameters and returns a flat array """
        R = []
        for L in self._layers:
            R.append(L.get_parameters())
            
        return np.concatenate(R)

    def generate_bounds(self):
        """ Collects the bounds of the individual layers """
        A_L = []
        A_U = []
        
        for L in self._layers:
            bl, bu = L.get_bounds()
            A_L.append(bl)
            A_U.append(bu)
         
        self._lower_bounds = np.concatenate(A_L).tolist()
        self._upper_bounds = np.concatenate(A_U).tolist()
    
    def get_bounds(self):
        """ Returns the bounds """
        return self._lower_bounds, self._upper_bounds
    
    def size(self):
        return self._Np
    
    def assign_params(self,P):
        """ Set to the given parameters """
        Nt = 0
        
        for L in self._layers:
            
            L.set_parameters(P[Nt:Nt+L.get_Nparameters()])
        
            Nt = Nt + L.get_Nparameters() 

    def predict(self,X):
        """ Performs prediction with the trained model """

        return self.feedthrough(X)
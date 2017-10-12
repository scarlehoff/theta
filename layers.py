from abc import ABCMeta, abstractmethod

import rtbm as rtbm
import numpy as np

class Layer(object):
    """ Abstract class for a layer of a deep network """
    __metaclass__ = ABCMeta
 
    
    @abstractmethod
    def feedin(self, X):
        return 0
    
    @abstractmethod
    def get_parameters(self):
        return 0
    
    @abstractmethod
    def set_parameters(self,P):
        return 0
    
    @abstractmethod
    def get_Nparameters(self):
        return 0
    
    @abstractmethod
    def get_bounds(self):
        return 0
    
    def get_Nin(self):
        return self._Nin
    
    def get_Nout(self):
        return self._Nout
    
    
    
class ThetaUnitLayer(Layer):
    """ A layer of log-gradient theta units """

    def __init__(self, Nin, Nout, param_bound=10):
        self._Nin  = Nin
        self._Nout = Nout

        # Parameter init
        self._bh = np.random.uniform(-1, 1,(Nout,1)).astype(complex)
        self._w  = np.random.uniform(-1, 1,(Nin,Nout)).astype(complex)
        self._q  = 10*np.diag(np.random.rand(Nout)).astype(complex)
     
        self._Np = 2*self._Nout+self._Nout*self._Nin
        
        # Generate allowed bounds
        self.generate_bounds(param_bound)
        
    def feedin(self,X):
        """ Feeds in the data X and returns the output of the layer 
            Note: Vectorized 
        """

        return np.array(rtbm.factorizedHiddenExpectation(X,self._bh,self._w,self._q))

    def get_parameters(self):
        """ Returns the parameters as a flat array 
            [bh,w,q]
        """

        return np.concatenate((self._bh.flatten(),self._w.flatten(),self._q.flatten()))

    def set_parameters(self,P):
        """ Set the matrices from flat input array P 
            P = [bh,w,q]
        """
        index = 0
        
        self._bh = P[index:index+self._bh.shape[0]].reshape(self._bh.shape)
        index += self._bh.shape[0]

        self._w = P[index:index+self._w.size].reshape(self._w.shape)
        index += self._w.size

        np.fill_diagonal(self._q, P[index:index+self._q.shape[0]])

    def get_Nparameters(self):
        """ Returns total # parameters """
        
        return self._Np
    
    def generate_bounds(self, param_bound):
      
        self._lower_bounds = [-param_bound for i in range(self._Np)]
        self._upper_bounds = [ param_bound for i in range(self._Np)]

        # set q positive
        index = self._Np-self._q.shape[0]
        self._lower_bounds[index:] = [1E-5]*self._q.shape[0]

    
    def get_bounds(self):
        """ Returns the set bounds as arrays """
        return self._lower_bounds, self._upper_bounds 
    
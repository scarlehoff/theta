:github_url:

Examples and tutorials
======================

We have prepared some basic ipython notebooks in the :code:`examples`
folder to demonstrate the functionality of the package. Here, we give
only two simple examples to show the general usage pattern.


Probability estimation
######################

Let's consider the example of training a RTBM to learn a
gaussian probability distribution.

1. The first step consists in generating normal distributed data::

     import numpy as np
     n = 1000
     data = (np.random.normal(5, 10, n)).reshape(1, n)

2. Then we allocate a RTBM with one visible and 2 hidden units::

     from theta.rtbm import RTBM

     model = RTBM(1, 2, init_max_param_bound=20, random_bound=1)

   In this example we have set ``random_bound=1`` to control the
   maximum random value for the Shur complement initialization. The
   ``init_max_param_bound=20`` controls the maximum value allowed for
   all parameters during training with the CMA-ES minimizer. Both
   flags may require tuning in order to obtain the best model results.

3. We train the model with the CMA-ES minimizer::
	  
     from theta.minimizer import CMA
     from theta.costfunctions import logarithmic
   
     minim = CMA(False)
     solution = minim.train(logarithmic, model, data, tolfun=1e-4)   

4. The learned probabilities for given data can be queried via::

     model.predict(data)
     

.. note:: Be aware that fine tuning of parameters is required in order
   to achieve good training results. This can be achieved by varying
   ``random_bound`` and ``init_max_param_bound`` for RTBMs.

   Also, the minimization algorithm provides extra options that may
   need to be adjusted in order to get acceptable results.
     
     
Data regression and classification
##################################

Let's now consider a data regression problem.

1. Suppose we have ``X_train`` and ``Y_train`` numpy arrays
   with respectively the support and target data. We allocate a
   ``DiagExpectationUnitLayer`` with ``Nin=X_train.shape[0]`` and
   ``Nout=X_train.shape[1]``::

     from theta.model import Model
     from theta.layers import DiagExpectationUnitLayer

     model = Model()
     model.add(DiagExpectationUnitLayer(Nin, Nout, phase=1,
                                        Q_init=uniform(2,4)))

   In this example we have also set an optional random uniform
   initialization for the :math:`Q` parameters through the ``Q_init``
   flag. The model is trained in phase I (``phase=1``).

2. Then we train the model using ``SGD``::

     from theta.minimizer import SGD
     from theta.costfunctions import mse
     from theta.gradientschemes import RMSprop
     from theta.initializers import uniform
   
     minim = SGD()
     solution = minim.train(mse, model, X_train, Y_train,
                            scheme=RMSprop(), lr=0.01)

   For this particular setup we are using the mean square error cost
   function (``mse``) with stochastic gradient descent in the RMS
   propagation scheme (``scheme=RMSprop()``). The learning rate is
   ``lr=0.01`` and may require tuning before getting the best results.   

   When using SGD, it is possible to split the data into training and
   validation datasets automatically, by using the
   ``validation_split`` option, or by passing extra datasets, see
   ``theta.minimizer.SGD.train`` for more details.
   
3. Predictions of the model can be obtained via::

     model.predict(data)


.. note::
   In order to achieve good training results please check for each
   layer the optional parameters concerning initialization.
   
   The SGD algorithm requires fine tuning of parameters such as the
   learning rate, scheme and batch size.

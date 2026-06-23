{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3170da94",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np \n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "5007588a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "X :  [[1659.01    2.  ]\n",
      " [1468.52    1.  ]\n",
      " [1704.31    5.  ]\n",
      " ...\n",
      " [1298.4     5.  ]\n",
      " [1658.73    4.  ]\n",
      " [1703.32    2.  ]]\n",
      "Y :  [864521.86 722252.75 939413.7  ... 807821.52 825368.42 782359.54]\n",
      "BETA :  [[0.77 0.44 0.86 ... 0.17 0.37 0.48]\n",
      " [0.72 0.71 0.2  ... 0.85 0.67 0.14]]\n"
     ]
    }
   ],
   "source": [
    "data = pd.read_csv(\"./data/housing_demo.csv\")\n",
    "np.set_printoptions(precision=2, suppress=True)\n",
    "\n",
    "X = data.to_numpy()[:,:-1]\n",
    "Y = data.to_numpy()[:,2]\n",
    "\n",
    "print(\"X : \",X)\n",
    "print(\"Y : \",Y)\n",
    "\n",
    "# dimention = x.size() * x[0].size()\n",
    "rng = np.random.default_rng(seed=42)\n",
    "beta_param = rng.random(size=(len(X[0]), len(X)))\n",
    "print(\"BETA : \",beta_param)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e33dfc70",
   "metadata": {},
   "outputs": [],
   "source": [
    "# impliment ridge regression \n",
    "\n",
    "L = 0.3;\n",
    "I = np.identity(size=(len(X), len(X[0])))\n",
    "B_Ridge = X.T @ X + L "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

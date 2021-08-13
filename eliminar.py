import numpy as np
import pandas as pd

numpy_data = np.array([[1, 2], [3, 4]])
df = pd.DataFrame(data=numpy_data, index=["row1", "row2"], columns=["column1", "column2"])
print(df)
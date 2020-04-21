import numpy as np
import pandas as pd
import pandas_profiling
import pandas as pd

#read in the file; look at the basic statistics


df = pd.read_csv('georegistration_table.tsv', sep='\t', header=0)

print (df.head())
#for column in df.columns:  print("|%s|"%column)
print (df['country_code'].describe())

#generate a pandas profiling
profile = df.profile_report(title='Pandas Profiling Report')
profile.to_file(output_file="data_qc_report_pandas.html")
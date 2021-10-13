# This file is to create some easy helper function imports to assist with EDA

def propna(df):
  '''simple function that gives a proportion of na values '''
  return df.isna().sum()/len(df);

def visualna(df):
  '''create a heatmap of missing values'''
  import seaborn as sns
  return sns.heatmap(df.isna(), cbar = False, cmap="Blues_r");

def corheatmap(data):
  '''Function to create a correlation matrix and heatmap'''
  import seaborn as sns
  import numpy as np
  corr_matrix = data.corr()
  mask = np.zeros_like(corr_matrix, dtype=np.bool)
  mask[np.triu_indices_from(mask)]= True

  f, ax = plt.subplots(figsize=(20, 25)) 
  heatmap = sns.heatmap(corr_matrix, 
                        mask = mask,
                        square = True,
                        linewidths = .5,
                        cmap = 'coolwarm',
                        cbar_kws = {'shrink': .4, 
                                  'ticks' : [-1, -.5, 0, 0.5, 1]},
                        vmin = -1, 
                        vmax = 1,
                        annot = True,
                        annot_kws = {'size': 12})
  #add the column names as labels
  ax.set_yticklabels(corr_matrix.columns, rotation = 0)
  ax.set_xticklabels(corr_matrix.columns)
  sns.set_style({'xtick.bottom': True}, {'ytick.left': True});

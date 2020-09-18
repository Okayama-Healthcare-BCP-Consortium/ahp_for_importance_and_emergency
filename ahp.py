import pandas as pd


def calc_ahp(path):

    df = pd.read_excel(path, index_col=0)

    alpha_importance = df.loc['重み', 'Importance']
    alpha_emergency = df.loc['重み', 'Emergency']

    df = df.iloc[:-1]

    total_importance = df['Importance'].sum()
    total_emergency = df['Emergency'].sum()

    task2score = dict()
    for task, row in df.iterrows():
        task2score[task] = alpha_importance * (row['Importance'] / total_importance) + alpha_emergency * (row['Emergency'] / total_emergency)
        
    return sorted(task2score.items(), key=lambda x: x[1], reverse=True)
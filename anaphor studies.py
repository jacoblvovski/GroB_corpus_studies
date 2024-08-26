import pandas as pd

from temporarymodules.simplecompling import *

poems_df = pd.read_csv('Корпус Летова v1.1_NER.csv', encoding='utf-8')

poems = list(poems_df['text'])
poems = [str(poem) for poem in poems]
dicts_with_shares = [calculate_share_of_repeated_elements_with_set(poem) for poem in poems]
lines_df = pd.DataFrame.from_records(dicts_with_shares)

#poems_df_new = pd.concat([poems_df, lines_df])

lines_df.to_excel('Метрики анафоры v4.xlsx')
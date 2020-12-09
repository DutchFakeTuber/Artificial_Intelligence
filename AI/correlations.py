from dataset import get_dataset, TOTAL_QUESTIONS
from pandas import DataFrame

dataset = get_dataset()


df = DataFrame(result, columns=[f'question_{i + 1}' for i in range(TOTAL_QUESTIONS)])
df.corr().to_csv('data.csv')

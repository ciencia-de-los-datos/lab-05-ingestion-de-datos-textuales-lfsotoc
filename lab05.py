
import pandas as pd
import glob

# Lista de archivos txt en el directorio especificado
file_negativetest = glob.glob(r"C:/Users/lfsoto/Github/lab-05-ingestion-de-datos-textuales-lfsotoc/data/test/negative/*.txt")
file_neutraltest = glob.glob(r"C:/Users/lfsoto/Github/lab-05-ingestion-de-datos-textuales-lfsotoc/data/test/neutral/*.txt")
file_positivetest = glob.glob(r"C:/Users/lfsoto/Github/lab-05-ingestion-de-datos-textuales-lfsotoc/data/test/positive/*.txt")
file_negativetrain = glob.glob(r"C:/Users/lfsoto/Github/lab-05-ingestion-de-datos-textuales-lfsotoc/data/train/negative/*.txt")
file_neutraltrain = glob.glob(r"C:/Users/lfsoto/Github/lab-05-ingestion-de-datos-textuales-lfsotoc/data/train/neutral/*.txt")
file_positivetrain = glob.glob(r"C:/Users/lfsoto/Github/lab-05-ingestion-de-datos-textuales-lfsotoc/data/train/positive/*.txt")




dfnt = []
dfnet = []
dfpt = []

for file in file_negativetest:
    with open(file, 'r', encoding='utf-8') as f:
        negativetest = f.read()
        dfnt.append(negativetest)

df1 = pd.DataFrame(dfnt, columns=['phrase'])
df1['sentiment'] = 'negative'

for file in file_neutraltest:
    with open(file, 'r', encoding='utf-8') as f:
        neutraltest = f.read()
        dfnet.append(neutraltest)

df2 = pd.DataFrame(dfnet, columns=['phrase'])
df2['sentiment'] = 'neutral'

for file in file_positivetest:
    with open(file, 'r', encoding='utf-8') as f:
        positivetest = f.read()
        dfpt.append(positivetest)

df3 = pd.DataFrame(dfpt, columns=['phrase'])
df3['sentiment'] = 'positive'

df_concatenado = pd.concat([df1, df2, df3], ignore_index=True)
df_concatenado.to_csv("test_dataset.csv", index=False)

print(df_concatenado['sentiment'].value_counts())



dfntr = []
dfnetr = []
dfptr = []

for file in file_negativetrain:
    with open(file, 'r', encoding='utf-8') as f:
        negativetrain = f.read()
        dfntr.append(negativetrain)

df4 = pd.DataFrame(dfntr, columns=['phrase'])
df4['sentiment'] = 'negative'

for file in file_neutraltrain:
    with open(file, 'r', encoding='utf-8') as f:
        neutraltrain = f.read()
        dfnetr.append(neutraltrain)

df5 = pd.DataFrame(dfnetr, columns=['phrase'])
df5['sentiment'] = 'neutral'

for file in file_positivetrain:
    with open(file, 'r', encoding='utf-8') as f:
        positivetrain = f.read()
        dfptr.append(positivetrain)

df6 = pd.DataFrame(dfptr, columns=['phrase'])
df6['sentiment'] = 'positive'
df_concatenado1 = pd.concat([df4, df5, df6], ignore_index=True)
df_concatenado1.to_csv("train_dataset.csv", index=False)

# print(df_concatenado1['sentiment'].value_counts())
import pandas as pd 
try:
    def get_urls():
        df=pd.read_csv('data.csv')
        data={'Category':list(df['Category']),'URL':list(df['URLs'])}
        return data
except:
    pass
if __name__ == '__main__':
    print(get_urls())
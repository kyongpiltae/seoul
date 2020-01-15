import numpy as np
import pandas as pd


def get_ratings_numpy(df):
    # ============================================
    # TODO : datafame을 인자로 받지만, numpy를 이용해서 각 영화별 평점(평균)을 구한다.
    #      [input] : dataframe of pandas 
    #       
    #      [output] : 영화 id별 평점 평균이 담겨있는 data
    # arr = np.array(df)      # Hint
    # np.unique , np.where 
   
    # ================ EDIT HERE =================
   
    '''
    userId,movieId,rating,timestamp
    '''
    arr = np.array(df)
    #print(arr[:,1:3].shape)

    newarr =arr[:,1:3]

    lu = np.unique(newarr[:,0:1])
    print(lu.shape)
    print(newarr.shape)
    
    rating_dic =dict()
    for id in lu:
        data =newarr[np.where(newarr[:,0] == id)][:,1]
        rating_dic[id]= np.mean(data)
  
    ratings = rating_dic
    #ratings =[k,v for k,v in rating_dic.items() ]
    print(ratings)
    # ============================================
    return ratings

def get_ratings_pandas(df):
    # ============================================
    # TODO : pandas를 이용해서 get_ratings_numpy와 같은 기능을 하는 함수를 만든다.
    #        즉, 영화별 평점 평균을 반환한다.
    #      [input] : dataframe of pandas 
    #       
    #      [output] : 영화 id별 평점 평균이 담겨있는 data
    # ================ EDIT HERE =================
    ratings = df.groupby('movieId').mean()['rating']
    print(ratings)
  

    # ============================================
    return ratings

def get_genres_cloumns(df):
    # ============================================
    # TODO : datafame의 영화 genres column에 있는 genre들을 unique하게 반환하는 함수
    #      [input] : dataframe of pandas 
    #       
    #      [output] : list 형태, genres 안에 있는 genre들을 담은 list
    # ================ EDIT HERE =================
   
    '''
    genre_columns= df['genres'].unique()

    newSet = set()

    for data in genre_columns:
        nl =data.split("|")
        newSet.update(nl)

    genre_columns = newSet
    print(genre_columns)
    '''
    
    genre_columns= list( set ( [ j for i in df.genres.str.split('|') for j in i ]))
    print(genre_columns)


    # ============================================
    return genre_columns

def make_df_to_oneshot(df,genre_columns):
    # ============================================
    # TODO : datafame에 있는 genres column을 one shot encoding을 해서, 각 genre별 column을 만들어서 
    #        해당 영화의 장르인 경우에 1로 표시한다. (앞에서 lab에서 했던 결과와 동일)
    #      [input] : (dataframe of pandas, genre의 column들의 list)
    #       
    #      [output] : None or 필요없어진 genres의 column을 제거한 dataframe
    # ================ EDIT HERE =================
    columns = df['genres']
    print(len(genre_columns))

    hot_enoding = np.zeros((len(columns), len(genre_columns)))

    rowindex = 0
    for data in columns:
        nl =data.split("|")
        colindex = 0
        for d in nl:
            if d in genre_columns:
                hot_enoding[rowindex,colindex]=1
                colindex +=1 


        rowindex += 1

    print(hot_enoding)
    # ============================================
    return hot_enoding

if __name__ == '__main__':
    ratings_path = 'ratings.csv'
    movies_path = 'movies.csv'
    ratings = pd.read_csv(ratings_path)
    movies = pd.read_csv(movies_path)
    '''
    movieId,title,genres
    userId,movieId,rating,timestamp
    '''
    #print(ratings.head(5))
    #print(movies.head(5))


    # =============== 영화 평점 평균 ================
    #ratings_n = get_ratings_numpy(ratings)
    #ratings_p = get_ratings_pandas(ratings)
    # ============================================
    
    # ============ one shot encoding =============

    genre_columns = get_genres_cloumns(movies)
    make_df_to_oneshot(movies,genre_columns)
    # ============================================
    #print(genre_columns)
    #print(movies)
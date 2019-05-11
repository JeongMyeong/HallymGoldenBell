import pandas as pd




df= pd.read_csv("goldenbell.csv",encoding='cp949')


check_list=[2, 6, 9, 12, 19, 20, 21, 23, 25, 26,
            28, 33, 35, 38, 45, 49, 55, 58, 61, 62,
           63, 65, 67, 70, 72, 75, 76, 77, 78, 82, 85, 87,
           94]    # 모르는 문제만 골라서 리스트에 넣는다.




for i in check_list:
    print("{}번) {}".format(i, df['문제'][i-1]))
    answer = input("입력 >> ")
    if answer == df['답'][i-1]:
        print("정답입니다.\n\n")
    else:
        print("오답입니다. 정답은 {} 입니다.\n\n".format(df['답'][i-1]))

print(df.head())







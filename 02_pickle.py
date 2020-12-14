# 모듈 불러오기
import pickle

# 저장하기
file = open("pickle.txt", "wb")
color = {"lion":"yellow", "kitty":"red"}
pickle.dump(color, file)
file.close()

# 불러오기
file = open("pickle.txt", "rb")
data = pickle.load(file)
file.close()

# 출력해보기
print(data["lion"])
print(data["kitty"])
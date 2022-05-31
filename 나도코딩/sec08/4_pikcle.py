import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 file에 저장
# profile_file.close()

with open("profile.pickle","rb") as profile_file:
    profile = pickle.load(profile_file) # 파일의 내용을 가져오기
print(profile)
profile_file.close()
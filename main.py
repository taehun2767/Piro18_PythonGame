import random
from interface_function import drinkingGame, printGameList, printIntro, printSelectLimit

playerList = []
playerLimit = []

friendList = ["유민", "건", "다은", "서진", "태훈"]
friendLimit = [2, 4, 6, 8, 10]

# 인트로 출력
printIntro()  #아래 내용을 interface_function에서 가져와서 출력

# 게임 진행 여부 판단
start = False
while not start:
  startGame = input("게임을 진행할까요? (y/n) : ")
  
  if startGame == "y" or startGame == "Y" :
    start = True
  elif startGame == "n" or startGame == "N":
    print("준비가 안되셨군요. 편하실 때 말씀해주세요.")
  else:
    print("잘못된 입력입니다. 다시 입력해주세요.")

userName = input("오늘 거하게 취해볼 당신의 이름은? : ")
playerList.append(userName) #게임참가할 유저를 플레이어리스트에 추가

# 주량 선택 출력
printSelectLimit()  #아래 내용을 interface_function에서 가져와서 출력

#치사량 선택
correctLimit = False
while not correctLimit:
  userDrinkingLimit = input("당신의 😵치사량(주량)은 얼마만큼인가요?(1~5를 선택해주세요) : ")
  if not str.isdigit(userDrinkingLimit):
    print("잘못된 값을 입력하셨습니다. 다시 입력해주세요!")
  elif 1 <= int(userDrinkingLimit) <= 5:
    correctLimit = True
  else:
    print("1부터 5사이의 정수를 골라주세요!")

playerLimit.append(friendLimit[int(userDrinkingLimit)-1]) #게임참가할 유저 주량을 플레이어주량리스트에 추가

#게임할 인원 선택
correctFriendNumber = False
while not correctFriendNumber:
  friendNumber = input("함께 취할 친구들은 얼마나 필요하신가요?\
(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : ")  # \ 역슬래쉬는 보기 편하기 위해 코드 줄바꿈 의미- 출력엔 영향 x

  if not str.isdigit(friendNumber):
    print("잘못된 값을 입력하셨습니다. 다시 입력해주세요!")
  elif 1 <= int(friendNumber) <= 3:
    correctFriendNumber =True
    print(correctFriendNumber)
  else:
    print("1부터 3사이의 정수를 골라주세요!")

loseCount = [0 for _ in range(int(friendNumber)+1)]  # 남은 치사량을 출력하기 위해 진 횟수를 카운트하는 리스트 생성

if userName in friendList:           # 입력받은 유저 이름이 친구들 이름과 중복될 수 있으므로
  idx = friendList.index(userName)   #중복되는 경우 userName 리스트에서 삭제 후 random하게 뽑아야함
  del friendList[idx]

for i in range(int(friendNumber)):
  playerNameIndex = random.randint(0, len(friendList)-1)  #친구들 리스트에서 랜덤하게 인덱스 선택
  playerLimitIndex = random.randint(0, 4)               #주량   리스트에서 랜덤하게 인덱스 선택
  
  
  friendName = friendList[playerNameIndex]                    #인덱스 기반으로 게임에 참여할 친구 선택
  LimitOfFriend = friendLimit[playerLimitIndex]   #인덱스 기반으로 게임 참여할 친구의 주량 선택
  playerList.append(friendName)
  playerLimit.append(LimitOfFriend)
  
  friendList.remove(friendName) # 뽑힌 친구가 다시 선택되어 중복되지 않도록 리스트에서 중복 제거
  print(f"오늘 함께 취할 친구는 {friendName}입니다! (치사량 : {LimitOfFriend})") # f-string  => 원하는 위치에 변수 넣으면서 출력 가능
  
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# 지금까지의 정보를 클래스에 인수로 넣어줘서 drinkingGame의 객체 생성
drinkGame = drinkingGame(playerList, playerLimit, loseCount)

# userName이 게임 선택하면서 시작
drinkGame.printLimit()
printGameList()
drinkGame.selectGame(userName)
drinkGame.changeStatus()

while True:

  drinkGame.printLimit()
  printGameList()
  keepGoing = input('술게임 진행중! 다른 사람의 턴입니다. 그만하고 싶으면 "exit"를, 계속하고 싶으면 아무키나 입력해주세요! :')
  if keepGoing == 'exit':
    print(f"{userName}님이 게임을 종료하셨습니다.")
    break
  drinkGame.selectGame(drinkGame.lastLoser)  #마지막으로 진 사람이 게임 선택
  drinkGame.changeStatus()       # 치사량 및 진 횟수 업데이트
  # print(drinkGame.playerLimit)   # 치사량 및 진 횟수 출력
  if 0 in drinkGame.playerLimit: # 게임이 끝난 경우
    drinkGame.printGameOver()
    break
import random

cards=['R1','R1','R1','R2','R2','R3','R3','R4','R4','R5',
       'B1','B1','B1','B2','B2','B3','B3','B4','B4','B5',
       'W1','W1','W1','W2','W2','W3','W3','W4','W4','W5',   #카드 목록 
       'Y1','Y1','Y1','Y2','Y2','Y3','Y3','Y4','Y4','Y5',
       'G1','G1','G1','G2','G2','G3','G3','G4','G4','G5']
trash=[] # 쓰레기통 
deck=[] # 필드 덱 

hint=int(10) # 힌트 
life=int(3) # 목숨

random.shuffle(cards)

print(cards)  #확인용 
     
class GameManager:
    
    def giveCards(cards):
        p=cards[0:4]               #카드 배분
        del cards[0:4]
        return p

p1=GameManager.giveCards(cards)
print(p1)         #확인용 
print(cards)        
   
class PlayerBehavior:
   
    def tellCards(what,player):
        global hint
        if hint == 0:                       #hint 유무에 따라 
            print("You can't use hint")
            return
        else:
            hint -= 1
            for card in player:    
                if what in card:           #카드내의 문자, 숫자 찾기
                    print('%s is here' %what)
                else:
                    print('nothing')        
    
    def delCards(player,order,cards,trash):
        num=order-1
        delc=player[num]
        trash.append(delc)         # 카드 버리고 쓰레기 통에 추가 및 한장 뽑기
        del player[num]
        plus=cards[0]
        player.insert(num, plus)
        del cards[0]
      
    def putCards(player,order,cards,deck):
        num=order-1
        putc=player[num]
        deck.append(putc)          # 카드를 덱에 추가 및 한장 뽑기 
        del player[num]
        plus=cards[0]
        player.insert(num, plus)
        del cards[0]

PlayerBehavior.putCards(p1,1,cards,deck)
print(p1)   #확인용 

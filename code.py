from os import set_inheritable
import discord
from datetime import datetime
from random import *
import time
import openpyxl

client=discord.Client()

token="ODU3MDg4OTMwNjQ5NjA0MTA2.YNKgRQ.rl0_diHh8yJEu7ZhfKX_oVL2xiM"

@client.event
async def on_ready():
    print(client.user.name)
    print("성공적으로 봇이 시작됨")
    game=discord.Game("DM으로 Watermelon 보내보세요")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):

    
    
    if message.content.startswith("잉하"):
        await message.channel.send("안뇽")
    
    if message.content.startswith(">멍멍이"):
        doni=randint(1,4)
        if doni==1:
            await message.channel.send(file=discord.File('평범돈니.png'))
        elif doni==2:
            await message.channel.send(file=discord.File('바보돈니.png'))
        elif doni==3:
            await message.channel.send(file=discord.File('화난 돈니.png'))
        elif doni==4:
            await message.channel.send(file=discord.File('원본돈니.jpg'))
        


    if message.content.startswith(">우왁굳"):
        wak=randint(1,5)
        if wak==1:
            await message.channel.send(file=discord.File('1.gif'))
        elif wak==2:
            await message.channel.send(file=discord.File('2.gif'))
        elif wak==3:
            await message.channel.send(file=discord.File('3.png'))
        elif wak==4:
            await message.channel.send(file=discord.File('4.png'))
        elif wak==5:
            await message.channel.send(file=discord.File('5.png'))
    if message.content.startswith(">케인"):
        kinin=randint(1,7)
        if kinin==1:
            await message.channel.send(file=discord.File('케인 1.png'))
        elif kinin==2:
            await message.channel.send(file=discord.File('케인 2.png'))
        elif kinin==3:
            await message.channel.send(file=discord.File('케인 3.png'))
        elif kinin==4:
            await message.channel.send(file=discord.File('케인 4.png'))
        elif kinin==5:
            await message.channel.send(file=discord.File('케인 5.png'))
        elif kinin==6:
            await message.channel.send(file=discord.File('케인 6.png'))
        elif kinin==7:
            await message.channel.send(file=discord.File('케인 7.png'))
    
    if message.content.startswith(">초대"):
        await message.channel.send("https://discord.com/oauth2/authorize?client_id=857088930649604106&permissions=3533904&scope=bot")
    
    
        
    if message.content.startswith(">도배"):
        await message.channel.send(">도배 ㅋㅋㅋㅋ")

    if message.content.startswith(">뭐먹지"):
        a=randint(1,10)
        if a==1:
            await message.channel.send("짜장면")
        elif a==2:
            await message.channel.send("라면")
        elif a==3:
            await message.channel.send("쌀국수")
        elif a==4:
            await message.channel.send("햄버거")
        elif a==5:
            await message.channel.send("치킨")
        elif a==6:
            await message.channel.send("피자")
        elif a==7:
            await message.channel.send("김치찌개")        
        elif a==8:
            await message.channel.send("볶음밥")
        elif a==9:
            await message.channel.send("돈까스")
        elif a==10:
            await message.channel.send("느그혐 민트초코")
    
    
    
    if message.content.startswith(">미니게임 시작"):
        await message.channel.send("봇이 죽일지 살릴지 정합니다...")
        die=randint(1,2)
        time.sleep(1.3)
        if die==1:
            await message.channel.send("생존!")
        else:
            await message.channel.send("죽음")

    if message.content.startswith(">건의"):
        await message.channel.send("2ingbot9294@gmail.com 으로 건의 해주세요")
    
    if message.content.startswith(">도움말"):
        await message.channel.send("https://discord.gg/JnMeVsPUTH 서버의 도움말 채널을 참고해주세요!")

    if message.content.startswith(">타이머"):
        second=message.content.split(" ")[1]
        await message.channel.send("타이머 시작")
        
        for i in range(1,int(second)+1):
            await message.channel.send(i)
            time.sleep(1)

    if message.content.startswith(">앵무새"):
        copy=message.content.split(" ")[1]
        await message.channel.send(copy)

    if message.content.startswith(">명언"):
        talk=randint(1,11)

        if talk==1:
            await message.channel.send("제발 니인생에 훈수하세요")
            await message.channel.send("-우왁굳-")
        elif talk==2:
            await message.channel.send("겨울배가 달단다!")
            await message.channel.send("-케인-")
        elif talk==3:
            await message.channel.send("못생긴 #이 담배 피는것 만큼 꼴보기 싫은게 없어")
            await message.channel.send("-랄로-")
        elif talk==4:
            await message.channel.send("이말이 누군가에겐 상처가 될수 있잖아요")
            await message.channel.send("-랄로-")
        elif talk==5:
            await message.channel.send("알아서 잘 딱 깔끔하고 센스있게")
            await message.channel.send("-우왁굳-")
        elif talk==6:
            await message.channel.send("햄버거맛이 이상한게 아니라 햄버거집에 맨날오는 니가 이상한거다")
            await message.channel.send("-우왁굳-")
        elif talk==7:
            await message.channel.send("화성 갈끄니까~")
            await message.channel.send("-일론 머스크-")
        elif talk==8:
            await message.channel.send("시청자는 집단 정신분열증 환자들이다")
            await message.channel.send("-우왁굳-")
        elif talk==9:
            await message.channel.send("레게노")
            await message.channel.send("-우왁굳-")
        elif talk==10:
            await message.channel.send("아이고난!")
            await message.channel.send("-케인-")
        elif talk==11:
            await message.channel.send("뭉탱이로 있 다가 유리게숭 아이그냥")
            await message.channel.send("-케인-")

    if message.content.startswith(">유튜브"):
        yt=message.content.split(" ")[1]
        if yt=="눕스틱":
            await message.channel.send("https://www.youtube.com/channel/UCoyaWaRPYKDvsQhN6Zh6I7Q")
        elif yt=="이잉봇":
            await message.channel.send("https://www.youtube.com/channel/UC-NB7HSy2w_o0fUHixbVvGw")
        elif yt=="이잉":
            await message.channel.send("https://www.youtube.com/channel/UC-NB7HSy2w_o0fUHixbVvGw")
        elif yt=="블루자드":
            await message.channel.send("https://www.youtube.com/channel/UCN3Un8T8awA9MwxLoX5JyLQ")
        elif yt=="완깎귤":
            await message.channel.send("https://www.youtube.com/channel/UCeTKm1iAkgGj4lSQI7Oa9SA")



    if message.content=="무":
        await message.channel.send("야호")
    if message.content=="혹시 액션이 어떻게 되는지 아십니까?":
        await message.channel.send("무야호~")
    if message.content=="무한":
        await message.channel.send("무야호")
    if message.content=="무야호":
        await message.channel.send("그만큼 신나 신다는 거지")

    if message.content.startswith(">대화"):
        talking=randint(1,1000)
        if talking==438:
            await message.channel.send("대답은 해줄께 ㅋㅋㅋ")
        else:
            await message.channel.send("ㅇ")
        
    if message.content.startswith(">주사위"):
        dice=int(message.content.split(" ")[1])
        await message.channel.send("주사위를 굴립니다.....")
        dicenum=randint(1,6)
        if dicenum==1:
            time.sleep(1)
            await message.channel.send(file=discord.File('주사위1.png'))
            if dice==dicenum:
                await message.channel.send("성공!")
                time.sleep(0.5)
                await message.channel.send(file=discord.File('성공.gif'))
            else:
                await message.channel.send("실패")
        elif dicenum==2:
            time.sleep(1)
            await message.channel.send(file=discord.File('주사위2.png'))
            if dice==dicenum:
                await message.channel.send("성공!")
                time.sleep(0.5)
                await message.channel.send(file=discord.File('성공.gif'))
            else:
                await message.channel.send("실패")
        elif dicenum==3:
            time.sleep(1)
            await message.channel.send(file=discord.File('주사위3.png'))
            if dice==dicenum:
                await message.channel.send("성공!")
                time.sleep(0.5)
                await message.channel.send(file=discord.File('성공.gif'))
            else:
                await message.channel.send("실패")
        elif dicenum==4:
            time.sleep(1)
            await message.channel.send(file=discord.File('주사위4.png'))
            if dice==dicenum:
                await message.channel.send("성공!")
                time.sleep(0.5)
                await message.channel.send(file=discord.File('성공.gif'))
            else:
                await message.channel.send("실패")
        elif dicenum==5:
            time.sleep(1)
            await message.channel.send(file=discord.File('주사위5.png'))
            if dice==dicenum:
                await message.channel.send("성공!")
                time.sleep(0.5)
                await message.channel.send(file=discord.File('성공.gif'))
            else:
                await message.channel.send("실패")
        elif dicenum==6:
            time.sleep(1)
            await message.channel.send(file=discord.File('주사위6.png'))
            if dice==dicenum:
                await message.channel.send("성공!")
                time.sleep(0.5)
                await message.channel.send(file=discord.File('성공.gif'))
            else:
                await message.channel.send("실패")


    if message.content.startswith(">랄로"):
        jeayook=randint(1,10)
        if jeayook==1:
            await message.channel.send(file=discord.File('랄로1.png'))
        elif jeayook==2:
            await message.channel.send(file=discord.File('랄로2.png'))
        elif jeayook==3:
            await message.channel.send(file=discord.File('랄로3.png'))
        elif jeayook==4:
            await message.channel.send(file=discord.File('랄로4.png'))
        elif jeayook==5:
            await message.channel.send(file=discord.File('랄로5.jpg'))
        elif jeayook==6:
            await message.channel.send(file=discord.File('랄로6.png'))
        elif jeayook==7:
            await message.channel.send(file=discord.File('랄로7.jpg'))
        elif jeayook==8:
            await message.channel.send(file=discord.File('랄로8.jpg'))
        elif jeayook==9:
            await message.channel.send(file=discord.File('랄로9.jpg'))
        elif jeayook==10:
            await message.channel.send(file=discord.File('랄로10.png'))


    if message.content=="Watermelon":
        await message.channel.send(file=discord.File('낚시.png'))

    if message.content==">대화 이잉봇귀여워":
        await message.channel.send("인정ㅎㅎ")

    if message.content.startswith("이프"):
        await message.channel.send("나락가즈아 ㅈㅂ")
        
        
    if message.content.startswith(">뭉탱이"):
        await message.channel.send(file=discord.File('케인 2.png'))

    if message.content.startswith(">큐톤"):
        await message.channel.send("해충.")

    

    if message.content.startswith(">백업 이잉봇서버"):
        await message.channel.send("https://discord.new/ffSWt27bVbUH")
    if message.content.startswith(">백업 도움말"):
        await message.channel.send(file=discord.File('도움말.txt'))

    if message.content.startswith(">가위바위보"):
        rsp=message.content.split(" ")[1]
        randrsp=randint(1,3)

        if randrsp==1:
            await message.channel.send(file=discord.File('가위.jpg'))
            if rsp=="가위":
                await message.channel.send("비겼습니다")
            elif rsp=="바위":
                await message.channel.send("이겼습니다")
            elif rsp=="보":
                await message.channel.send("졌습니다")
            else:
                await message.channel.send("오류")
        if randrsp==2:
            await message.channel.send(file=discord.File('바위.png'))
            if rsp=="가위":
                await message.channel.send("졌습니다")
            elif rsp=="바위":
                await message.channel.send("비겼습니다")
            elif rsp=="보":
                await message.channel.send("이겼습니다")
            else:
                await message.channel.send("오류")
        if randrsp==3:
            await message.channel.send(file=discord.File('보.png'))
            if rsp=="가위":
                await message.channel.send("이겼습니다")
            elif rsp=="바위":
                await message.channel.send("졌습니다")
            elif rsp=="보":
                await message.channel.send("이겼습니다")
            else:
                await message.channel.send("오류")


                

    if message.content.startswith(">배너 1"):
        await message.channel.send("https://discord.gg/UBxdN7crxs")
        await message.channel.send("연합 1번째 서버인 cloud village")
    
    if message.content.startswith(">배너 2"):
        await message.channel.send("https://discord.gg/Zb4AWHhs")
        await message.channel.send("연합 2번째 서버인 눕스틱 왕국")
    
    

    if message.content==">":
        await message.channel.send("까먹음?")


    if message.content.startswith(">백업 블루자드"):
        await message.channel.send("블자는 악마다")
        await message.channel.send("모솔이다")
        await message.channel.send("천재가 아니다")
        await message.channel.send("운동 개못한다")
        await message.channel.send("인성질을 좋아한다")

    if message.content.startswith(">백업 완깎귤"):
        await message.channel.send("완깍귤이 주장한 데이터는 거짓말이기에 백업하지 않았습니다")

    if message.content.startswith(">서포트서버"):
        await message.channel.send("https://discord.com/invite/yWVBQyZcF8")

    if message.content.startswith(">현재시각"):
        now = datetime.now()
        await message.channel.send("현재시각:",now.year, "년", now.month, "월", now.day, "일", now.hour, "시", now.minute, "분", now.second, "초")

    if message.content.startswith(">생일"):
        await message.channel.send("2021년 6월 10일이에요!")
    if message.content.startswith(">앵무새 이잉봇병신"):
        await message.channel.send("니애미병신")
    if message.content.startswith(">부관리자"):
        await message.channel.send("https://forms.gle/cwP84vtVUcKVVkVE7")

    if message.content.startswith(">디자이너"):
        await message.channel.send("https://forms.gle/aJx99cZtAfKGsmXE8")

    iing=int(10000)
    nubstick=int(0)
    cloud=int(0)
    fnxm=int(0)
    vanGoah=int(0)
    goyounghee=int(0)
    landen=int(0)
    ngurad=int(0)
    desorry=int(0)
    DM=int(0)
    gyull=int(0)
    bluezard=int(0)
    akey=int(0)
    cokunut=int(0)
    zara=int(0)
    birdcham=int(0)

    if message.content.startswith(">출첵 이잉"):
        iing=iing+10
        await message.channel.send("10잉머니 충전 완료")
    if message.content.startswith(">출첵 오옹 나이스"):
        nubstick=nubstick+10
        await message.channel.send("10잉머니 충전 완료")
    if message.content.startswith(">출첵 클라우드"):
        cloud=cloud+10
        await message.channel.send("10잉머니 충전 완료")
    if message.content.startswith(">출첵 루트"):
        fnxm=fnxm+10
        await message.channel.send("10잉머니 충전 완료")
    if message.content.startswith(">출첵 반 고흐"):
        vanGoah=vanGoah+10
        await message.channel.send("10잉머니 충전 완료")
    if message.content.startswith(">출첵 고영희"):
        goyounghee=goyounghee+10
        await message.channel.send("10잉머니 충전 완료")
    if message.content.startswith(">출첵 랜든"):
        landen=landen+10
        await message.channel.send("10잉머니 충전 완료")
    if message.content.startswith(">출첵 엔가드"):
        ngurad=ngurad+10
        await message.channel.send("10잉머니 충전 완료")
    if message.content.startswith(">출첵 데소리"):
        desorry=desorry+10
        await message.channel.send("10잉머니 충전 완료")
    if message.content.startswith(">출첵 DM"):
        DM=DM+10
        await message.channel.send("10잉머니 충전 완료")
    if message.content.startswith(">출첵 완깎귤"):
        gyull=gyull+10
        await message.channel.send("10잉머니 충전 완료")
    if message.content.startswith(">출첵 블자"):
        bluezard=bluezard+10
        await message.channel.send("10잉머니 충전 완료")
    if message.content.startswith(">출첵 아키"):
        akey=akey+10
        await message.channel.send("10잉머니 충전 완료")
    if message.content.startswith(">출첵 코크넛"):
        cokunut=cokunut+10
        await message.channel.send("10잉머니 충전 완료")
    if message.content.startswith(">출첵 쿠쿸"):
        zara=zara+10
        await message.channel.send("10잉머니 충전 완료")
    if message.content.startswith(">출첵 힝힝"):
        birdcham=birdcham+10
        await message.channel.send("10잉머니 충전 완료")
    

    if message.content.startswith(">돈 이잉"):
        await message.channel.send(str(iing)+" 잉머니")
    if message.content.startswith(">돈 오옹 나이스"):
        await message.channel.send(str(nubstick)+" 잉머니")
    if message.content.startswith(">돈 클라우드"):
        await message.channel.send(str(cloud)+" 잉머니")
    if message.content.startswith(">돈 루트"):
        await message.channel.send(str(fnxm)+" 잉머니")
    if message.content.startswith(">돈 반 고흐"):
        await message.channel.send(str(vanGoah)+" 잉머니")
    if message.content.startswith(">돈 고영희"):
        await message.channel.send(str(goyounghee)+" 잉머니")
    if message.content.startswith(">돈 랜든"):
        await message.channel.send(str(landen)+" 잉머니")
    if message.content.startswith(">돈 엔가드"):
        await message.channel.send(str(ngurad)+" 잉머니")
    if message.content.startswith(">돈 데소리"):
        await message.channel.send(str(desorry)+" 잉머니")
    if message.content.startswith(">돈 DM"):
        await message.channel.send(str(DM)+" 잉머니")
    if message.content.startswith(">돈 완깎귤"):
        await message.channel.send(str(gyull)+" 잉머니")
    if message.content.startswith(">돈 블자"):
        await message.channel.send(str(bluezard)+" 잉머니")
    if message.content.startswith(">돈 아키"):
        await message.channel.send(str(akey)+" 잉머니")
    if message.content.startswith(">돈 코크넛"):
        await message.channel.send(str(cokunut)+" 잉머니")
    if message.content.startswith(">돈 쿠쿸"):
        await message.channel.send(str(zara)+" 잉머니")
    if message.content.startswith(">돈 힝힝"):
        await message.channel.send(str(birdcham)+" 잉머니")
    



    
    
    
    
    
    

    
client.run(token)

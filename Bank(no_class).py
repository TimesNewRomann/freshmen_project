import pandas as pd
import random


def command():
    print("--" * 30)
    command_num = input(
        "$$$ 은행 시스템입니다$$$\n-1번 : 유저 생성 \n-2번 : 유저 정보 확인 \n-3번 : 계좌전송(랜덤) \n-4번 : 유저 삭제 \n >> 원하는 서비스를 선택하십시오 : ")
    if command_num == "Exit" or command_num == "exit":
        print("시스템을 종료합니다.")
        exit()
    return command_num


path = '/home/seonwoo/Desktop/workspace/Banking_System_Algorithm'
user_df = pd.read_csv(
    path + '/user_csv', sep=',', encoding='cp949')
if user_df.empty == True:
    print("비어있음")
else:
    print(user_df)

while True:
    start = command()
    # command()  # 커멘드 입력
    if start == "1":  # 유저생성모드
        print("-" * 40)
        print("### 유저 생성 모드입니다 ###")
        name = input(" >> 성함을 입력해 주십시오 : ")  # 이름 입력
        if name == "Exit" or name == "exit":
            continue
        user_id = input(" >> 생성하실 ID를 입력해 주십시오 : ")  # 유저 아이디 입력
        if user_id == "Exit" or user_id == "exit":
            continue
        if len(user_id) >= 4 and user_id.isalnum() == True:  # 유저 아이디 조건
            good_id = user_id
        else:
            cnt = 1
            while True:  # 아이디 조건 조금더 손봐야함(조합)
                if len(user_id) >= 4 and user_id.isalnum() == True:
                    good_id = user_id
                    response = True
                    break
                if cnt == 3:
                    print("3회이상 잘못된 ID를 입력하였습니다. 유저 생성모드를 종료합니다.")
                    response = False
                    break
                elif user_id.isalnum() == False and len(user_id) < 4:
                    user_id = input(
                        " >> 아이디 형식에 적합하지 않으며 길이가 짧습니다. 다시 입력하여 주십시오 : ")
                    cnt += 1
                    if user_id == "Exit" or user_id == "exit":
                        response = False
                        break
                    continue
                elif len(user_id) < 4:
                    user_id = input(
                        " >> 아이디의 길이가 너무 짧습니다. 다시입력하여 주십시오(4자리 이상) : ")
                    cnt += 1
                    if user_id == "Exit" or user_id == "exit":
                        response = False
                        break
                    continue
                elif user_id.isalnum() == False:
                    user_id = input(
                        " >> 아이디 형식에 적합하지 않습니다. 다시 입력하여 주십시오(영어 및 숫자 조합) : ")
                    cnt += 1
                    if user_id == "Exit" or user_id == "exit":
                        response = False
                        break
                    continue
                continue
            if response == False:  # 이전 단계로 되돌아가기
                continue
            elif response == True:
                pass

        while True:
            passward = input(" >> 생성하실 비밀번호를 입력해 주십시오 : ")  # 비밀번호 입력
            if passward == "Exit" or passward == "exit":
                response = False
                break
            # 비밀번호 조건
            if len(passward) < 8 or passward.isdigit() == True or passward.isalpha() == True or passward.isalnum() == True or passward == passward.lower():
                print("잘못된 비밀번호 형식입니다.")
                continue
            else:
                good_pw = passward
                good_pw_agian = input(
                    " >> 비밀번호를 한번 더 입력해 주십시오 :  ")  # 비밀번호 재확인
                if good_pw_agian == good_pw:
                    response = True
                    break
                elif good_pw_agian == "Exit" or good_pw_agian == "exit":
                    response = False
                    continue
                else:
                    print("올바른 암호가 아닙니다. 비밀번호 초기설정으로 돌아갑니다.")
                    continue
        if response == False:  # 이전 단계로 되돌아가기
            continue
        elif response == True:
            pass

        num_list = []
        for i in range(8):
            num_list.append(random.randint(0, 9))
        account = "".join(map(str, num_list))
        seed = 100000
        user = {"Name": name, "ID": good_id,
                "PW": good_pw, "Account": account, "Balance": seed}

        user_df = pd.concat([user_df, pd.DataFrame(
            user, index=[0])], ignore_index=True)

        user_df.to_csv(path + '/user_csv',
                       index=False, encoding='cp949')  # 변경내용 저장

    elif start == "2":  # 유저 정보 확인 모드
        print("-" * 40)
        print("### 확인 모드입니다 ###")
        if user_df.empty == True:
            print("비어있음")
        else:
            print(user_df)
        continue

    elif start == "3":  # 계좌 송금 모드
        print("-" * 40)
        print("### 랜덤 계좌 송금 모드입니다 ###")
        balance = user_df.Balance.copy()  # user_df의 잔액열의 사본
        if user_df.empty:
            print("등록된 유저가 없습니다. 유저 생성모드에서 유저를 생성하십시오")
            continue
        elif len(user_df) == 1:
            print("유저는 자기 자신에게 송금할 수 없습니다. 유저를 추가로 생성하여 주십시오.")
            continue
        else:  # 송금 하는 경우
            c = 0
            while True:
                spend_index = random.randrange(0, len(balance))  # 보내는 랜덤 인덱스
                recieve_index = random.randrange(0, len(balance))  # 받는 랜덤 인덱스
                if spend_index == recieve_index:
                    continue
                else:
                    # 이동할 금액(임의로 1회 최대 10만원으로 설정)
                    money = random.randint(0, 100000)
                    if balance[spend_index] >= money:  # 송금할 금액이 잔액보다 작인 경우(실행)
                        # spend
                        balance[spend_index] = balance[spend_index] - money
                        # recieve
                        balance[recieve_index] = balance[recieve_index] + money
                        c += 1
                        # 개인별로 송금기록 저장
                        f = open(
                            f"{path}/{user_df.Name[spend_index]}.txt", "a+")
                        f.write(
                            f"{user_df.Name[recieve_index]}님에게 {money}원을 송금하였습니다.\n")
                        f.close()
                    elif balance[spend_index] < money:  # 잔액이 부족한 경우
                        if c < len(balance):
                            continue
                        else:
                            print(
                                f"{money - balance[spend_index]}원이 부족하여 송금을 종료합니다.")
                            break
                user_df.Balance = balance  # 다시 끼워넣기

            print(f"송금이 {c}번 진행되었습니다. ")
            user_df.to_csv(path + '/user_csv',
                           index=False, encoding='cp949')  # 변경내용 저장

    elif start == "4":  # 유저 삭제 모드
        print("-" * 40)
        print("### 유저 삭제 모드입니다 ###")
        del_id = input(" >> 삭제하실 유저의 ID를 입력하여 주십시오 : ")
        if del_id == "Exit" or del_id == "exit":
            continue
        else:
            if del_id in user_df.ID.tolist():
                del_pw = input(" >> 삭제하실 유저의 비밀번호를 입력하여 주십시오 : ")
                if del_pw == "Exit" or del_pw == "exit":
                    continue
                else:
                    if del_pw in user_df.PW.tolist():
                        del_index = user_df.ID.tolist().index(del_id)
                        user_df = user_df.drop(index=del_index, axis="rows").reset_index(
                            drop=True)
                        print("삭제되었습니다.")
                        user_df.to_csv(path + '/user_csv',
                                       index=False, encoding='cp949')  # 변경내용 저장
                        continue
                    else:
                        print("비밀번호가 일치하지 않습니다.")
                        continue
            else:
                print("입력하신 아이디는 존재하지 않는 아이디 입니다.")
                continue

    else:
        print("다시 입력하여 주십시오")
        continue

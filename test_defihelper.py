import pywaves as pw
import random
import requests
import time
import json
import ast

NODE_URL = "http://testnet-htz-nbg1-2.wavesnodes.com"

def dAppScript(dApp):
    script = open(dApp, "r").read()
    return script

def wait_for_resource_available(id, timeout):
    status_code = 0
    status = 0
    while status_code != 200:
        time.sleep(1)
        response = requests.get(NODE_URL + "/transactions/info/" + id)
        status_code = response.status_code
        try:
            status = json.loads(str(response.content.decode('utf8')))[
                "applicationStatus"]
        except:
            status = "NotFound"
    return status

governance_script = dAppScript("swop_governance.ride")
balance_script = dAppScript("balance.ride")
automate_script = dAppScript("automate.ride")
oracle_script = dAppScript("oracle.ride")

pw.setNode(node=NODE_URL, chain_id="T")

SWOP = "Ccgesc9iWMSg1f8CqFP5nZwgF6xsGirReDhpvNp1JAWW"

pw_SWOPmy = pw.Asset(SWOP)


moneySeed =  pw.Address(seed = "money seed for defihelper") # 3MvBuFJ8UaqdC8hmsZpZKm8xuiwnqBAKhB5

try_ = "28"

admin1 = pw.Address(seed = "admin1_" + try_)
admin2 = pw.Address(seed = "admin2_" + try_)
admin3 = pw.Address(seed = "admin3_" + try_)
admin4 = pw.Address(seed = "admin4_" + try_)
admin5 = pw.Address(seed = "admin5_" + try_)
user = pw.Address(seed = "user_" + try_)
govarnanceDapp = pw.Address(seed = "govarnanceDapp_" + try_)
balanceDapp = pw.Address(seed = "balanceDapp_" + try_)
automateDapp = pw.Address(seed = "automateDapp_" + try_)
oracleDapp = pw.Address(seed = "oracleDapp_" + try_)
SWOP_USDN_WAVES_pool = pw.Address(seed = "SWOP_USDN_WAVES_pool_" + try_)

# print("oracleDapp",oracleDapp,"\n")
# print("balanceDapp",balanceDapp,"\n")
# print("automateDapp",automateDapp,"\n")
# print("user",user,"\n")
# print("govarnanceDapp", govarnanceDapp,"\n")
# print("SWOP_USDN_WAVES_pool",SWOP_USDN_WAVES_pool,"\n")

# print("moneySeed", moneySeed,"\n")
# print("admin1", admin1,"\n")
# print("admin2", admin2,"\n")
# print("admin3", admin3,"\n")
# print("admin4", admin4,"\n")
# print("admin5", admin5,"\n")


# 0 _prepare_ 
## a) Увеличим инремент try_, если мы осуществляем прогон с нуля 
## b) !Укажем адрес oracle в automate и balance! Для этого принтанём адрес оракла 
## c) Создадим SWOP. После этого обновим перенную, заменим это поле в governance контракте
## 

# print("oracleDapp",oracleDapp,"\n")

# print(moneySeed.issueAsset(name = "SWOPmy",
#                                 description = "SWOPmy",
#                                 quantity = 100000000000000,
#                                 decimals = 8 ))


# 1 Инициализируем поля в оракле, раскатим скрипт. !Не забудем захардкодить оракла в балансе и автомейте!

# transfer = moneySeed.sendWaves(oracleDapp,int(10000000), txFee= 1400000)
# print(transfer,"\n")
# wait_for_resource_available(transfer["id"],1000)

# data = oracleDapp.dataTransaction([{
#         'type':'string', 
#         'key': 'balance_address', 
#         'value': balanceDapp.address
#         },
#         {
#         'type':'string', 
#         'key': 'swop_governance', 
#         'value': govarnanceDapp.address
#         },
#         {
#         'type':'string', 
#         'key': 'SWOP', 
#         'value': SWOP
#         },
#         {
#         'type':'string', 
#         'key': 'WAVES_USDN_pool', 
#         'value': SWOP_USDN_WAVES_pool.address
#         },
#         {
#         'type':'string', 
#         'key': 'consumers', 
#         'value': moneySeed.address + "," + admin1.address + "," + admin2.address + "," + admin3.address
#         },
#         {
#         'type':'string', 
#         'key': 'admin_1', 
#         'value': admin1.address
#         },
#         {
#         'type':'string', 
#         'key': 'admin_2', 
#         'value': admin2.address
#         },
#         {
#         'type':'string', 
#         'key': 'admin_3', 
#         'value': admin3.address
#         },
#         {
#         'type':'string', 
#         'key': 'admin_4', 
#         'value': admin4.address
#         },
#         {
#         'type':'string', 
#         'key': 'admin_5', 
#         'value': admin5.address
#         },
#         {
#         'type':'integer', 
#         'key': 'protocol_fee_in_usdn', 
#         'value': int(1e6)
#         },
#         {
#         'type':'boolean', 
#         'key': 'is_protocol_active', 
#         'value': True
#         }
#         ])
# print(data)
# wait_for_resource_available(data["id"],1000)

# setScript = oracleDapp.setScript(oracle_script,txFee=1400000)
# print(setScript,"\n")
# wait_for_resource_available(setScript["id"],1000)


# _2_
## Развернём swop governance контракт

# transfer = moneySeed.sendWaves(govarnanceDapp,int(100000000), txFee= 1400000)
# print(transfer,"\n")
# wait_for_resource_available(transfer["id"],1000)

# setScript = govarnanceDapp.setScript(governance_script,txFee=1400000)
# print(setScript,"\n")
# wait_for_resource_available(setScript["id"],1000)


# _3_
# ## Дадим пользователю вавесы и свопы 

# transfer = moneySeed.sendWaves(user,int(100000000), txFee= 1400000)
# print(transfer,"\n")
# wait_for_resource_available(transfer["id"],1000)

# transfer_SWOP = moneySeed.sendAsset(user, pw_SWOPmy, int(100000000))
# print(transfer_SWOP,"\n")
# wait_for_resource_available(transfer_SWOP["id"],1000)


# _4_
## Разворачивание balance контракта 

# transfer = moneySeed.sendWaves(balanceDapp,int(100000000), txFee= 1400000)
# print(transfer,"\n")
# wait_for_resource_available(transfer["id"],1000)

# setScript = balanceDapp.setScript(balance_script,txFee=1400000)
# print(setScript,"\n")
# wait_for_resource_available(setScript["id"],1000)

# initBalance = moneySeed.invokeScript(balanceDapp.address,
#                                     "init",
#                                     [],
#                                     [],
#                                     txFee=int(1e8*0.005)
#                                 )
# print(initBalance,"\n")
# wait_for_resource_available(initBalance["id"], 100)


# _5_
# # Пополним кошелёк от имени user и сразу спишем половину

# replanishBalance = user.invokeScript(balanceDapp.address,
#                                     "replenishBalance",
#                                     [{"type": "string", "value": user.address}],
#                                     [{"amount": int(10000000), "assetId": None }],
#                                     txFee=int(1e8*0.005)
#                                 )
# print(replanishBalance,"\n")
# wait_for_resource_available(replanishBalance["id"], 100)

# withdraw = user.invokeScript(balanceDapp.address,
#                                     "withdraw",
#                                     [{"type": "integer", "value": 5000000}],
#                                     [],
#                                     txFee=int(1e8*0.005)
#                                 )
# print(withdraw,"\n")
# wait_for_resource_available(withdraw["id"], 100)

# _6_
## Создадим псевдообменик, записав туда поля. Из них будем вычислять стоимость количество Waves, эквивалентного 1$

# transfer = moneySeed.sendWaves(SWOP_USDN_WAVES_pool,int(10000000), txFee= 1400000)
# print(transfer,"\n")
# wait_for_resource_available(transfer["id"],1000)

# data = SWOP_USDN_WAVES_pool.dataTransaction([{
#         'type':'integer', 
#         'key': 'B_asset_balance', 
#         'value': 5967062347309
#         },
#         {
#         'type':'integer', 
#         'key': 'A_asset_balance', 
#         'value': 20542289038095
#         }])
# wait_for_resource_available(data["id"],1000)
# print(data)

# _7_
## Развернём автомейт

# transfer = user.sendWaves(automateDapp,int(10000000), txFee= 1400000)
# print(transfer,"\n")
# wait_for_resource_available(transfer["id"],1000)

# data = automateDapp.dataTransaction([{
#         'type':'string', 
#         'key': 'owner', 
#         'value': user.address
#         },
#         {
#         'type':'boolean', 
#         'key': 'is_dapp_active', 
#         'value': True
#         }])
# wait_for_resource_available(data["id"],1000)
# print(data)

# setScript = automateDapp.setScript(automate_script,txFee=1400000)
# print(setScript,"\n")
# wait_for_resource_available(setScript["id"],1000)

# _8_
## Залочим SWOP через автомейт, получим инкам, рестейкнем от имени user

# lockSWOP = user.invokeScript(automateDapp.address, "governanceLockSWOP", [], [
#     {"amount": int(100000000), "assetId": SWOP }
#    ], txFee=int(1e8*0.005))
# print(lockSWOP,"\n")
# wait_for_resource_available(lockSWOP["id"], 100)

# airDrop = moneySeed.invokeScript(govarnanceDapp.address, "airDrop", [], [
#    {"amount": int(100000000), "assetId": SWOP }], txFee=int(1e8*0.005))
# print(airDrop,"\n")
# wait_for_resource_available(airDrop["id"], 100)

# claimAndStake = user.invokeScript(automateDapp.address, "governanceClaimAndStake", [{"type": "integer", "value": 100000000}], [], txFee=int(1e8*0.005))
# print(claimAndStake,"\n")
# wait_for_resource_available(claimAndStake["id"], 100)

# _9_
## Получим инкам, рестейкнем от имени defihelperManager

# airDrop = moneySeed.invokeScript(govarnanceDapp.address, "airDrop", [], [
#    {"amount": int(100000000), "assetId": SWOP }], txFee=int(1e8*0.005))
# print(airDrop,"\n")
# wait_for_resource_available(airDrop["id"], 100)

# claimAndStake = moneySeed.invokeScript(automateDapp.address, "governanceClaimAndStake", [{"type": "integer", "value": 100000000}], [], txFee=int(1e8*0.005))
# print(claimAndStake,"\n")
# wait_for_resource_available(claimAndStake["id"], 100)

# _10_
## Получим инкам, рестейкнем от имени defihelperManager. Убедимся, что не хватает срадеств

# airDrop = moneySeed.invokeScript(govarnanceDapp.address, "airDrop", [], [
#    {"amount": int(100000000), "assetId": SWOP }], txFee=int(1e8*0.005))
# print(airDrop,"\n")
# wait_for_resource_available(airDrop["id"], 100)

# claimAndStake = moneySeed.invokeScript(automateDapp.address, "governanceClaimAndStake", [{"type": "integer", "value": 100000000}], [], txFee=int(1e8*0.005))
# print(claimAndStake,"\n")
# wait_for_resource_available(claimAndStake["id"], 100)


# _11_
## defihelperManager выводит SWOP через автомейт. Убедимся, что он не имеет на это прав

# withdraw = moneySeed.invokeScript(automateDapp.address, "governanceWithdraw", [{"type": "integer", "value": 399999999}], [], txFee=int(1e8*0.005))
# print(withdraw,"\n")
# wait_for_resource_available(withdraw["id"], 100)


# _12_
## user выводит SWOP через автомейт

# withdraw = user.invokeScript(automateDapp.address, "governanceWithdraw", [{"type": "integer", "value": 299999999}], [], txFee=int(1e8*0.005))
# print(withdraw,"\n")
# wait_for_resource_available(withdraw["id"], 100)


# _13_
## Вывод дохода defihelper. Без одобрения транзакций админом. Убедимся, что тразнакция не отправляется

# incomeProtocolWithdraw = moneySeed.invokeScript(balanceDapp.address, "incomeProtocolWithdraw", [{"type": "string", "value": admin1.address}], [], txFee=int(1e8*0.005))
# print(incomeProtocolWithdraw,"\n")
# wait_for_resource_available(incomeProtocolWithdraw["id"], 100)

# _14_ 
# shutdown dApp

# shutdown = moneySeed.invokeScript(balanceDapp.address, "shutdownDapp", [], [], txFee=int(1e8*0.005))
# print(shutdown,"\n")
# wait_for_resource_available(shutdown["id"], 100)

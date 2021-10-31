# defi-helper-waves

automate.ride, balance.ride и oracle.ride -- dApp-ы defi-helper
swop_governance.ride -- обрезанный по функционалу контракт экоситсемы SWOP
test_defihelper.py -- файл, который позволяет в скриптовом стиле посмотреть бизнес логику и проверить работоспособность контратков

#### Общая информация
Все действия, требующие 2/3 подтверждений от админов, осуществляются через добавление в стейт аккаунта админов информации о транзакции
```
{
    'type':'boolean', 
    'key': _txid_ # ключ с id транзакции в base58
    'value': True
}
```

##### oracle.ride
В этотом контракте хранится все осоновные переменные
```
balance_address, type:string - base58 адрес balance контракта 
swop_governance, type:string - base58 адрес swop_governance контракта 
SWOP, type:string - base58 id токена SWOP 
WAVES_USDN_pool, type:string - base58 адрес контракта экосистемы SWOP
consumers, type:string - через запятую base58 адреса контрактов, обладающих правом взаимоедйтсвововать с автомейтами 
admin_1, type:string - base58 адрес админа
admin_2, type:string - base58 адрес админа
admin_3, type:string - base58 адрес админа
protocol_fee_in_usdn, type:integer - комиссия протокола в копейках USDN
is_protocol_active, type:boolean - если не true, методы контрактов экосистемы defi-helper
```
Пример можно увидеть в test_defihelper.py

##### balance.ride

Вызываемые методы:

- init() -- вызывается один раз. Создаёт запись для общего баланса и активирует  is_dapp_active == true
- updateAutomateStatus(automate: String, status: Boolean) -- добавление automate в whitelist. Необходимо, чтобы автомейт самостоятельно списывал комиссию с balance
- extractFee(user: String, isFeeExtract: Boolean) -- метод, вызываемый automate-ом, при списываении комиссии
- replenishBalance(userToReplenish: String) -- пополнение баланса в WAVES для userToReplenish
- withdraw(withdrawAmt: Int) -- вывод средств пользователем с баланса 
- incomeProtocolWithdraw(addresForSendingIncome : String) -- вывод дохода протокола. Требует 2/3 одобрения от админов
- shutdownDapp() -- остановка контракта. Доступно consumer, admins 
- @Verifier(tx) -- все отправляемые транзакции требут 2/3 одобрения от админов

##### automate.ride

Вызываемые методы:

- init() -- вызывается пользователем. Записывает в стейт адрес владельца и активирует  is_dapp_active == true
- governanceLockSWOP() -- принимает платёж в SWOP. Вызывает lockSWOP() на governance контракте экосистемы Swop
- governanceClaimAndStake(minSWOPreward: Int) -- Клейм и рестейк средств. Возможен вызов consumer и пользователем. При вызове от имени consumer взымается комиссия протокола  protocol_fee_in_usdn и 0.005 WAVES с баланса пользователя в balance
- governanceWithdraw(amtToWithdraw:Int) -- вывод SWOP из экоситсемы Swop. Доступно толко пользователю
- shutdownDapp() -- остановка контракта. Доступно consumer, admins и owner(пользователь)
- @Verifier(tx) -- все отправляемые транзакции требут 2/3 одобрения от админов


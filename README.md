# defi-helper-waves

automate.ride, balance.ride and oracle.ride — defi-helper dApp-s

swop_governance.ride — feature-reduced SWOP ecosystem contract

test_defihelper.py — script that allows glance at business logic and checks the functionality

#### General info
All actions requiring 3/5 confirmation from admins are performed by adding data about the transaction to the admins' account state
```
{
    'type':'boolean', 
    'key': _txid_ # key with base58 transaction id  
    'value': True
}
```

##### oracle.ride
This contract stores all the main variables
```
balance_address, type:string - base58 balance contract  
swop_governance, type:string - base58 swop_governance contract 
SWOP, type:string - base58 SWOP token id 
WAVES_USDN_pool, type:string - base58 SWOP ecosystem contract address
consumers, type:string - comma-separated base58 addresses that have the right to interact with automates
admin_1, type:string - base58 admin1
admin_2, type:string - base58 admin2
admin_3, type:string - base58 admin3
admin_4, type:string - base58 admin4
admin_5, type:string - base58 admin5
protocol_fee_in_usdn, type:integer - USDN protocol commission
is_protocol_active, type:boolean - if not true, defi-helper ecosystem contract methods are inactive
```
You can see an example in test_defihelper.py

##### balance.ride

Called methods:

- init() - сalled once. Creates an entry for total balance and activates is_dapp_active == true
- updateAutomateStatus(automate: String, status: Boolean) - adding automate to the whitelist. It is necessary for the automate to deduct the commission from the balance
- extractFee(user: String, isFeeExtract: Boolean) - method called by automate for debiting the commission
- replenishBalance(userToReplenish: String) - balance replenishment in WAVES for userToReplenish
- withdraw(withdrawAmt: Int) - user withdrawal from the balance  
- incomeProtocolWithdraw(addresForSendingIncome : String) - protocol income output. Requires 3/5 approval from admins
- shutdownDapp() - contract stop. Available for consumers and admins 
- @Verifier(tx) -  all transactions sent from contract require 3/5 approval from admins

##### automate.ride

Called methods:

- init() - called by user. Writes owner's address to the state and activates is_dapp_active == true
- governanceLockSWOP() - accepts payment in SWOP. Calls lockSWOP() on the Swop ecosystem contract
- governanceClaimAndStake(minSWOPreward: Int) - Claim and restake SWOP. It is possible to call for consumer and user. When calling  by consumer, protocol_fee_in_usdn and 0.005 WAVES are charged from user in balance dApp
- governanceWithdraw(amtToWithdraw:Int) - output SWOP from the Swop ecosystem. Available only to the user
- shutdownDapp() - contract stop. Available for consumer, admins and owner(user)
- @Verifier(tx) -  all transactions sent from contract require 3/5 approval from admins


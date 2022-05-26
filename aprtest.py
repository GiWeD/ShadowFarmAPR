PF = 5/100
SingleStake = 50/100

TVL = 1000
compoundTime = 365 #day --> once a day

singleBalance = list()
costantInflux = TVL*PF / compoundTime

for i in range(compoundTime):

    #first day deposit TVL, we harvest next day --> singleBalance = 0
    if (i==0):
        singleBalance.append(0)


    #else farm PF+Single and stake in singleStake
    else:
       
        # The total balance on the single farm is composed by:
        # - The costant Influx from the principal farm = Total Value Locked * PrincipalFarm APR / compound day
        # - The farmed token from the single staking, this is done using the balance at the previous epoch
        # - The balance staked at the previous epoch
        # eg.:  day0 -> Deposit 1000$.
        #       day1 -> Harvest PF (5% = 5$/CompoundTime) + SingleStake(day1 = 0$), Deposit harvest in single stake. Total Earn so far = 0.01369$
        #       day2 -> Harvest PF (5% = 5$/CompoundTime) + SingleStake( 5$/CompoundTime * SingleStakeAPR), Total Earn so far =  0.01369$(PF) + 0.01369$ (balance[i-1]) +  0.00685 $ (single stake farm) = 0.0342 $
        #       --------        
        singleFarmReturnsOfEpoch = singleBalance[i-1] * SingleStake / compoundTime
        singleBalance.append( (costantInflux + singleFarmReturnsOfEpoch + singleBalance[i-1])  ) 


# save the final Balance (our earnings)
finalBalance = singleBalance[-1]

# Im considering everything = 1$. In case the finalBalance is a token just do finalBalance*PriceOfToken 
annualPercentageReturn = (finalBalance / TVL) *100


## PRINT ##

## FINALBALANCE =   64.59025906560294
## APR          =   6.459025906560294 % [PF WAS 5%, SHADOWFARMS INCREASED BY ~29%]     
print(finalBalance)
print(annualPercentageReturn)

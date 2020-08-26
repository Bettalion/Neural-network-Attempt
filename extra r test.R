# creating training data set
Sys.setenv(LANG = "en")
TR=c(20,10,30,20,80,30)
TS=c(90,20,40,50,50,80)
GEN=c(1,0,0,0,1,1)
ATEN=c(1,0,0,0,1,1)
WEA=c(1,0,0,0,1,1)
# LOC=c(1,0,0,0,1,1) #not in test
FAMS=c(1,0,0,0,1,1)
ETH=c(1,0,0,0,1,1)
HQUAL=c(1,0,0,0,1,1)

Grade9=c(1,0,1,0,1,1)
# Here, you will combine multiple columns or features into a single set of data
df=data.frame(TR,TS,GEN,ATEN,WEA,FAMS,ETH,HQUAL,Grade9)

# load library
require(neuralnet)

# fit neural network
nn=neuralnet(Grade9~TR+TS+GEN+ATEN+WEA+FAMS+ETH+HQUAL,data=df, hidden=3,act.fct = "logistic",
                linear.output = FALSE)

# plot neural network
plot(nn)

# creating test set
TRs=c(20,10)
TSs=c(90,20)
GENs=c(1,0)
ATENs=c(1,0)
WEAs=c(1,0)
# LOCs=c(1,0,0,0,1,1) #not in test
FAMSs=c(1,0)
ETHs=c(1,0)
HQUALs=c(1,0)

Grade9s=c(1,0)
test=data.frame(TRs,TSs,SATSs,GENs,ATENs,WEAs,FAMSs,ETHs,HQUALs,Grade9s)

## Prediction using neural network
Predict=compute(nn,test)
Predict$net.result

# Converting probabilities into binary classes setting threshold level 0.5
prob <- Predict$net.result
pred <- ifelse(prob>0.5, 1, 0)
pred
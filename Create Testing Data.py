import random as r
import os

def populate(sample=10):
  maindir=os.getcwd()
  try:
    os.chdir(f'{maindir}/Testing data')
    log = open('DATA.txt','w')
  except:
      os.chdir(maindir)
      log = open('DATA.txt','w')
      print('Warning! Was not able to place DATA.txt in the Testing data folder')

  # used to attempt to make the probabilities more accurate
  atten= [1,1,1,2,2,3,4,5,1,1,1,2,3,1,1,1,2,2]
  Money= [1,2,2,3,3,3,3,3,3,3,3,4,4,4,5,1]
  fams=[2,2,2,2,3,3,3,3,3,3,3,4,4,5,2,4]
  race= [4,4,4,4,4,4,4,3,3,3,2,2,5,5,1,1]
  educ=[1,2,2,2,2,3,3,4,4,4,5,5,5,5,5,5,5,6,6,6,6]
  
  # populates the data file
  for x in range(sample):
    #time revising
    Rev=r.randint(0,10)
    #time socialising
    Scio = r.randint(0,10)
    while (Rev+Scio) >= 12: # to be logical (corect # of hours a day)
      if r.randint(0,1) == 0 and Rev >=1:
        Rev-=1
      elif Scio >=1:
        Scio-=1
    # decide gender
    if r.randint(0,100)%2 == 0: 
      Gen = 0 # male
    else:
      Gen = 1
    # attendance
    Aten = r.choice(atten)
    # wealth
    Wea=r.choice(Money)
    # num of family members
    fam = r.choice(fams)
    # ethnicity
    rac = r.choice(race)
    # Highest qualification in family
    edu=r.choice(educ)

    log.write(f'[{x}, {Rev}, {Scio}, {Gen}, {Aten}, {Wea}, {fam}, {rac}, {edu}, {r.randint(1,9)}]\n')
  log.close()
  os.chdir(maindir)

def sas(val,arr):
  arr.append(int(val))
  return arr

# collects data from file so it can be used in the program
def Collect(sample=10):
  maindir=os.getcwd()
  os.chdir(f'{maindir}/Testing data')
  
  f= open('DATA.txt','r')
  Rev=[]
  Sci=[]
  Gen=[]
  Ate=[]
  Wea=[]
  Fam=[]
  Rac=[]
  Edu=[]
  Grade=[]
  Cases=[]
  
  # takes data for data file and putts it into the array
  for _ in range(sample):
    person=f.readline().split('[')[1].split(']')[0]
    atributes= person.split(',')
    # print(atributes)

    Cases.append(atributes)

    Rev=sas(atributes[1],Rev)
    Sci=sas(atributes[2],Sci)
    Gen=sas(atributes[3],Gen)
    Ate=sas(atributes[4],Ate)
    Wea=sas(atributes[5],Wea)
    Fam=sas(atributes[6],Fam)
    Rac=sas(atributes[7],Rac)
    Edu=sas(atributes[8],Edu)
    Grades=sas(atributes[9],Grade)

  # for debuging purposes - to see each individual case as a table
  for case in Cases:
  #  print(case)
   pass

  # for debuging purposes - to see the value of the arrays at each stage
  # print(Rev,Sci,Gen,Ate,Wea,Fam,Rac,Edu,Grades)
  f.close()

  InputNodes,Grade=[Rev,Sci,Gen,Ate,Wea,Fam,Rac,Edu],Grades
  os.chdir(maindir)
  return [Cases,InputNodes,Grade]

# returns an array in the 'R' sytax so it can be writen into the script file
def CA(arr,ind,TL,name,before,GRADE=False):
  if before == True:
    if GRADE == False:
      x=str(arr[ind][:TL]).split('[')[1].split(']')[0]
    else:
      x=str(arr[:TL]).split('[')[1].split(']')[0]
  else:
    if GRADE == False:
      x=str(arr[ind][TL:]).split('[')[1].split(']')[0]
    else:
     x=str(arr[TL:]).split('[')[1].split(']')[0]
  rv = f'{name}=c({x})\n'
  return rv

# Uses the data to create the generic program
def CreateScript(Cases,InputNodes,grades):
  maindir=os.getcwd()
  # partioning 90% of data
  try:
   TL=0.9*len(Cases)
   TL=int(TL)
   print(len(Cases),TL)
   print(Cases[0],'\n',Cases)
  except:
    print(f'failed to get 90% of data as integer, total:{len(Cases[0])},TL:{TL}')
  try:
   os.chdir(f'{maindir}/Generic Neural Network Scripts')
   if os.path.exists('R Neural_Network.R') == False:
    f = open('R Neural_Network.R','w')
   else:
    naming = True
    count=1
    while naming ==True:
      if os.path.exists(f'R Neural_Network ({count}).R') == False:
        f = open(f'R Neural_Network ({count}).R','w')
        naming=False
      else:
        count+=1
   os.chdir(f'{maindir}/Testing data')
   if os.path.exists('Data R.txt') == False:
    fd = open('Data R.txt','w')
   else:
    naming = True
    count=1
    while naming ==True:
      if os.path.exists(f'Data R ({count}).txt') == False:
        fd = open(f'Data R ({count}).txt','w')
        naming=False
      else:
        count+=1
  except:
    os.chdir(f'{maindir}/Generic Neural Network Scripts')
    f=open('R Neural_Network.R','w')
    os.chdir(f'{maindir}/Testing data')
    fd=open('Data R.txt','w')

  # training data
  tr=CA(InputNodes,0,TL,'TR',True)
  ts=CA(InputNodes,1,TL,'TS',True)
  gen=CA(InputNodes,2,TL,'GEN',True)
  aten=CA(InputNodes,3,TL,'ATEN',True)
  wea=CA(InputNodes,4,TL,'WEA',True)
  fams=CA(InputNodes,5,TL,'FAMS',True)
  eth=CA(InputNodes,6,TL,'ETH',True)
  hqual=CA(InputNodes,7,TL,'HQUAL',True)

  G9=CA(grades,9,TL,'Grade9',True,True)

  ############
  # testing
  trs=CA(InputNodes,0,TL,'TRs',False)
  tss=CA(InputNodes,1,TL,'TSs',False)
  gens=CA(InputNodes,2,TL,'GENs',False)
  atens=CA(InputNodes,3,TL,'ATENs',False)
  weas=CA(InputNodes,4,TL,'WEAs',False)
  famss=CA(InputNodes,5,TL,'FAMSs',False)
  eths=CA(InputNodes,6,TL,'ETHs',False)
  hquals=CA(InputNodes,7,TL,'HQUALs',False)

  G9s=CA(grades,9,TL,'Grade9s',False,True)
  

  trainingString=f'{tr}{ts}{gen}{aten}{wea}{fams}{eth}{hqual}\n{G9}'
  testingString=f'{trs}{tss}{gens}{atens}{weas}{famss}{eths}{hquals}\n{G9s}'
  # Adding data to Neural_Network script
  os.chdir(f'{maindir}/Generic Neural Network Scripts')
  f.write(f'#Training Data\n{trainingString}\n#Testing Data\n{testingString}')
  # Adding data to a backup textfile - can be used as extra data
  os.chdir(f'{maindir}/Testing data')
  fd.write(f'#Training Data\n{trainingString}\n#Testing Data\n{testingString}')
  os.chdir(maindir)

def main():
  SampleS=10 # default - but can be used to hardcode the amount (comment out the input)
  try:
    # SampleS=int(input('Give the sample size required'))
    str(x)
  except:
    pass
  populate(SampleS)
  Cases,InputNodes,grades = Collect(SampleS)
  CreateScript(Cases,InputNodes,grades)


if __name__ == '__main__':
  masterdir=os.getcwd()
  main()
  os.chdir(masterdir)
 












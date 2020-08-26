import random as r
def populate(sample= 50):
  # try:
  #   log = open('DATA.txt','a')
  # except:
  log = open('DATA.txt','w')
  atten= [1,1,1,2,2,3,4,5,1,1,1,2,3,1,1,1,2,2]
  Money= [1,2,2,3,3,3,3,3,3,3,3,4,4,4,5,1]
  fams=[2,2,2,2,3,3,3,3,3,3,3,4,4,5,2,4]
  race= [4,4,4,4,4,4,4,3,3,3,2,2,5,5,1,1]
  educ=[1,2,2,2,2,3,3,4,4,4,5,5,5,5,5,5,5,6,6,6,6]
  
  for x in range(sample):
    Rev=r.randint(0,10)
    Scio = r.randint(0,10)
    while (Rev+Scio) >= 12: # to be logical
      if r.randint(0,1) == 0 and Rev >=1:
        Rev-=1
      elif Scio >=1:
        Scio-=1
    
    if r.randint(0,100)%2 == 0: 
      Gen = 0 # male
    else:
      Gen = 1
    Aten = r.choice(atten)
    Wea=r.choice(Money)
    fam = r.choice(fams)
    rac = r.choice(race)
    edu=r.choice(educ)
    log.write(f'[{x}, {Rev}, {Scio}, {Gen}, {Aten}, {Wea}, {fam}, {rac}, {edu}, {r.randint(1,9)}]\n')
  log.write('\n\n\n')
  log.close()
def sas(val,arr):
  arr.append(int(val))
  return arr
def Collect(sample=10):
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

  print(' ')
  for case in Cases:
   print(case)
  # print(1,Rev,Sci,Gen,Ate,Wea,Fam,Rac,Edu,Grades)
  f.close()
  InputNodes,Grade=[Rev,Sci,Gen,Ate,Wea,Fam,Rac,Edu],Grades
  # print(InputNodes,Grade)
  # return [InputNodes,Grade]
  return [Cases,InputNodes,Grade]

def CA(arr,ind,TL,name,GRADE=False):
  if GRADE == False:
    x=str(arr[ind][:TL]).split('[')[1].split(']')[0]
  else:
    x=str(arr[TL:]).split('[')[1].split(']')[0]
  rv = f'{name}=c({x})\n'
  return rv
def rdata(Cases,InputNodes,grades):
  total=len(Cases[0])
  try:
   TL=0.9*total
  #  print(total,TL,int(TL))
   TL=int(TL)
  except:
    print(f'failed to get 90% of data as integer, total:{total},TL:{TL}')
  try:
   f=open('Data R.R','a')
  except:
    f=open('Data R.R','w')

  # training data
  x=str(InputNodes[0][:TL]).split('[')[1].split(']')[0]
  tr=f'TR=c({x})\n'
  x=str(InputNodes[1][:TL]).split('[')[1].split(']')[0]
  ts=f'TS=c({x})\n'
  x=str(InputNodes[2][:TL]).split('[')[1].split(']')[0]
  gen=f'GEN=c({x})\n'
  x=str(InputNodes[3][:TL]).split('[')[1].split(']')[0]
  aten=f'ATEN=c({x})\n'
  x=str(InputNodes[4][:TL]).split('[')[1].split(']')[0]
  wea=f'WEA=c({x})\n'
  x=str(InputNodes[5][:TL]).split('[')[1].split(']')[0]
  fams=f'FAMS=c({x})\n'
  x=str(InputNodes[6][:TL]).split('[')[1].split(']')[0]
  eth=f'ETH=c({x})\n'
  x=str(InputNodes[7][:TL]).split('[')[1].split(']')[0]
  hqual=f'HQUAL=c({x})\n'

  x=str(grades[:TL]).split('[')[1].split(']')[0]
  G9=f'Grade9=c({x})\n'

  tr=CA(InputNodes,0,TL,'TR')
  ts=CA(InputNodes,1,TL,'TS')
  gen=CA(InputNodes,2,TL,'GEN')
  aten=CA(InputNodes,3,TL,'ATEN')
  wea=CA(InputNodes,4,TL,'WEA')
  fams=CA(InputNodes,5,TL,'FAMS')
  eth=CA(InputNodes,6,TL,'ETH')
  hqual=CA(InputNodes,7,TL,'HQUAL')

  G9=CA(grades,9,TL,'Grade9',True)

  ############
  # testing
  x=str(InputNodes[0][TL:]).split('[')[1].split(']')[0]
  trs=f'TRs=c({x})\n'
  x=str(InputNodes[1][TL:]).split('[')[1].split(']')[0]
  tss=f'TSs=c({x})\n'
  x=str(InputNodes[2][TL:]).split('[')[1].split(']')[0]
  gens=f'GENs=c({x})\n'
  x=str(InputNodes[3][TL:]).split('[')[1].split(']')[0]
  atens=f'ATENs=c({x})\n'
  x=str(InputNodes[4][TL:]).split('[')[1].split(']')[0]
  weas=f'WEAs=c({x})\n'
  x=str(InputNodes[5][TL:]).split('[')[1].split(']')[0]
  famss=f'FAMSs=c({x})\n'
  x=str(InputNodes[6][TL:]).split('[')[1].split(']')[0]
  eths=f'ETHs=c({x})\n'
  x=str(InputNodes[7][TL:]).split('[')[1].split(']')[0]
  hquals=f'HQUALs=c({x})\n'

  x=str(grades[TL:]).split('[')[1].split(']')[0]
  G9s=f'Grade9s=c({x})\n'

  trs=CA(InputNodes,0,TL,'TRs')
  tss=CA(InputNodes,1,TL,'TSs')
  gens=CA(InputNodes,2,TL,'GENs')
  atens=CA(InputNodes,3,TL,'ATENs')
  weas=CA(InputNodes,4,TL,'WEAs')
  famss=CA(InputNodes,5,TL,'FAMSs')
  eths=CA(InputNodes,6,TL,'ETHs')
  hquals=CA(InputNodes,7,TL,'HQUALs')

  G9s=CA(grades,9,TL,'Grade9s',True)
  
  
  trainingString=f'{tr}{ts}{gen}{aten}{wea}{fams}{eth}{hqual}\n{G9}'
  testingString=f'{trs}{tss}{gens}{atens}{weas}{famss}{eths}{hquals}\n{G9s}'
  f.write(f'#Training Data\n{trainingString}\n#Testing Data\n{testingString}')

def main():
  populate()
  Cases,InputNodes,grades = Collect()
  rdata(Cases,InputNodes,grades)

main()
 
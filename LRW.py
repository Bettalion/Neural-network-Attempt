# this is a single function that will find the approximate line of best fit from a curve
# assign data in format: 1) data = [[x1,y1], [x2,y2]...] or 2) x=[x1,x2,x3..] y=[y1,y2,y3..] data = [x,y]
def summer(x):
   sum = 0
   for value in x:
     sum+=int(value)
   return sum
def sortxy(data):
  x=[]
  y=[]
  for dataset in data:
    x.append(dataset[0])
    y.append(dataset[1])
  return [x,y]

def LinearRegression(data,MethodOfAssignment=1): ###
  if MethodOfAssignment == 1:
    x,y = sortxy(data)
  elif MethodOfAssignment == 2:
    x,y=data
  xsum=summer(x)
  ysum=summer(y)
  xpmean=xsum/len(x) #mean of xvalues
  ypmean=ysum/len(y) #mean of yvalues

  xbar = [] # x-meanx
  ybar = [] # y-meany
  xbar2 = [] # xbar ^2
  ybar2 = [] # ybar ^2
  xybar = []
  for i in range(len(x)):
    xbari = x[i]-xpmean
    ybari = y[i]-ypmean 
    xbar.append( xbari )
    ybar.append( ybari )

    xbar2.append( xbari**2 ) 
    ybar2.append( ybari**2 )

    xybar.append( xbari * ybari )
  
  xbar2sum = summer(xbar2)
  xybarsum = summer(xybar)

  m = xybarsum / xbar2sum

  c = ypmean - (m * xpmean)
  return [m,c] #grad, y-intercept
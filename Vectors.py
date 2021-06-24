firstVec = [2,3]
secondVec = [7,-1]
vecs = [firstVec[0],firstVec[1],secondVec[0],secondVec[1]] #x1,y1,x2,y2

import math

def calcDotProduct(x1,y1,x2,y2):
  return x1*x2+y1*y2

def calcMagnitude(x,y):
  return math.sqrt(x*x+y*y)

def calcAngleBetweenTwoVecs(x1,y1,x2,y2):
  vec1Mag = calcMagnitude(x1,y1)
  vec2Mag = calcMagnitude(x2,y2)
  dotProd = calcDotProduct(x1,y1,x2,y2)
  if vec1Mag * vec2Mag == 0:
    return (float)(0)
  return (math.acos(dotProd/(vec1Mag * vec2Mag))) * 180/math.pi

def convertToUnitVectorForm(x, y):
  return str(x) + "i + " + str(y) + "j"

def addVectors(x1,y1,x2,y2):
  arr = [x1+x2,y1+y2]
  return arr

def subtractVectors(x1,y1,x2,y2):
  arr = [x1-x2,y1-y2]
  return arr

def orthogonalParallel(x1,y1,x2,y2):
  if calcDotProduct(x1,y1,x2,y2) == 0:
    return "orthogonal"
  elif x1 > x2 and x1 % x2 == 0 and y1 % y2:
    return "parallel"
  elif x2 > x1 and x2 % x1 == 0 and y2 % y1:
    return "parallel"
  elif x2 == x1 and y2 == y1:
    return "parallel"
  else:
    return "neither parallel nor orthogonal"

def calcAngle(x,y):
  if x == 0:
    return (float)(90)
  return math.atan(y/x) * 180/math.pi

def toPolarForm(x,y):
  return [calcMagnitude(x,y), calcAngle(x,y)]

def oppositeVectors(x1,y1,x2,y2):
  if calcMagnitude(x1,y1) == calcMagnitude(x2,y2) and calcAngleBetweenTwoVecs(x1,y1,x2,y2) == 180:
    return True
  return False

def unitVector(x,y):
  mag = calcMagnitude(x,y)
  if (mag == 0):
    return[0,0]
  return[x/mag,y/mag]

print("Angle between the two vectors is: " + str(calcAngleBetweenTwoVecs(vecs[0],vecs[1],vecs[2],vecs[3]))) 
print("Dot product between the two vectors is: " + str(calcDotProduct(vecs[0],vecs[1],vecs[2],vecs[3])))
print("Unit vector form of the two vectors is: " + str(convertToUnitVectorForm(firstVec[0],firstVec[1])))
print("Two vectors added becomes: " + str(addVectors(vecs[0],vecs[1],vecs[2],vecs[3])))
print("Two vectors subtracted becomes: " + str(subtractVectors(vecs[0],vecs[1],vecs[2],vecs[3])))
print("Vectors are " + str(orthogonalParallel(vecs[0],vecs[1],vecs[2],vecs[3])))
print("Magnitude of the first vector is: " + str(calcMagnitude(vecs[0],vecs[1])))
print("Magnitude of the second vector is: " + str(calcMagnitude(vecs[2],vecs[3])))
print("Polar form of vec 1 is: " + str(toPolarForm(vecs[0],vecs[1])))
print("Polar form of vec 2 is: " + str(toPolarForm(vecs[2],vecs[3])))
print("The two vectors are opposite vectors: " + str(oppositeVectors(vecs[0],vecs[1],vecs[2],vecs[3])))
print("Unit vector of vec 1 is " + str(unitVector(vecs[0],vecs[1])))
print("Unit vector of vec 2 is " + str(unitVector(vecs[2],vecs[3])))

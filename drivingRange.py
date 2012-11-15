def positiveInput(swingPercent):
	input=false
	while input== false:
		swingPercent= int(input("Enter your swing force: 0 to 100: "))
		input=swingPercent
		if input < 0:
			print("Swing percent must be positive: ")
			input=false
		elif input > 100:
			print("Sorry 100 percent is the max ")
			input=false
		#end if
	#end while
#end def

def clubSelection():
	print(" Make your club selection by entering the number with the club you want ")
	print(" the pitch determines the hight of the ball ")
	clubType=true
	while clubType != true:
		
		print("1. 3 iron has a pitch of 20 degrees: ")
		print("2. 5 iron has a pitch of 40 degrees ")
		print("3. 7 iron has a pitch of 60 degrees ")
		print("4. 9 iron has a pitch of 80 degrees ")
		clubType= int(input(" 1, 2, 3, or 4 "))
		
		if clubType== 1:
			elevationInDegrees= 20
		elif clubType== 2:
			elevationInDegrees= 40
		elif clubType== 3:
			elevationInDegrees= 60
			
		elif clubType== 4:
			elevationInDegrees= 80
		else:
			clubType=false
			print("Please make a valid club selection: ")
		#end if
		clubType=elevationInDegrees
		
		return elevationInDegrees
	#end while
#end def

def distanceBetween(elevationInDegrees, swingForce):
	gravity= 32.172
	feetPerMile= 5280
	secsPerHour= 3600
	pi= 3.14159
	
	elevationInRadians= elevationInDegrees * pi / 180
	
	velocityInSecs= swingForce * feetPerMile / secsPerHour
	
	horizontalDistance= velocityInSecs**2 * sin(2 * elevationInRadians) / gravity
	
	return horizontalDistance
#end def

gongHits=0
swings=0
swingDistance=0
import random
import math

swingAgain= "Y"
while swingAgain== "Y":
	clubSelection()
	
	swingPercent= positiveInput() 
	swingForce= 150 * swingPercent / 100
	swings+1
	
	swingDistance = distanceTraveled()
	
	gongDistance= random.randint(1, 1000)
	
	print("You hit the ball: ", swingDistance, " feet")
	
	bong = abs(swingDistance - gongDistance)
	
	if bong <= 10:
		print("BONG! ")
		print("Thats a hit! ")
		gongDistance= random.randrange(1001)
		print("Your new distance is: ", gongDistance, " feet away ")
		gongHits+1
	else:
		print("Give it another shot! ")
		print("You are still: ", gongDistance, " feet away ")
	#end if
	
	swingAgain= input("Would you like to swing again: ")
#end while
print("You hit the ball: ", swings, " times")
print("You hit the gong: ", gongHits, " times")
print("nice job come again! ")



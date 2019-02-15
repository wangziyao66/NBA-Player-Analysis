import matplotlib.pyplot as plt 

def playerAndScores():
    file = open("player_database.txt")
    playerName = file.readline()
    
    info = []
    info.append(playerName)
    
    numGames = 5

    for g in range(0,numGames):
        playtime = 0
        score = 0
        rebounds= 0
        assists = 0
        steals = 0
        performance_rating = 0
        
        playtime = int(file.readline())
        score = int(file.readline())
        rebounds= int(file.readline())
        assists = int(file.readline())
        steals = int(file.readline())
        
        performance_rating += (playtime/48)*20 + (score/50)*25
        performance_rating += (rebounds/8)*25 + (assists/8)*15
        performance_rating += (steals/3)*15
        
        info.append(performance_rating)
            
    return info

# x axis values 
# x = [1,2,3,4,5,6] 
# corresponding y axis values 
# y = [2,4,1,5,2,6] 
    
stats = playerAndScores()
name = stats[0]

# The numbers for our games
x = [1,2,3,4,5]  

# The y axis should be the performance ratings for the player
y = []
 
 # Adds all the performance ratings, not including player name
for i in range(1,len(stats)):
     y.append( stats[i] )

# plotting the points  
plt.plot(x, y, color='orange', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=12) 
  
# setting x and y axis range 
plt.ylim(1,100) 
plt.xlim(1,10) 
  
# naming the x axis 
plt.xlabel('Game Number') 
# naming the y axis 
plt.ylabel('Performance Rating') 
  
# giving a title to my graph 
plt.title('NBA Los Angeles Lakers Performance Over Season') 
  
# function to show the plot 
plt.show() 
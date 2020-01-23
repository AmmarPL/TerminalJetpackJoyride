JetpackJoyride: Save Baby Yoda
===================
*Coded by:*
**Ammar Ahmed**

About The Game
-------------

>Baby Yoda has been kidnapped by the evil dragon 'Drakon'. Save him by killing the bad dragon.
----------


Rules of the Game
-------------------

#### Aim:
> - You have a hero whom you can control and you have to cross the obstacles and reach the boss to defeat him
#### Hero:
> - You have 5 lives
> - You loose a life on colliding with the obstacle
> - You loose a life on getting hit by dragonballs
> - You loose the game if the time gets over
#### Boss:
> - The boss has 50 lives
#### Shield:
> - There is a shield which can be used for 10 seconds in the game. once you use it you can only use it after 60 secs
#### Score:
> - Collect coins to increse your score +1
------------------------
#### Controls:
- A and D for horizontal movement
- W to actvate jetpack
- P to toggle the speed of the game (can be used only 6 times)
- K to activate shield
- Space bar to shoot bullets 
------------------------

Description of Classes and important variables Created
--------------------------------------------
#### Board:
The board array (numpy) which contains the entire game. It is a 45*width_of_the_scree matrix. Board has the main while true loop of the game
#### Beams:
Beam like structures appear as obstacles. There
are three kinds of beams: horizontal, vertical and some at 45 ◦ with the ground/platform. The
hero must ensure to not collide with these beams, else he will lose a life. He can use his
blaster to shoot at them and clear his way.
#### Magnet:
A magnet appears on the way, which will influence the motion of the
hero. So if he is in the range of the magnet, he would be continuously attracted towards
the magnet.
#### Boss:
The boss enemy must appear in the end.The boss enemy a flying dragon that adjusts its
position according to the player. It throws ice balls aimed at the hero, which he must dodge.
#### Bullets and SnowBalls:
These are the weapons of the hero and the dragon respectivly.
__________________

___________________

Reqiurements:
--------------------
- Python3 with the following modules installed
1) numpy
2) colorama

For Linux:
```
sudo apt-get update
sudo apt-get install python3
```

------------
Files
--------------
```
.
+-- alarmexception.py
+-- dragon.txt  
+-- obstacles.py
+-- dragon.py
+-- mandalorian.py
+-- coin.py
+-- game.py
+-- space.py
+-- getChUnix.py
+-- Readme.md
```










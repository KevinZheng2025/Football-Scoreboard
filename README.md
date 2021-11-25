# Football-Scoreboard
Scoreboard that is built on python3.9 and has a live display so you can bring it into your live streaming software like OBS.

Set up program from live streaming in OBS

Step 1: Download the FootballScoreboard.pyw file

Step 2: If you're on Windows install python 3.9 either from https://www.python.org/downloads/ or the microsoft store. Macs will have Python installed already

Step 3: Run the FootballScoreboard.pyw file

Step 4: Open OBS and in the scene you want to add the scoreboard in click the "+" icon under the Scources tab NOT THE SCENE TAB and select window capture

Step 5: A properties window should pop up and in the window option select the Scoreboard Program also make sure to uncheck the Capture Curser option 
          so when your mouse hovers over the scoreboard it does not show up on the broadcast. After that is done click the OK button

Step 6: You should now see the entire program being shown in OBS to just display the Scoreboard you will need to crop out some od the edges.
          To do that right click on the Windows capture Source and click Filter. Click the "+" button at the bottom left of the filter window and select crop.
          crop it at Left=200, Top=11, Right=204, Bottom=179

Step 7: You can now close out of the filter window and adjust the position of your scoreboard.

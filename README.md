# Wordle-Solver
This is a quickly made script to play the game of wordle.
The script supports using any number of characters for the word,
unlike the original game. But naturally the words that the program knows of,
are based from the included dataset. 

The included dataset is based on the word counts from wikipedia. 
Specifically from the project by https://github.com/IlyaSemenov/wikipedia-word-frequency
While this dataset can be used in its entireity I preferred to filter it. 

The way the dataset is filtered is so that any words that have a frequency<50 
were deleted. This was done to filter off any needlessly rare words or typos and also save on space.

The script was made only as a proof of concept and thus is not designed to be used 
for any serious projects, however one is permitted to modify the code as needed based 
on the license included. 

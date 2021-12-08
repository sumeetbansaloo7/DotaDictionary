# DotaDictionary

Dota 2 is a multiplayer online battle arena video game developed and published by Valve. The game is a sequel to Defense of the Ancients, which was a community-created mod for Blizzard Entertainment's Warcraft III: Reign of Chaos.


This project uses FastAPI web framework to fetch data from MongoDB to provide all stats and details related to all 122 Heroes in the game.


The main goal of this project was to recreate the functanality of old DOTA 2 hero pick screen.

In previous versions of the game players were allowed to filter heroes based on roles and complexity.

This feature was removed with new updates, to re-create the feature I first scrapped web for all hero details such as roles, attributes and complexity and created a databse for it, after which I imported data onto Mongo DB. To fetch and use data in up-coming projects I created FastAPI endpoints.

This API is currently hosted and can be viewd at https://vast-spire-84220.herokuapp.com/docs

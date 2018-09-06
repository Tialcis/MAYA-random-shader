# MAYA-random-shader

A maya plugin used to randomly assign shaders. Will support adjusting distribution of colors

## Usage 

Load the script into your scripts folder
In script panel, import shaderUI and instantiate
Use showUI() function on instance
Make selection of objects and click object select button
Make selection of shaders and click shader select button
Click randomize button!
Optional: Click distribute rainbow normally button ('RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'INDIGO' and 'VIOLET' shaders automatically generated if not already present)

## Abstract

I first got the idea to work on this project after seeing a much more complex subject presented at SIGGRAPH about generating the shaders as well (a super fascinating read which I wish I understood better which can be found here https://users.cg.tuwien.ac.at/zsolnai/gfx/gaussian-material-synthesis/). I ended up then settling a much smaller scope project which allowed me to develop off ideas and really test my ability to apply materials learned from Udemy course Python for Maya: Artist Friendly Programming by Dhruv Govil and the book Practical Maya Programming with Python by Robert Galanakis.

Adapted from https://www.highend3d.com/maya/script/random-shader-assign-to-objects-for-maya for Maya 2017 and thanks to Isaac Jiffar for help with the stats for the normal distribution work

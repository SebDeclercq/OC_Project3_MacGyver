# README

## PRESENTATION

This game is the result of my training as an Application Developer ([more info][DApython]).

This project is intended as a escape game : MacGyver (sic) has to collect three tools (a syringe, a needle and an ether bottle) and put to sleep the vilain Guardian blocking the labyrinth's exit.

## INSTALLATION

To install the game, you have to :

1. Download the game from Github (either by cloning it or by downloading the zip file attached)
2. Launch a virtual environment (venv) for python 3
3. Install the required modules with `pip install -r requirements.txt`

## CONFIGURATION AND GAMING

The configuration file is `app/Config.py`. There's some variables you can change to adapt the game to your desire, yet the most importants are :
- `PATH_MODEL_FILE` :  the path to the model file describing the labyrinth (see below)
- `BOARDGAME_WIDTH` : the width of the boardgame/labyrinth
- `BOARDGAME_HEIGHT` : its height
- `USER_INTERFACE` : the type of game you wish to play (either `text` (which I don't recommand), `prompt` (console only) or `GUI` (graphical))

The defaults parameters link to a model file available in the `models` subdirectory.

If you wish to add a new labyrinth, feel free to write it up as the model, in an Excel or a text file, and change the configuration to use it.

To launch the game, just execute the `app.py` within your venv and you're set !

### LICENSE

The credits of the used icons within this game (all of them are available for use and modification in a non-commercial project) are :
- Ether bottle: [pngimg][ether]
- Needle : [pngimg][needle]
- Syringe : [wikimedia][syringe]
- Wall : [wikimedia][wall]
- Everything else : [Jesse Freeman][jessefreeman]

**Permission is granted to copy, modify and/or distribute this work and/or license, without conditions except those ruled out by the icons cited above.**


[DApython]: https://openclassrooms.com/fr/paths/68-developpeur-dapplication-python
[ether]: http://pngimg.com/uploads/poison/poison_PNG45.png
[needle]: http://pngimg.com/uploads/sewing_needle/sewing_needle_PNG19094.png
[syringe]: https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Filled_Syringe_icon.svg/128px-Filled_Syringe_icon.svg.png
[wall]: https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Brick_wall_old.jpg/463px-Brick_wall_old.jpg
[jessefreeman]: https://www.jessefreeman.com

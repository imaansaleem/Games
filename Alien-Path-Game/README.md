# Alien-Path-Game
This Folder contains the source code of the console-based Alien Path game in which Players must carefully plan their moves and utilize the unique abilities of each Alien hero to overcome challenges.

## 6.1. Overview of Alien vs. Zombie

Alien vs Zombie is a turn-based combat game in which the player controls Alien to defeat a group of Zombies. Prior to the game, the player can customize settings including game board dimensions and number of zombies. The player can also save a game into a file and load a game from a file.

## 6.2. Game Board

The game is played on a two-dimensional board that contains game characters and objects. No characters or objects can be placed outside the board. The dimensions of the game board must be odd numbers so that the Alien can be placed at the centre of the game board. For a game board with 10 or more rows or columns, ensure that the row and column numbers are displayed correctly.

## 6.3. Game Characters

### 6.3.1. Attributes

Alien and Zombie are game characters. They share two common attributes: life and attack. A character is defeated when its life becomes zero. The attack indicates the damage a character inflicts on its opponent’s life in one hit. Unlike Alien, Zombie has the range attribute, which defines how far Zombie’s attack can reach.

Before the game begins, all attributes of Alien and Zombie are initialized with a random number. The only exception is the Alien’s attack which always starts from ZERO (0) at each turn. This is because Alien’s attack is accumulated by collecting the Arrow objects on the game board and is reset after each turn.

### 6.3.2. Movement and Attack

Both Alien and Zombie can move and attack, but their behaviors differ. Alien moves by continuously thrusting in one of the FOUR (4) directions (i.e., up, down, left, or right). It is stopped by one of the following events:
1. It hits the border of the game board (see Game Board).
2. It hits the Rock object (see Game Objects).
3. It hits and attacks Zombie, but Zombie survives the attack.

When Alien moves, it leaves trails on its path. At the end of Alien’s turn, the trails must be reset with random non-trail game objects before the Zombie’s turn begins. Alien attacks when it encounters Zombie on the move. If Zombie is defeated by the attack, Zombie will be removed from the game board while Alien continues to move.

Unlike Alien, Zombie performs both move and attack successively at each turn. However, Zombie can only move one step in a randomly selected direction (i.e., up, down, left, or right). Zombie can only move to a location not occupied by Alien. After a move, Zombie will attack Alien if Alien is within its attack range.

Both characters cannot move outside the board. When Alien hits a border of the board, it stops, and its turn ends. Zombie must also be programmed to avoid moving outside the board.

### 6.3.3. Multiple Zombies

Each zombie is represented by a unique digit character on the game board, starting from 1 to N, where N is the number of zombies specified by the player. The digit ZERO (0) is not used; hence the game can only support a maximum of NINE (9) zombies.

Each zombie must have different values for its attributes (i.e., life, attack, and range) which are generated randomly. You are free to decide the maximum and minimum limits of these attributes, but ensure that the limits are sensible.

Zombie cannot move to locations occupied by other zombies. When Alien finds a pod, the attack must target only ONE (1) zombie closest to the pod. If there are two or more zombies closest to the pod, choose any one of them at random. For defeated zombies, the game should skip their turns, but their attributes must remain displayed throughout the game.

### 6.4. Game Objects
Apart from the game characters, the game board also contains game objects that Alien can interact 
with. Here are the game objects:

| Name         | Appearance | Description                                              |
|--------------|------------|----------------------------------------------------------|
| Arrow        | ^ (up),    | Changes Alien’s direction of movement.                 |
|              | v (down),  | Adds 20 attack to Alien.                               |
|              | < (left),  |                                                        |
|              | > (right)  |                                                        |
| Health       | h          | Adds 20 life to Alien.                                 |
| Pod          | p          | Instantly inflicts 10 damage to Zombie when hit by Alien|
| Rock         | r          | Hides a game object (except Rock and Trail) beneath it.|
|              |            | Reveals the hidden game object when hit by Alien.     |
|              |            | Stops Alien from moving.                               |
| Empty Space  |            | Just an empty space on the board.                      |
| Trail        | .          | Left by Alien when it moves.                           |
|              |            | Reset to a random game object (except Trail) after Alien’s turn ends. |

### 6.5. Game Controls
The player plays the game by typing commands. The following shows the commands:

| Command | Description                                                |
|---------|------------------------------------------------------------|
| up      | Alien to move up.                                         |
| down    | Alien to move down.                                       |
| left    | Alien to move left.                                       |
| right   | Alien to move right.                                      |
| arrow   | Switch the direction of an arrow object in the game board. |
|         | (The player will be asked to enter the row and column of the arrow object to switch, followed by the direction of the arrow object to switch to.) |
| help    | List and describe the commands that the player can use in the game. |
| save    | Save the current game to a file.                          |
|         | (The player will be asked to enter the name of the file to save to.) |
| load    | Load a saved game from a file.                            |
|         | (The player will be asked to enter the name of the file to load from.) |
| quit    | Quit the game while still in play.                       |
|         | (The player will be asked to confirm his/her decision.)  |


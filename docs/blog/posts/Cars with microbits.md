---
draft: true
date: 2025-03-31
categories:
  - Project
  - Python
  - MicroPython
  - Electronique
authors:
  - mathiol
  - mathchameleon
---
## The idea
For the competition `Yes We Code` MathChameleon and I first thought to make a drone with the microbits but to avoid breaking any board we've switched to making a car. So to build our car, we need two microbits, one on the car itself and another to serve as the controller.
We are going to use the radio module of the microbit to communicate between the two boards. All the code used in this project is available at [GITHUB LINK HERE].  

### Quick explanation of the project difficulties
So, we need to send value of a potentiometer linked to the controller microbit to control the speed of the motors on the car. We also need to send custom value to command the car, for example when `A` is pressed the car's motors turns on and when `A` is released they turn off. An analogue stick need to be used to control direction or use the gyroscope of the board.

## First experiences with the microbit
...

## Our work
### Controller
>By Mathiol

#### Actions sheet
In this table, you will find each action the controller need to have, physical interface with the user and an explanation of the action. 

| Action                   | Physical Interface                  | Explanation                                                                                        |
| ------------------------ | ----------------------------------- | -------------------------------------------------------------------------------------------------- |
| Accelerate               | `A` button                          | When the `A` button is pressed, the motors need to turn on while when released, to turn motors off |
| Reverse motors direction | `B` button                          | When `B` is pressed we set a flag on/off to change motors rotating direction                       |
| Control Speed            | Potentiometer                       | Potentiometer linked to the board, intensity change the motors speed                               |
| Change direction         | On board gyroscope / Analogue stick | Allow to turn left or right                                                                        |
| Pause everything*        | `Touche` button                     | Pause everything except the radio until the button is pressed again                                |
| Turn on headlight*       | Separate button                     | Turn on / off the headlight on the car                                                             |
| Initialize controller**  | Seperate button                     | Setup on board gyroscope and reset radio settings, verify connection with car                      |
> \*: Special action
> \*\*: No radio output
#### Data formatting
All the data need to be transferred by radio with the minimal delay and no confusion, data will be structured in a custom binary format to allow easy decoding and be error safe.
There is two packet type, the classic one, sent each time a value changed and the specialized, a packet sent when a special button is pressed.

##### Classic
Packet sent every time a value change, ordered from first to last.

| Name       | Type   | Encoding size | Range      |
| ---------- | ------ | ------------- | ---------- |
| Accelerate | `bool` | 1 byte        | 0/1        |
| Reverse    | `bool` | 1 byte        | 0/1        |
| Direction  | `int`  | 8 bytes       | 0 <-> 255  |
| Speed      | `int`  | 12 bytes      | 0 <-> 1023 |
##### Special
Packet sent if a special action is activated. The header tells the car that this packet is special and he need to read the next 2 bytes as a special code.

| Name           | Type  | Encoding size |
| -------------- | ----- | ------------- |
| *Header*       | `int` | 4 bytes       |
| Special Action | `int` | 2 bytes       |


### Car
>By MathChameleon

## Material and documentation used
>If you're curious of what we've used to build this project or want more technical explanation  
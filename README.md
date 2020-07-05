# RiskBlitz

Risk board game Blitz dice program that resembles the operation of the phone app.

## How it works
The program takes 2 arguments:
1. Number of attacking troops
2. Number of defending troops

The maximum available troops will be used for each battle (i.e. up to 3 for attack, and up to 2 for defence), and the battles will continue until one side has 0 troops left.

The program will output the winner, how many troops remain on the winning side, and how many troops were lost on each side.

## How to run
```
./blitz.py num_attack num_defend
```
or
```
python3 blitz.py num_attack num_defend
```

#### Example:
```
> ./blitz.py 20 10

Attacking army wins after 8 rolls, with 17 troops remaining.
Casualties:
Attack: 3
Defence: 10
```

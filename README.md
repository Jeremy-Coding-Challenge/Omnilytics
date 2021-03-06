# Omnilytics

## How to run
1. `python challenge_a.py` - this will generate the output_a.txt
2. `python challenge_b.py` - this will print all of the strings and their respective types on console
3. `docker build -t challenge_c:latest .` - builds Docker image
4. `docker run challenge_c > output_b.txt` - execute dockerize challenge b and channel output to file "output_b.txt"

---
## Challenge A 

Write a program that will generate four (4) types of printable random objects and store them in a single file, each object will be separated by a ",".  These are the 4 objects: alphabetical strings, real numbers, integers, alphanumerics. The alphanumerics should contain a random number of spaces before and after it (not exceeding 10 spaces). The output should be 10MB in size.

Sample extracted output:
```
hisadfnnasd, 126263, assfdgsga12348fas, 13123.123, 
lizierdjfklaasf, 123192u3kjwekhf, 89181811238,122, 
nmarcysfa900jkifh  , 3.781, 2.11, ....
```
----

## Challenge B

Create a program that will read the generated file above and print to the console the object and its type. Spaces before and after the alphanumeric object must be stripped.

Sample output:
```
youruasdifafasd - alphabetical strings
127371237 - integer
asdfka12348fas - alphanumeric
13123.123 - real numbers
asjdfklasdjfklaasf - alphabetical strings
123192u3kjwekhf - alphanumeric
```
---- 

## Challenge C
Dockerize Challenge B. Write a docker file so that it reads the output from Challenge A as an Input. Once this container is started,  the program in challenge B is executed to process this file. The output should be saved in a file and should be exposed to the Docker host machine.

---
### UTF-8 Validation

**Description**
- For 1-byte character, the first bit is a 0, followed by its unicode code.
- For n-bytes character, the `first n-bits are all one's, the n+1 bit is 0`, followed by `n-1 bytes with most significant 2 bits being 10`.

```
Example 1
[197, 130, 1] -> 11000101 10000010 00000001.

[110]00101 = 2 bytes character   
[10]000010 = (2 bytes) starts with 10 

[0]0000001 = a single byte character 
```

```
Example 2 
[235, 140, 4] -> 11101011 10001100 00000100

[1110]1011 = 3 bytes character 
10001100 = (3 bytes) start with 10 
00000100 = (3 bytes) fails to start with 10 thus return false. 
```

```
Example 3 
[250,145,145,145,145] -> 11111010 10010001 10010001 10010001 10010001

[111110]10 = 5 bytes character but not a valid UTF-8 character 
A valid UTF-8 character can be 1 - 4 bytes long
```

<br>

**& operation**
- The `&` symbol is a bitwise AND operator.
- masks the value to extract the lowest bit
- tell you if the value is even or odd

```
11000101 = 197 
10000000 = 128 
01000000 = 64
--------------
1 - the left signifcant bit exists
2 - the second signifcant bit exists 
```

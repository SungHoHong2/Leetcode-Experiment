### UTF-8 Validation

**Description**
- For 1-byte character, the first bit is a 0, followed by its unicode code.
- For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.

```
Example 1
[197, 130, 1] -> 11000101 10000010 00000001.

[11]000101 = 2 byte character   
10000010 = (2 byte) starts with 10 

[0]0000001 = a single byte character 
```

```
Example 2 
[235, 140, 4] -> 11101011 10001100 00000100

[111]01011 = 3 byte character 
10001100 = (3 byte) start with 10 
00000100 = (3 byte) fails to start with 10 thus return false. 
```

### Iteration
* To execute the same basic task or set of statements multiple times
* Also allows variations with each repetition

### Counter-controlled Loops
* Execute a fixed numebr of times
* A special counter variable is assigned a different value each iteration and may be referenced to within the loop
* In python this is done by the for statement
```python
for i in range(1, 10):
#range(start, stop, step)
#Note: Always stop the iteration one less than the stop value
#Range returns an array (list) of numbers
	print("You dumb lol")
```

![[Pasted image 20230312211640.png]]

### Condition-controlled Loops
* The loop execute while the condition is true
```python
is_horny = True
nnn_day_count = 0
while is_horny:
	print("Pussy")
	nnn_day_count += 1
	if nnn_day_count == 30:
		break
```
![[Pasted image 20230312213942.png]]

### Post-check Loop
* Check the condtition for looping after the iteration
*  The do while loop in other languages
```javascript
//An example in javascript
pussie_count = 0
do {
console.log("Gimme the pussie plz 🥺")
pussie_count ++
} while (pussie_count <= 10)
```
```python
```

### Other Techniques
* Infinite loops: A loop that goes on forever
```python
while True:
# Don't actually run this shit lmao
	print("Jou ma se poes lol lol lol")
```
* break: To break out of a loop immediately
```python
jou_ma = 10
while True:
	jou_ma -= 1
	print("Jou ma se poes lol lol lol")
	if not jou_ma:
	# remember 0 is equivalent as False
		break
	
```

* continue: Immediately starts next iteration
```python
mama_protector = True
attack_remain = 10
while attack_remain > 0:
	attack_remain -= 1
	if mama_protector:
		print("Jou mama has been protected by the mama protector!!!!!")
		continue
	
	print("Jou ma is dead")
```
* else: Executes at the end of the loop that ends normally
```python
for i in range(10):
	print("Push")
	print("Pull")
else:
	print("The door is broken you dumbass")
```
* pass: To do nothing

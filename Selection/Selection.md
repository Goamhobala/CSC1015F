### If statement
* It's like a detour off a road. It's only temporary; eventually, they rejoin
![[Pasted image 20230224103737.png]]
* Uses boolean type to decide True or False:

```python
have_a_girlfriend = True
if have_a_girlfriend:
	print("Happy")

elif have_a_girlfriend == "in progress":
# AKA if ladder. Just a nicer way to write multiple selection (nested sequence.)
	print("good luck g")

else:
	print("sad :(")
```

* Note: use = for assignment and == for equation

### Nested If statement:

* putting a if statement inside another if statement:
```python
have_a_girlfriend = False
she_is_cute = null
if have_a_girlfriend:
	print("Happy")
	if she_is_cute:
		print("you fucking lucky bastard")

elif have_a_girlfriend == "in progress":
	print("good luck g")

else:
	print("sad :(")
```

### Dangling Else:

* Some programming languages have problem identifying which "if" does the else belong to
* Python doesn't have this problem because those in pair have the same indent level
Today, I learn the concepts of loop, range, and coding blocks.
So, for checking my practical understanding about the concepts, I tried to make a Password_Generator project.

In Password_Generator, we would be taking input as:
1) How many letters you want in your password.
2) How many numbers you want in your password.
3) How many symbols you want in your password.

Implementation of Password_Generator.


--> Here, I used two special built-ins :
(1) random.choice: This method return the randomly selected element from the specified sequence.
-> The Sequence can be string, a range, a list, a tuple or any other kind of sequence.

>> I used random.choice in taking a random char from letter, numbers, symbols for my password.

(2) random.shuffle: shuffle() method takes a sequence, like a list, and reorganize the order of the items.
<< This method only changes the original list, it does not return a new list.>>
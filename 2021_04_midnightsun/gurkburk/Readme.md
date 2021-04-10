# Challenge: Gurkburk (misc,python)

The flag is located in `./flag.txt`.

nc gurkburk-01.play.midnightsunctf.se 37541 

# My attempt (I didn't solve it)

It looks like an application that can store notes and display them.
I initially thought it was a pwn (heap) challenge, but the challenge mentioned it as misc.

There was a load notes option that takes some code as input.
I entered some garbage and it showed the traceback with some base64decode function.
Then I entered ./flag.txt in base64.
That gave a Unpickling error. So python pickle is involved.

I then picked a string './flag.txt' and sent it.
It did not report any error but when I try to print the display notes, it says the str has no function list\_notes(). So it is some form of a class object, not a str.

Ok so the code is just the pickle of a struct called Notes with two fields name and value, where value is a list.
I think we have to use some vulnerability of pickle library.
I read somewhere that it can lead to arbitrary code execution.

After searching I found that we can create a shell using the pickled data given below.
But the pickle didn't work on remote. There seems to be some restriction in remote that os.system is forbidden

```
cos
system
(S'/bin/sh'
tR.
```

But we only have to read the flag. So a shell is not necessary.

https://stackoverflow.com/questions/47705202/pickle-exploiting

I understood that defining the \_\_reduce\_\_ function will allow us to execute a single function with some arguments on remote while doing pickle.load(). But there are restrictions on what functions can be called.

I tried different functions (print, Notes constructor, etc), with different arguments, but couldn't figure out how to read the flag.

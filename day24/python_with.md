# Reading from a file

Use the open function to open a file.

    file = open("my_file.txt")

To read the contents of a file, use .read(). To see the contents, save it to a variable.

    contents = file.read()
    print(contents)

Once python opens a file, it'll stay open (and using resources) until you close it. Like tabs open on a computer. To close, use .close()

    file.close()

However, it can be hard to know when to close a file, and you might forget to close it. To combat this, we can change the way we open the file.

## with

Using 'with', we can open a file and then write 'as' to name it something.

    with open("my_file.txt") as file:
        contents = file.read()
        print(contents)

Basically a different way of opening/saving to a variable than what we did originally. Also, doing it this way, we don't need to remember to write file.close() at the end.

'with' is managing that file. Once it notices that we're done with it, we've performed whatever operations we wanted to using that file, it'll close it.

# Write to a file

If we simply write this:

    with open("my_file.txt") as file:
        file.write("New text.")

We'll get an error -- unsupported operation. That's because the default mode of open is 'read.' We have to change that mode in order to write.

    with open("my_file.txt", mode="w") as file:
    file.write("New text.")

If you run this and check the txt file, anything that was already in that file has now been deleted and replaced with "New text."

If we don't want to get rid of everything in the file, we can change the mode to "a", append. This will put the "New text." right after whatever is in the file.

    My favorite color is blueNew text.

To space it out, put \n in front of the text.

    with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

If you try to write to a file that doesn't exist, it'll create that file for you.

    with open("new_file.txt", mode="w") as file:
    file.write("New text.")

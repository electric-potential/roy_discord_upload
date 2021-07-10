# roy_discord_upload
A command line utility script that dismantles and recombines files for users to send over Discord to obey filesize limits.
The script is written in Python3 and can be used from a terminal to split a large file into multiple files (each under 8MB) like so:

<pre>
$ python rdu.py decompress my_file.txt
</pre>

Or, alternatively, can be used to recombine multiple files back into a single file like so:

<pre>
$ python rdu.py recombine my_file.txt
</pre>

Where `my_file.txt` was the original name of a split file. Decompressing a file creates multiple files
with filenames that start with the original filename so anyone can know what filename to enter to recombine a
file. Other arguments can be passed to the program:

<pre>
usage: rdu.py -i [path to read file(s)] -w [path to write file(s)] -b [max decompress filesize bytes] [mode (either decompress or recombine)] [filename]
</pre>

On another note, I ***__highly recommend__*** you use other means to send files to other people if you surpass the filsize limit on discord,
you can easily accomplish this same task by using other command line utilities such as `scp`. If you are insistent on sending files through discord,
then feel free to use this tool.

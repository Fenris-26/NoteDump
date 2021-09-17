# NoteDump
A Repository for the NoteDump.py tool mentioned in my HacktivityCon talk.

Two ways to use it:
1. Copy the python file over to the victim host, and run the script. It will automatically look in the default path for the users stickynotes database.
2. Exfil the sqlite database from the victim host, and then run the script and specify the location of the db.

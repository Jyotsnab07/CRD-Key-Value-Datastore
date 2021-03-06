# CRD-Key-Value-Datastore
Data is stored in form of key-value pair [ student - marks ] in .json file.<br/>
This data is accessed through python and converted to dictionary format , perform required actions and write back to .json file<br/>
source.py contains the code for read,create,delete and modify<br/>
display() function is used to write the updated date to the .json file<br/>
Time-to-live property has been included . User can enter timeout value during creation after which read/delete/modify operations are not possible<br/>
read() - For a given key if time-to-live has not expired and is available in datastore appropriate value is returned else error displayed<br/>
create() - If the key is not duplicate,memory limit not exceeded and is in string format , new key value pair created  else error displayed<br/>
delete() -  For a given key if time-to-live has not expired and is available in datastore respective key-value pair is deleted else error displayed<br/>
modify() - For a given key if time-to-live has not expired and is available in datastore , value can be modified for the respective key  else error displayed<br/>
access.py allows user to perform the required operations <br/>
import required : <br/>
import time<br/>
import json<br/>
import source as x<br/>
import threading<br/>


Question:
Freshworks – Backend Assignment
Build a file-based key-value data store that supports the basic CRD (create, read, and delete)
operations. This data store is meant to be used as a local storage for one single process on one
laptop. The data store must be exposed as a library to clients that can instantiate a class and work
with the data store.
The data store will support the following functional requirements.
1. It can be initialized using an optional file path. If one is not provided, it will reliably
create itself in a reasonable location on the laptop.
2. A new key-value pair can be added to the data store using the Create operation. The key
is always a string - capped at 32chars. The value is always a JSON object - capped at
16KB.
3. If Create is invoked for an existing key, an appropriate error must be returned.
4. A Read operation on a key can be performed by providing the key, and receiving the
value in response, as a JSON object.
5. A Delete operation can be performed by providing the key.
6. Every key supports setting a Time-To-Live property when it is created. This property is
optional. If provided, it will be evaluated as an integer defining the number of seconds
the key must be retained in the data store. Once the Time-To-Live for a key has expired,
the key will no longer be available for Read or Delete operations.
7. Appropriate error responses must always be returned to a client if it uses the data store in
unexpected ways or breaches any limits.
The data store will also support the following non-functional requirements.
1. The size of the file storing data must never exceed 1GB.
2. More than one client process cannot be allowed to use the same file as a data store at any
given time.
3. A client process is allowed to access the data store using multiple threads, if it desires to.
The data store must therefore be thread-safe.
4. The client will bear as little memory costs as possible to use this data store, while
deriving maximum performance with respect to response times for accessing the data
store.
Languages:<br/>
Ideally, we would not restrict you from working on a language of your choice. However, it
would be preferable if you stick with one of these -<br/>
• NodeJS<br/>
• Java<br/>
• Python<br/>
• GoLang<br/>
• Ruby<br/>
• C/C++
Submission:<br/>
Submit a link to the source code, ideally committed to Github.
Code accompanied by thorough unit tests is typically a mark of quality work.
Ideally, your data store will work on most operating systems. If this is not the case, please
specify which OSes are supported.

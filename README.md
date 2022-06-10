# Back Up Server Files Using MultiProcessing

Harness the power of the CPU!!! 

![evil-laugh](https://media4.giphy.com/media/EJIqwKKY30Dlu/giphy.gif)

## Use multiple processers on host machine to back up server files

![backup](https://blackrockbusiness.com/wp-content/uploads/2013/04/Cloud-Backup-Support.jpg)

This script is my take on the solution for the Week 2 Google Certification Course for Troubleshooting and Debugging the OS.

You can set the source and destination locations of your files using the `src` and `dest` variables.

```python
src = "source_location"
dest = "destination"
```

## Pools

This script uses the Pool method from the multiprocessing module that we use to generate a batch of processes for our
back up task.

By using subprocess module, we can designate the folders we want to back up from a specific source to these batch of processes
so that they can take advantage of the built in processor on the machine. 

We use the function `get_folders_to_backup()` and pass the `src` as
a parameter to get a list of of the folders we want to back up.

We use this list to generate the number of processes we want when creating an instance of Pool, which we then call this instance using map
to designate each folder to the function `backup_files`

```python
tasks = get_folders_to_backup(src)
# Cert the number of processes with Pool
p = Pool(len(tasks))
# Map each task to the backup_files function
p.map(backup_files, tasks)
```
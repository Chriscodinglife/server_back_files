#!/usr/bin/env python

'''
This script written in Python 2 was for tackling the Week 2 Python Google Certificate for the Troubleshooting and Debugging course.

This script utilizes the multiprocessing module to create a pool of processes to run several rsync tasks using the subprocess module.

'''

import os
import subprocess
from multiprocessing import Pool

src = "location_1"
dest = "location_2"

def get_folders_to_backup(source):

        '''Get a list of all the files that need to be backed up'''
        i = 0
        list = []
        for root, dirs, files in os.walk(source):
                for name in dirs:
                        list.append(name)
                i += 1
                if i == 1:
                        break

        return list


def backup_files(folder):

        '''Back up a list of folders from source to destination'''

        source = "{}/{}".format(src, folder)
        destination = "{}/{}".format(dest, folder)

        print("Backing up {} to {}".format(source, destination))
        subprocess.call(["rsync", "-arq", source, destination])


if __name__ == "__main__":

        # Gather the list of folders that need to be backed up
        tasks = get_folders_to_backup(src)
        # Cert the number of processes with Pool
        p = Pool(len(tasks))
        # Map each task to the backup_files function
        p.map(backup_files, tasks)
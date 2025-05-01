# PLUS W - IT Training
*Date: April 26, 2025*

## Class 14: Linux User Management & File Permissions for Software Developers

### Acknowledgement
- Supported by **AOTS** and **OEC**
- **Ministry of Economy, Trade and Industry**
- **Overseas Employment Corporation**

## 1. Recap of Last Week
- Usage of control and loop flow statements
- Performing Linear Algebra in NumPy
- Inspecting and understanding data
- Importance of requirement analysis
- Machine learning algorithms
- Software Development Life Cycle (SDLC)
- Importance of security compliance
- Detailed steps for launching a new EC2 instance

## 2. Today’s Focus
- Understanding the Linux file system hierarchy and user roles
- Step-by-step guide on creating users and groups
- Changing file permissions and ownership
- Basic and system-level Linux commands
- Quiz
- Q&A session

## 3. Exploring the Linux File System Hierarchy
- **What is a File System?**: A method for storing and organizing files on a storage device.
- **Why Hierarchy Matters?**: Everything in Linux is treated as a file, following a tree-like structure starting from `/` (root).
- **Key Directories and Their Purposes**:
  - `/` – Root directory (base of the file system)
  - `/bin` – Essential binaries (e.g., `ls`, `cat`)
  - `/etc` – Configuration files (e.g., network settings)
  - `/home` – User personal directories (e.g., `/home/john`)
  - `/var` – Variable data like logs, mail, etc.
  - `/usr` – User-installed applications and libraries
  - `/tmp` – Temporary files
  - `/root` – Home directory for root user
  - `/opt` – Optional packages/software

## 4. Paths and File Types
- **Absolute Path**: Full path from root (e.g., `/home/user/file.txt`)
- **Relative Path**: Based on current location (e.g., `../Documents`)
- **File Types**:
  - `-` → Regular files
  - `d` → Directory
  - `l` → Symbolic link
  - `c/b` → Character/Block device

## 5. Users, Groups, and Permissions
- **Root User**: Superuser with all privileges
- **Normal Users**: Limited access to system
- **System Users**: Run background processes (e.g., `mysql`, `www-data`)
- **Important Files**:
  - `/etc/passwd` – List of all users
  - `/etc/shadow` – Encrypted passwords
  - `/etc/group` – Group memberships
- **Example**: `cat /etc/passwd | grep hamza`  
  Output: `hamza:x:1001:1001:Hamza Munir:/home/hamza:/bin/bash`

## 6. Linux Commands
- **Basic Navigation and File Handling**:
  - `cd` – Change directory
  - `ls` – List files/directories
  - `pwd` – Print working directory
  - `cp` – Copy files/folders
  - `mv` – Move/rename files
  - `rm` – Delete files/directories
  - `mkdir` – Create a directory
  - `touch` – Create an empty file
  - `cat` – Display file contents
  - `less` – View file contents (scrollable)
- **Text Editors & Viewers**:
  - `nano file.txt` – Easy-to-use text editor
  - `vim file.txt` – Powerful editor for advanced users
  - `head -n 5 file.txt` – First 5 lines
  - `tail -n 10 file.txt` – Last 10 lines
- **Search and Extract**:
  - `grep 'error' log.txt` – Search for "error"
  - `cut -d ':' -f 1 /etc/passwd` – Extract usernames
- **System Monitoring Commands**:
  - `top` – Real-time process monitor
  - `free -h` – Show memory usage
  - `df -h` – Disk space usage
  - `du -sh folder/` – Size of a folder
  - `uptime` – System running time
  - `htop` – Colorful version of top (may require install)
- **Process Management Commands**:
  - `ps aux` – List running processes
  - `kill PID` – Terminate a process by PID
  - `kill -9 PID` – Force kill
  - Example: `ps aux | grep apache`, `kill 12345`
- **User Session and Log Commands**:
  - `who` – Logged in users
  - `whoami` – Current user
  - `w` – Detailed session info
  - `last` – Last logged in users
  - `id` – UID, GID, and group info

## 7. Creating a New User
- `useradd username` – Add new user (basic)
- `adduser username` – Interactive version (recommended)
- `passwd username` – Set password for user
- **Example**:  
  ```bash
  adduser john
  passwd john
  ```

## 8. Creating a New Group
- `groupadd groupname` – Create a new group
- **Example**: `groupadd devs`

## 9. Adding Users to Groups
- `usermod -aG groupname username` – Add user to group (append)
- **Example**: `usermod -aG devs john`

## 10. Viewing User and Group Information
- `groups username` – Lists all groups the user belongs to
- `cat /etc/passwd` – User account info
- `cat /etc/group` – Group info
- `id username` – Shows UID, GID, and group memberships
- **Example**: `id john`, `groups john`

## 11. Deleting Users and Groups
- `userdel username` – Deletes user
- `userdel -r username` – Deletes user & home directory
- `groupdel groupname` – Deletes group
- **Example**: `userdel -r john`, `groupdel devs`

## 12. Understanding File Permissions Structure
- **Permissions**:
  - **User (u)** – File owner
  - **Group (g)** – Group members
  - **Others (o)** – Everyone else
  - `r` – Read, `w` – Write, `x` – Execute
- **Example Output**: `-rwxr-xr-- 1 user group 1234 Apr 10 file.sh`

## 13. Viewing Permissions with ls -l
- `ls -l filename`
- **Example**: `-rw-r--r-- 1 user group 1234 Apr 10 file.txt`

## 14. Changing Permissions Using chmod
- **Symbolic Mode**:
  - `chmod u+x file.sh` – Add execute to user
  - `chmod g-w file.txt` – Remove write from group
- **Numeric Mode**:
  - `r=4`, `w=2`, `x=1`
  - `chmod 755 script.sh` → `rwxr-xr-x`
  - `chmod 644 file.txt` → `rw-r--r--`

## 15. Changing Ownership with chown
- `chown newuser file.txt` – Change owner
- `chown newuser:newgroup file` – Change owner & group
- **Example**: `chown hamza:devs project.log`

## 16. Changing Group with chgrp
- `chgrp newgroup file.txt`
- **Example**: `chgrp staff notes.txt`

## 17. Practical Scenarios for Permissions
- **Restricting Access**: `chmod 600 secrets.txt` (only owner can read/write)
- **Shared Directory**:
  ```bash
  chmod 770 shared/
  chown :developers shared/
  ```

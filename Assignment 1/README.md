# Assignment 1 – Ansible Project

This project manages two files:

- /tmp/testme-1.py
- /tmp/testme-2.py

Final permissions: rwxr-x--- (0750)

## Roles

### create_files
Creates the two files and sets permissions.

### ensure_shebang
Ensures a correct Python shebang exists (idempotent).

### add_header
Adds a header to the files (idempotent).

## Running the playbook

Run all roles:

## AI Assistance 
- Help structure the Ansible project
- Ensure idempotency and correct permission handling

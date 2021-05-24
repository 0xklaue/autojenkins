


# autojenkins
Streamline your Jenkins

# What is autojenkins?
autojenkins is a python2 script that allows you to streamline your pipeline by automating tasks that can be lenghty, tedious, and worth automating.

# Why autojenkins?
autojenkins was created to automate certain tasks via python script, such as onboarding repositories for secure code review on SonarQube/Checkmarx/Fortify from a Git based solution (GitHub/GitLab/BitBucket).

# How to use?
You need 2 files for autojenkins to be operational:
 - Configuration file (`config.xml`) of your Jenkins
 - List of all repositories to be added in a CSV file, repos.csv. The format should be as following: 

Keep your Jenkins config.xml & repos.csv in the same directory:

# Usage

```sh
python2 autojenkins.py
```
# Questions
Reach me out on Twitter: [@0xklaue](https://twitter.com/0xklaue)

<img src="https://www.jenkins.io/images/logos/jenkins-is-the-way/jenkins-is-the-way.png" width="200" height="250">

# autojenkins
Streamline your Jenkins

# What is autojenkins?
autojenkins is a python2 script that allows you to streamline your pipeline by automating tasks that can be lenghty, tedious, and worth automating.

# Why autojenkins?
autojenkins was created to automate certain tasks via python script, such as onboarding repositories for secure code review on SonarQube/Checkmarx/Fortify from a Git based solution (GitHub/GitLab/BitBucket).

# How to use?
You need 2 files for autojenkins to be operational:
 - Configuration file (`config.xml`) of your Jenkins
 - List of all repositories to be added in a CSV file, `items.csv`. The format should be as following: 

<img src="https://github.com/0xklaue/autojenkins/blob/main/res/items.png">

Keep your Jenkins config.xml & repos.csv in the same directory

# Usage

```sh
python2 autojenkins.py
```
# Questions
Reach me out on Twitter: [@0xklaue](https://twitter.com/0xklaue)

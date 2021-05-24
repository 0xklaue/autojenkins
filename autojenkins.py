import jenkins
import xml.etree.ElementTree as ET
import time
import csv
import subprocess
from queue import Queue as Queue
# Banner :)

def print_banner(title=""):
    subprocess.call("clear")
    print("""
               __          _            __   _
  ____ ___  __/ /_____    (_)__  ____  / /__(_)___  _____
 / __ `/ / / / __/ __ \  / / _ \/ __ \/ //_/ / __ \/ ___/
/ /_/ / /_/ / /_/ /_/ / / /  __/ / / / ,< / / / / (__  )
\__,_/\__,_/\__/\____/_/ /\___/_/ /_/_/|_/_/_/ /_/____/
                    /___/

""")
    total_len = 60
    if title:
        padding = total_len - len(title) - 4
        print("== {} {}\n".format(title, "=" * padding))
    else:
        print("{}\n".format("=" * total_len)) 



# Declare XML
config_file = './res/config.xml' # Enter your jenkins config file here, or enter your own file.
tree = ET.parse(config_file)
root = tree.getroot()
# Convert XML to String
def convert_xml():
  return ET.tostring(root).decode()
def getElements():
    try:
        with open('./res/items.csv', 'r') as filecsv: #Edit this items.csv as per your requirement
            csv_reader = csv.reader(filecsv, delimiter=',')
            server = jenkins.Jenkins('<Enter Jenkins URL>', username='<Enter Jenkins username>', password='<Enter Jenkins API token>') # Enter your Jenkins server IP, Username & Jenkins API token.
            config = convert_xml()
            for row in csv_reader:
                try:
                    githubURL = root.find("./scm/userRemoteConfigs/hudson.plugins.git.UserRemoteConfig/url")
                    githubURL.text = row[0]
                    jobName = row[2]
                    githubBranch = root.find("./scm/branches/hudson.plugins.git.BranchSpec/name")
                    githubBranch.text = row[1]
                    sonarProperties = root.find("./builders/hudson.plugins.sonar.SonarRunnerBuilder/properties")
                    sonarProperties.text = "\n\nsonar.projectKey=myProject."+jobName+"\nsonar.projectName="+jobName+"\nsonar.projectVersion=1.0\nsonar.sources=.\nsonar.sourceEncoding=UTF-8\nsonar.java.binaries=${WORKSPACE}" # Make changes accordingly!
                    tree.write(config_file)
                    myconfig = ET.tostring(root)
                    server.create_job(jobName, myconfig)
                    print "[+] Jenkins job created: ", row[2]
                    server.build_job(jobName)
                except jenkins.JenkinsException:
                    print "[!] Job already exists!", jobName
                    continue
    except KeyboardInterrupt:
        print("\n[!] Interrupt caught. Exiting")
    
# Main
def main():
    print_banner()
    getElements()
    
main()

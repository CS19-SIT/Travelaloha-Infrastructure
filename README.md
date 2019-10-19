---
title: "CSC 210/BIF 521 Analysis and Design of Algorithms | CSC218 Database Systems"
author: ["thanadon.rh@mail.kmutt.ac.th", "ID: 61130500240"]
date: "2019-10-15"
subject: "Markdown"
keywords: [Markdown, Algorithms, Database, Infrastructure]
subtitle: "An Overall step-by-step Infrastructure documentation"
lang: "en"
titlepage: true
titlepage-color: "1E90FF"
titlepage-text-color: "FFFAFA"
titlepage-rule-color: "FFFAFA"
titlepage-rule-height: 2
book: true
classoption: oneside
...
# Travelaloha-Infrastructure

## Introduction

This Doumentation contains all efforts that were conducted in order to configure the server to deploy the project.

# High-Level Summary

I was tasked with configuring the server to deploy our project.
The project is part of CSC 210/BIF 521 Analysis and Design of Algorithms and CSC218 Database Systems.
The focus of this project is to put our theory into practice.
My overall objective was to configure the network, and systems.

# Installing Jenkins 

Jenkins is an open-source tool that tests and compiles the code.
Jenkins is used to minimizes the testing time and automates the deployment of new commits from github.

## Step 1 : we need to install Java.
```bash
sudo apt-get update
sudo apt-get install openjdk-11-jre-headless
```

## Step 2 : Add the Jenkins key to apt.
```bash
wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
```

## Step 3 : Creates the source list for Jenkins.
```bash
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
```

## Step 4 : Install Jenkins
```bash
sudo apt-get update
sudo apt-get install jenkins
```
## Step 5 : Complete Jenkins Setup
Go to http://35.247.178.19:8080/ The initial password is in
```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```
## Step 6 : Create new Item in Jenkins
### Step 6.1 : Create a Freestyle Project
### Step 6.2 : In General
Select Github project.
Add Project URL.
```bash
https://github.com/CS19-SIT/travel-aloha
```
### Step 6.3 : In Source code Management
Select Git.
Add Repository URL.
```bash
https://github.com/CS19-SIT/travel-aloha.git
```
Add Credentials.
Add Branch Specifier.

### Step 6.4 : In Build Triggers
Select Github hook trigger for GITScm polling.

### Step 6.5 : In Build
Select Add build step.
Select Execute shell.
Add in desired commands, For this project it will be
```bash
/bin/bash
cd /var/www/project
git pull origin master
npm i
sudo pm2 restart 0
```

## Step 7 : Post Setup
normally Jenkins user does not have permission in most of the system folders.
We need to change this by giving sudoers group to Jenkins user.
```bash
sudo visudo
```
Navigate to the end of the file, Then add.
```nano
jenkins ALL=(ALL) NOPASSWD: ALL
```

# Additional Items

## Appendix - Things here:

```
code here
```
# Django | GLUGWeb

## Mission 1 | Establish a Member Verification Portal

### Definitions

1. *Bold* text in _Logical database requirement_ indicates *primary key*

### Objectives

1. A portal similar to [UIDAI verification system](https://resident.uidai.net.in/aadhaarverification)
2. A mechanism to register new members automatically via Slack
3. A key which is returned to the user via a Slack bot
4. A rating mechanism

### Specific requirements

#### External interface requirements

1. Public
    - Batch, course, stream, SAP ID
    - Duration served
    - Rating

2. Private

#### Logical database requirement

1. Members
    - *MemberID*
    - First name
    - Last name
    - Date of birth
    - Sex
    - Batch
    - SAP ID
    - Division
    - Year
    - Course
    - Stream
    - Phone
    - Email
    - Address

## Mission 2 | A seamless tyler


---

## Member Verification

### Objectives

1. Gmail will be used for log-in
2. Two set of users:
  - GLUG members
  - Public access
3. Access control matrix for differentiating between sets of users, after gmail verifies the user
4. GLUG members will be allowed access to all the online resources available
5. Public access will be restrained


## Blog posts

### Objectives

1. Glugizens can write blogs on various topics and these will be a part of the website.
2. Access available to both sets of users


## How-To Guide

### Objectives

1. This will act as the guidelines for most How-Tos revolving around Open Source/ GNU/linux
2. Access will be made available to both sets of users


## Code snippets

### Objectives

1. Tiny code snippets (in any preferred language) as a part of the website
2. Access available exclusively to Glugizens


## Book library

### Objectives

1. Online resource basket
2. Collaboration of all ebooks available with any Glugizen
3. Access available exclusively to Glugizens


## Grouping the Modules

### Objectives

1. To group all the resources made available online with respect to:
  - Domains
    - All available resources will be divided according to their Domains
    - For eg., resources categorized as Data Analytics, Hacking, Web Development, etc.
  - Functionality
    - All available resources will be divided according to their Functionality
    - For eg., resources categorized as blogs, snippets, guides, library, etc.
2. Both the options will be available to the user simultaneously. User can choose according to comfort.

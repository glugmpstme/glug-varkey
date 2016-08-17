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
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
	1.1. Batch, course, stream, SAP ID
	1.2. Duration served
	1.3. Rating

2. Private

#### Logical database requirement

1. Members
	1.1. *MemberID*
	1.2. First name
	1.3. Last name
	1.4. Date of birth
	1.5. Sex
	1.6. Batch
	1.7. SAP ID
	1.8. Division
	1.9. Year
	1.10. Course
	1.11. Stream
	1.12. Phone
	1.13. Email
	1.14. Address

## Mission 2 | A seamless tyler
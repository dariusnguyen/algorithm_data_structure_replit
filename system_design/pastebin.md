Design Pastebin, a website where you can store and share text online for a set period of time.

Requirements/Scope
- Paste text only
- Text can be up to 100,000 chars
- generate a random key
- users can choose a key
- paste is valid for 7 days by default
- user can set the expiration up to 30 days from creation
- 1M new pastes/day

Capacity estimation
1M pastes/day
365 M pastes/yr
3650 M ~ 3.6 M pastes/10 yrs

storage:
paste content
	100,000 chars/paste
	1 Byte/char
	100 KB/paste

meta data:
	URL
	base 64 encoding A-Z a-z 0-9 -+
	6 chars should accomodate more than enough strings
	64^6 = 68 B strings
	1 Byte/char
	 6 chars/key
	6 Bytes/key

	potential other info to store:
	username
	password
	IP address

Assume total per paste does not exceed 150 KB

1M pastes/day
1M * 150 KB /day = 150 * 1000 * 1000 KB/day = 150 GB /day
150 * 365 GB / yr = 54 750 ~ 55 TB/yr
10 years: 550 TB

Traffic:
	5:1 read:write ratio
	5M reads + 1M writes/day
	~58 reads/sec
	~11 writes/sec

 API design
createPaste(apiKey, paste, customKey, expire)
	 return: key (string)
  
readPaste(apiKey, key)
	return: paste

updatePaste(apiKey, key, newPaste)
	return bool
 
deletePaste(apiKey, key)
	return bool

Database design
object storage db:
	key: paste key
	value: paste content

meta data Db:
	Paste table
		key (PK)
		contentKey
		userID (FK)
		timestamp


	User table
		userID (PK)
		encryptedPW
		email
		creationDate
		lastLogin
		

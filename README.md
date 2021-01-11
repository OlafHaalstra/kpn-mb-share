# Share KPN MBs with family members
Docker container to share MBs between mobile phone numbers at the first of the month.

## Installation
Create a `.env` file with your preferences, see the `.env.example` file which fields must be filled. Don't forget to remove the comments. A correct `.env` file could look like this:
```
EMAIL=someone@example.com
PASSWORD=secret123
NUMBER=0612345678
SC_SERVICE_TOKEN=aBCd1234
NUMBERS=0601010101,0602020202
MBS=6000,1337
```
Which will sent 6000MB to 0601010101 and 1337MB to 0602020202, by default once per month.

### Getting the `SC_SERVICE_TOKEN`
The easiest way is to log in to [mijn.kpn.com](mijn.kpn.com) and open the developer tools. Then go to `Application` > `Local storage` > `https://mijn.kpn.com` and in the `Value` field copy the `serviceToken`.

### Running
Once you have succesfully created a `.env` file you can now run the script on a server, if you use Docker you can run:
```
docker build -t kpn-mb-share . 
docker run -d --name kpn-mb-share
```

The script is scheduled with `cron` in `entrypoint.sh` to run every first of the month at exactly 00:05.

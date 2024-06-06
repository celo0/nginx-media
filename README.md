# nginx-media
Basic nginx config for accesing all your media services under only one domain name (including autoindex for download files if needed)  
Some people may call it URI or folder or path.  
In example:  
your.domain.com is your base URL and it has a simple page with links to redirect to your services

your.domain.com/plex is your URL for your plex server  
your.domain.com/qbit is your URL for your qBitTorrent WebUI  
your.domain.com/sonarr is your URL for your Sonarr  
your.domain.com/radarr is your URL for your Radarr  


Remember that I'm using a Windows version of NGINX.  
If you're using it on linux, **copy only the server directive and the ssl configuration**. The default nginx.conf file for linux and windows are a bit different.


Generate Let's Encrypt certificate with certbot without automatic renew and needed access to add records to your DNS.
certbot certonly --manual --preferred-challenges dns -d your.domain.com
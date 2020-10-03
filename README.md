# flask_iframe_refresh

Flask app to provide a basic dashboard to show whether a host is online or offline.

Hosts are specified in the target_sites.csv file (category, host name, URL) and the results are presented in an iframe. Javascript is used to refresh the iframe every 60 seconds, but of course this is configurable.

HTTP/HTTPS requests made by the app are set so they do not require certificte validation. A request is deemed to be successful if the response code is 200 - any other code results in the site being designated as unreachable.

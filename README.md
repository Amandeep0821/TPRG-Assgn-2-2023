# TPRG-Assgn-2-2023
# Commit one
Server Working 
The Server code establishes a server on a Raspberry Pi that continuously listens for connections. Upon connection, it fetches core temperature and additional system data using vcgencmd commands. This information is added to a JSON object, converted to a string, and sent to the client as bytes. The server loop ensures a continuous stream of real-time performance metrics to connected clients.

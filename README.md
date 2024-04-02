# Python Socket Programming

This repository contains two key projects demonstrating the power of socket programming in Python. It showcases a network bandwidth monitor and a basic client-server application using threading for concurrent connections.


## Projects

### Bandwidth Monitor

The `bandwidth-monitor` directory houses a Python script (`bandwidth.py`) that provides real-time network bandwidth monitoring.

#### Features:
- Real-time upload and download speeds
- Graphical representation of network usage (Screenshots in the `ss` folder)

#### How to Run:
Ensure you have Python installed on your system. Then run the following command in your terminal:

```bash
python bandwidth-monitor/bandwidth.py
```

#### Output:
![Bandwidth Monitor Screenshot](screenshots/Figure4.png)


### 2. Client-Server Connection

The `client-server` directory features a simple implementation of socket-based client and server programs, demonstrating basic network communication.

#### Features:
- Establish a socket connection between a server and multiple clients.
- Utilize threading to manage multiple client connections simultaneously.

#### How to Run:
Launch the server by executing:
```bash
python server.py
```

Open another terminal window and start the client by running:
```bash
python client.py
```

### Installation Requirements
Both projects require only Python to be installed on your system. No additional libraries are necessary, as they use the Python standard library.

### Future Developments
A Command Line Interface (CLI) chat application built upon the client-server architecture for real-time communication.

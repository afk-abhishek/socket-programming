# Socket Programming Journey 🚀

A structured, hands-on learning journey to master **socket programming** through progressively challenging projects.
This repository documents practical implementations, experiments, and concepts related to **network communication using sockets**.

The goal is to move from **basic TCP communication → multi-client systems → custom protocols → real-time applications**.

---

# 📚 What This Repository Covers

- Fundamentals of **TCP socket programming**
- Building **client-server architectures**
- Handling **multiple clients**
- Designing **simple application protocols**
- Implementing **real-time communication systems**
- Writing **tests for network programs**

All projects are written primarily in **Python**, focusing on clarity and practical understanding.

---

# 🗂 Repository Structure

```
socket-programming-journey/
├── README.md                    # Main project overview & roadmap
├── QUICKSTART.md               
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore file
│
├── 01-basics/                 
│   ├── README.md              # Detailed phase guide
│   ├── tcp_echo_server.py     
│   ├── tcp_echo_client.py     
│   └── tests/
│       └── test_tcp_echo.py   # Test templates
│
├── 02-chat-app/               # Phase 2
│   └── README.md
│
├── 03-protocols/              # Phase 3
│   └── README.md
│
├── 04-real-time/              # Phase 4
│   └── README.md
│
└── resources/
    └── LEARNING.md          
```

---

# 🧭 Learning Roadmap

## Phase 1 — Basics

Learn the fundamentals of socket communication.

Topics:

- TCP sockets 
- Client–server architecture 
- Sending and receiving data 
- Handling connections 

---

## Phase 2 — Chat Application

Build a simple messaging system.

Topics:

- Multi-client servers 
- Threading / concurrency 
- Broadcasting messages
- Managing connected users 



---

## Phase 3 — Protocol Design

Understand how application protocols work.

Topics:

- Message framing 
- Serialization 
- Custom command protocols 
- Error handling 

---

## Phase 4 — Real-Time Systems

Apply networking concepts to real-time communication.

Topics:

- WebSockets 
- Asynchronous networking 
- Event-driven servers 
- Real-time updates 

---

# ⚡ Quick Start

Clone the repository:

```bash
git clone https://github.com/yourusername/socket-programming-journey.git
cd socket-programming-journey
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start with the basics phase:

```bash
cd 01-basics
```

Follow the instructions inside:

```
01-basics/README.md
```

---

# 🧪 Running Tests

Tests are included to verify socket behavior.

Run them using:

```bash
pytest
```

---

#  Goals of This Project

- Learn **network programming by building**
- Understand **how communication protocols work**
- Develop **debugging skills for distributed systems**


---

# Contributions

This repository is primarily a **personal learning project**, but suggestions, improvements, and discussions are welcome.

If you'd like to contribute:

1. Fork the repository 
2. Create a feature branch 
3. Submit a pull request 

---

# Note

This repository focuses on **learning by building real systems**

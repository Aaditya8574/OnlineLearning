# Comprehensive Technical Learning Roadmap

## Five Specializations

1. Electronics, Signals, Systems, and Digital Control
2. Computer Science, Computer Architecture, and Systems Software
3. Embedded Systems, Microcontrollers, and IoT
4. Computer Networks and Cybersecurity
5. Robotics, Computer Vision, and Autonomous Systems

---

# LEARNING PLAN: GENERAL RULES

### Starting assumptions

- High-school mathematics and physics are already known.
- No university-level engineering or computer-science knowledge is assumed.
- All essential prerequisites must be taught within this roadmap.
- Practical assignments, laboratories, and projects are mandatory.
- Prefer free learning materials and inexpensive certificates.
- Avoid unnecessary repetition between specializations.
- Nand2Tetris is shared between Computer Science and Embedded Systems.
- Mathematics courses are shared across the relevant specializations.

### Difficulty scale

| Level | Meaning |
|---|---|
| Beginner | No prior knowledge of the subject required. |
| Beginner–Intermediate | Basic programming or mathematics may be useful. |
| Intermediate | Requires previous foundational courses. |
| Advanced | Requires substantial mastery of earlier courses. |

### Course classification

- CORE: Essential to the specialization.
- ADVANCED: Important for deeper technical understanding.
- OPTIONAL: Useful extension, but not essential to the core learning objectives.
- GUIDED STUDY: A structured collection of resources and exercises, rather than one formal course.

---

# SPECIALIZATION 1
# ELECTRONICS, SIGNALS, SYSTEMS, AND DIGITAL CONTROL

## Objective

Develop a strong understanding of:
- Electrical circuits and electronic components.
- Analog and digital electronics.
- Semiconductor devices and amplifiers.
- Signals and systems.
- Fourier and Laplace transforms.
- Continuous and discrete-time systems.
- Feedback and control theory.
- PID controllers.
- State-space modelling.
- Digital control systems.

| Order | Course name | Platform link | Expected time | Difficulty | Course prerequisite links |
|---|---|---|---|---|---|
| 1 | Single Variable Calculus — MIT 18.01SC | [MIT OCW](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) | 6–8 weeks | Beginner–Intermediate | High-school algebra, functions, and trigonometry. |
| 2 | Multivariable Calculus — MIT 18.02SC | [MIT OCW](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/) | 5–7 weeks | Intermediate | [Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/). |
| 3 | Linear Algebra — MIT 18.06SC | [MIT OCW](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) | 5–7 weeks | Beginner–Intermediate | High-school algebra and vectors. |
| 4 | Differential Equations — MIT 18.03SC | [MIT OCW](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/) | 6–8 weeks | Intermediate | [Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) and [Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/). |
| 5 | Circuits and Electronics — MIT 6.002 | [MIT OCW](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) | 8–10 weeks | Intermediate | [Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) and [Differential Equations](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/). |
| 6 | Introduction to Electronics | [Georgia Tech — Coursera](https://www.coursera.org/learn/electronics) | 4–6 weeks | Intermediate | [MIT Circuits and Electronics](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/). |
| 7 | Signals and Systems — MIT 6.003 | [MIT OCW](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/) | 6–8 weeks | Intermediate–Advanced | [Differential Equations](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/), [Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), and [Circuits and Electronics](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/). |
| 8 | Feedback Control Systems — MIT 2.14 | [MIT OCW](https://ocw.mit.edu/courses/2-14-analysis-and-design-of-feedback-control-systems-spring-2014/) | 6–8 weeks | Advanced | [Differential Equations](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/), [Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), and [Signals and Systems](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/). |
| 9 | Digital Control Systems — MIT 2.171 | [MIT OCW](https://ocw.mit.edu/courses/2-171-analysis-and-design-of-digital-control-systems-fall-2006/) | 6–8 weeks | Advanced | [Feedback Control Systems](https://ocw.mit.edu/courses/2-14-analysis-and-design-of-feedback-control-systems-spring-2014/) and [Signals and Systems](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/). |

### Core topics to master

| Subject | Required concepts |
|---|---|
| Circuit theory | Kirchhoff's laws, nodal analysis, mesh analysis, Thevenin and Norton equivalents |
| Electronics | Diodes, BJTs, MOSFETs, op-amps, amplifiers |
| Digital electronics | Logic gates, combinational and sequential circuits |
| Signals | Continuous and discrete signals, convolution, Fourier series and transforms |
| Systems | Laplace transforms, Z transforms, transfer functions |
| Control | Feedback, stability, PID, root locus, frequency response |
| Modern control | State-space models, controllability, observability |
| Digital control | Sampling, discretization, digital filters, digital controllers |

### Required project

**Closed-loop DC Motor Speed Controller**

1. Derive a mathematical model of a DC motor.
2. Simulate its behaviour.
3. Design a PID controller.
4. Evaluate stability and transient response.
5. Discretize the controller.
6. Implement it on a microcontroller.
7. Measure overshoot, settling time, steady-state error, and disturbance rejection.

---

# SPECIALIZATION 2
# COMPUTER SCIENCE, COMPUTER ARCHITECTURE, AND SYSTEMS SOFTWARE

## Objective

Develop deep understanding of:
- Programming and computational thinking.
- C, C++, and Python.
- Data structures and algorithms.
- Computer architecture.
- Processor design and memory hierarchy.
- Compilers and interpreters.
- Operating systems.
- Linux and kernel internals.
- Databases.
- Containers and virtualization.
- Boot process and memory management.

| Order | Course name | Platform link | Expected time | Difficulty | Course prerequisite links |
|---|---|---|---|---|---|
| 1 | CS50x — Introduction to Computer Science | [Harvard CS50x](https://cs50.harvard.edu/x/) | 10–14 weeks | Beginner–Intermediate | None. |
| 2 | Mathematics for Computer Science — MIT 6.042J | [MIT OCW](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) | 6–8 weeks | Intermediate | [CS50x](https://cs50.harvard.edu/x/). |
| 3 | Nand2Tetris Part I — Hardware | [Nand2Tetris](https://www.nand2tetris.org/) / [Coursera](https://www.coursera.org/learn/build-a-computer/) | 5–7 weeks | Intermediate | [CS50x](https://cs50.harvard.edu/x/). |
| 4 | Nand2Tetris Part II — Software | [Nand2Tetris](https://www.nand2tetris.org/) / [Coursera](https://www.coursera.org/learn/nand2tetris2/) | 5–7 weeks | Intermediate | [Nand2Tetris Part I](https://www.coursera.org/learn/build-a-computer/). |
| 5 | Introduction to Algorithms — MIT 6.006 | [MIT OCW](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) | 8–10 weeks | Advanced | [CS50x](https://cs50.harvard.edu/x/) and [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/). |
| 6 | Computation Structures — MIT 6.004 | [MIT OCW](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) | 6–8 weeks | Intermediate–Advanced | [Nand2Tetris Part I](https://www.coursera.org/learn/build-a-computer/) and [CS50x](https://cs50.harvard.edu/x/). |
| 7 | Operating System Engineering — MIT 6.1810 | [MIT PDOS](https://pdos.csail.mit.edu/6.1810/2026/) | 8–10 weeks | Advanced | [Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/), [CS50x](https://cs50.harvard.edu/x/), and [Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/). |
| 8 | Database Systems — CMU 15-445/645 | [CMU Database Systems](https://15445.courses.cs.cmu.edu/) | 8–12 weeks | Advanced | [CS50x](https://cs50.harvard.edu/x/), [Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/), and familiarity with C++ and memory management. |
| 9 | Linux and Systems Programming — Guided Study | [Linux Journey](https://linuxjourney.com/), [Linux Kernel Documentation](https://docs.kernel.org/), [Linux man-pages](https://www.kernel.org/doc/man-pages/), [Docker Documentation](https://docs.docker.com/get-started/) | 6–8 weeks | Intermediate–Advanced | [CS50x](https://cs50.harvard.edu/x/), [Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/), and [Operating System Engineering](https://pdos.csail.mit.edu/6.1810/2026/). |

### Core topics to master

| Subject | Required concepts |
|---|---|
| Programming | C, C++, Python, memory management, pointers |
| Data structures | Arrays, linked lists, stacks, queues, trees, graphs, hash tables |
| Algorithms | Sorting, searching, dynamic programming, graph algorithms |
| Computer architecture | ALU, registers, instruction execution, pipelining |
| Memory | Registers, cache, SRAM, DRAM, flash, virtual memory |
| Compilers | Lexical analysis, parsing, intermediate representation, code generation |
| Operating systems | Processes, threads, scheduling, synchronization, virtual memory |
| Kernel | System calls, interrupts, device drivers, filesystems |
| Boot process | Firmware, UEFI, bootloaders, kernel loading |
| Databases | SQL, indexes, B+ trees, transactions, concurrency |
| Containers | Namespaces, cgroups, Docker, container networking |

### Additional practical modules

These are guided labs rather than separate formal courses:

- Modern C++: C++11/14/17/20, RAII, smart pointers, templates, STL.
- Linux systems programming: processes, threads, pipes, signals, sockets, epoll.
- Boot process: BIOS/UEFI, GRUB, bootloader-to-kernel handoff.
- Linux kernel: kernel modules, device drivers, memory management.
- Containers: namespaces, cgroups, images, networking, volumes.

### Required project

**Linux-Based Data Acquisition and Monitoring Service**

1. Write the service in C or C++.
2. Implement concurrent data processing.
3. Use bounded queues and synchronization.
4. Store data in a database.
5. Expose a local API.
6. Add logging, error handling, and automated tests.
7. Run as a Linux service.
8. Package the application in Docker.
9. Document memory usage, concurrency, and failure handling.

---

# SPECIALIZATION 3
# EMBEDDED SYSTEMS, MICROCONTROLLERS, AND IoT

## Objective

Develop expertise in:
- Microprocessors and microcontrollers.
- ARM architecture.
- Embedded C and C++.
- Memory-mapped I/O.
- GPIO, ADC, DAC, PWM.
- Timers and interrupts.
- UART, SPI, I2C, CAN.
- RTOS and real-time scheduling.
- Sensors and actuators.
- IoT communication.
- Hardware/software interaction.

| Order | Course name | Platform link | Expected time | Difficulty | Course prerequisite links |
|---|---|---|---|---|---|
| 1 | Nand2Tetris Part I — Hardware | [Nand2Tetris](https://www.nand2tetris.org/) / [Coursera](https://www.coursera.org/learn/build-a-computer/) | 5–7 weeks | Intermediate | [CS50x](https://cs50.harvard.edu/x/). Shared with Specialization 2; do not repeat. |
| 2 | Nand2Tetris Part II — Software | [Nand2Tetris](https://www.nand2tetris.org/) / [Coursera](https://www.coursera.org/learn/nand2tetris2/) | 5–7 weeks | Intermediate | [Nand2Tetris Part I](https://www.coursera.org/learn/build-a-computer/). Shared with Specialization 2. |
| 3 | Embedded Software and Hardware Architecture | [University of Colorado Boulder — Coursera](https://www.coursera.org/learn/embedded-software-hardware) | 2–4 weeks | Intermediate | [CS50x](https://cs50.harvard.edu/x/), [Nand2Tetris Part I](https://www.coursera.org/learn/build-a-computer/), and basic C programming. |
| 4 | Embedded Systems Essentials with Arm — Get Started with the micro:bit | [Arm Education — edX](https://www.edx.org/school/armeducation) | 3–5 weeks | Beginner–Intermediate | [CS50x](https://cs50.harvard.edu/x/) and [MIT Circuits and Electronics](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/). |
| 5 | Embedded Systems Essentials with Arm — Get Practical with Hardware | [Arm Education — edX](https://www.edx.org/school/armeducation) | 4–6 weeks | Intermediate | [Get Started with the micro:bit](https://www.edx.org/school/armeducation), [Embedded Software and Hardware Architecture](https://www.coursera.org/learn/embedded-software-hardware), and [MIT Circuits and Electronics](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/). |
| 6 | Introduction to Microprocessors | [Arm Education — edX](https://www.edx.org/school/armeducation) | 4–6 weeks | Intermediate | [Nand2Tetris Part I](https://www.coursera.org/learn/build-a-computer/) and [Embedded Software and Hardware Architecture](https://www.coursera.org/learn/embedded-software-hardware). |
| 7 | Build Your First Internet of Things Application on Arm | [Arm Education — edX](https://www.edx.org/school/armeducation) | 3–5 weeks | Intermediate | [Get Practical with Hardware](https://www.edx.org/school/armeducation) and [Networking Basics](https://www.netacad.com/courses/networking-basics/how-routers-work). |
| 8 | Real-Time Embedded Systems — Advanced Study | [University of Colorado Boulder — Coursera](https://www.coursera.org/specializations/real-time-embedded-systems) | 8–12 weeks | Advanced | [Embedded Software and Hardware Architecture](https://www.coursera.org/learn/embedded-software-hardware), [Operating System Engineering](https://pdos.csail.mit.edu/6.1810/2026/), and [Feedback Control Systems](https://ocw.mit.edu/courses/2-14-analysis-and-design-of-feedback-control-systems-spring-2014/). |

### Core topics to master

| Subject | Required concepts |
|---|---|
| Microcontrollers | CPU, registers, memory map, peripherals |
| Embedded programming | C, pointers, bitwise operations, volatile |
| GPIO | Digital input/output, pull-up and pull-down resistors |
| Analog interfaces | ADC, DAC, sampling |
| Timers | Counters, PWM, capture and compare |
| Interrupts | Interrupt vectors, ISR, priorities |
| Communication | UART, SPI, I2C, CAN |
| Memory | Flash, SRAM, stack, heap |
| Real-time systems | Scheduling, deadlines, latency, jitter |
| RTOS | Tasks, queues, semaphores, mutexes |
| IoT | MQTT, device communication, cloud integration |

### Required project

**Real-Time Environmental Monitoring System**

1. Interface multiple sensors.
2. Read sensors through I2C or SPI.
3. Use interrupts and timers.
4. Implement task scheduling.
5. Handle communication failures.
6. Transmit sensor readings using MQTT or another suitable protocol.
7. Build a Linux-based data collection service.
8. Document timing constraints and memory utilization.

---

# SPECIALIZATION 4
# COMPUTER NETWORKS AND CYBERSECURITY

## Objective

Develop a strong foundation in:
- Computer networking.
- Ethernet and wireless networks.
- IPv4 and IPv6.
- Subnetting.
- Routing and switching.
- TCP and UDP.
- DNS and DHCP.
- VLANs and network segmentation.
- Network troubleshooting.
- Cybersecurity fundamentals.
- Endpoint security.
- Network defense.
- Linux networking.
- Security monitoring.
- Secure IoT communication.

Cisco Networking Academy is the primary learning platform for this specialization.

## A. Networking Foundations — Cisco Networking Academy

| Order | Course name | Platform link | Expected time | Difficulty | Course prerequisite links |
|---|---|---|---|---|---|
| 1 | Getting Started with Cisco Packet Tracer | [Cisco Networking Academy](https://www.netacad.com/courses/getting-started-cisco-packet-tracer/1000) | 2 hours | Beginner | None. |
| 2 | Networking Basics | [Cisco Networking Academy](https://www.netacad.com/courses/networking-basics/how-routers-work) | 22 hours | Beginner | [Getting Started with Packet Tracer](https://www.netacad.com/courses/getting-started-cisco-packet-tracer/1000). |
| 3 | Networking Devices and Initial Configuration | [Cisco Networking Academy](https://www.netacad.com/courses/networking-devices-and-initial-configuration) | 12–16 hours estimated | Beginner–Intermediate | [Networking Basics](https://www.netacad.com/courses/networking-basics/how-routers-work). |
| 4 | Network Addressing and Basic Troubleshooting | [Cisco Networking Academy](https://www.netacad.com/courses/network-addressing-and-basic-troubleshooting) | 14 hours | Beginner–Intermediate | [Networking Basics](https://www.netacad.com/courses/networking-basics/how-routers-work) and [Networking Devices and Initial Configuration](https://www.netacad.com/courses/networking-devices-and-initial-configuration). |
| 5 | Exploring Networking with Cisco Packet Tracer | [Cisco Networking Academy](https://www.netacad.com/courses/exploring-networking-cisco-packet-tracer) | 3 hours | Beginner–Intermediate | [Getting Started with Packet Tracer](https://www.netacad.com/courses/getting-started-cisco-packet-tracer/1000) and [Networking Basics](https://www.netacad.com/courses/networking-basics/how-routers-work). |

## B. Advanced Networking — Cisco CCNA Pathway

| Order | Course name | Platform link | Expected time | Difficulty | Course prerequisite links |
|---|---|---|---|---|---|
| 6 | CCNA: Introduction to Networks | [Cisco Networking Academy](https://www.netacad.com/) | Approximately 70 hours | Intermediate | Courses 1–5 above. |
| 7 | CCNA: Switching, Routing, and Wireless Essentials | [Cisco Networking Academy](https://www.netacad.com/) | Approximately 70 hours | Intermediate–Advanced | [CCNA: Introduction to Networks](https://www.netacad.com/). |
| 8 | CCNA: Enterprise Networking, Security, and Automation | [Cisco Networking Academy](https://www.netacad.com/) | Approximately 70 hours | Advanced | [CCNA: Switching, Routing, and Wireless Essentials](https://www.netacad.com/). |

**Important:** The CCNA sequence is commonly delivered through instructor-led academies. Confirm course availability and enrollment requirements before scheduling it. It is an advanced extension, not a mandatory prerequisite for the cybersecurity courses below.

## C. Cybersecurity Foundations — Cisco Networking Academy

| Order | Course name | Platform link | Expected time | Difficulty | Course prerequisite links |
|---|---|---|---|---|---|
| 9 | Introduction to Cybersecurity | [Cisco Networking Academy](https://www.netacad.com/courses/introduction-to-cybersecurity) | 6 hours | Beginner | None formally required. Preferably complete [Networking Basics](https://www.netacad.com/courses/networking-basics/how-routers-work) first. |
| 10 | Endpoint Security | [Cisco Networking Academy](https://www.netacad.com/courses/endpoint-security) | 27 hours | Beginner–Intermediate | [Introduction to Cybersecurity](https://www.netacad.com/courses/introduction-to-cybersecurity) and [Networking Basics](https://www.netacad.com/courses/networking-basics/how-routers-work). |
| 11 | Cyber Threat Management | [Cisco Networking Academy](https://www.netacad.com/courses/cyber-threat-management) | 16 hours | Beginner–Intermediate | [Introduction to Cybersecurity](https://www.netacad.com/courses/introduction-to-cybersecurity) and [Endpoint Security](https://www.netacad.com/courses/endpoint-security). |

## D. Network Defense and Security Operations

| Order | Course name | Platform link | Expected time | Difficulty | Course prerequisite links |
|---|---|---|---|---|---|
| 12 | Network Defense | [Cisco Networking Academy](https://www.netacad.com/trainings/network-defense) | 27 hours | Intermediate | [Networking Devices and Initial Configuration](https://www.netacad.com/courses/networking-devices-and-initial-configuration), [Endpoint Security](https://www.netacad.com/courses/endpoint-security), and [Cyber Threat Management](https://www.netacad.com/courses/cyber-threat-management). |
| 13 | SOC Essentials: Investigating with Splunk | [Cisco Networking Academy](https://www.netacad.com/courses/soc-essentials-investigating-with-splunk) | 3 hours | Intermediate | [Introduction to Cybersecurity](https://www.netacad.com/courses/introduction-to-cybersecurity), [Endpoint Security](https://www.netacad.com/courses/endpoint-security), and [Cyber Threat Management](https://www.netacad.com/courses/cyber-threat-management). |

**Availability note:** Network Defense may require an instructor-led academy offering. Treat it as a planned advanced course rather than assuming self-paced enrollment is available.

## E. Linux and Network Programming

| Order | Course name | Platform link | Expected time | Difficulty | Course prerequisite links |
|---|---|---|---|---|---|
| 14 | Linux Essentials | [Cisco Networking Academy](https://www.netacad.com/courses/linux-essentials/operacijskega%20Sistema?courseLang=en-US) | 70 hours | Intermediate | [CS50x](https://cs50.harvard.edu/x/). No prior Linux experience is required. |
| 15 | Linux Network Programming — Guided Practical Study | [Linux man-pages](https://www.kernel.org/doc/man-pages/) and [Linux Kernel Networking Documentation](https://docs.kernel.org/networking/) | 4–6 weeks | Intermediate–Advanced | [CS50x](https://cs50.harvard.edu/x/), [Networking Basics](https://www.netacad.com/courses/networking-basics/how-routers-work), and [Linux Essentials](https://www.netacad.com/courses/linux-essentials/operacijskega%20Sistema?courseLang=en-US). |

### Core topics to master

| Subject | Required concepts |
|---|---|
| Networking fundamentals | LAN, WAN, Ethernet, wireless, network topologies |
| Network models | OSI and TCP/IP models |
| Addressing | IPv4, IPv6, subnetting, CIDR |
| Transport | TCP, UDP, ports, sockets |
| Network services | DNS, DHCP, HTTP, HTTPS |
| Routing | Routing tables, static routing, dynamic routing |
| Switching | VLANs, trunks, STP, EtherChannel |
| Wireless | Wi-Fi standards, WLAN security |
| Security | Threats, vulnerabilities, encryption, authentication |
| Network defense | Firewalls, ACLs, segmentation, monitoring |
| Linux networking | Sockets, routing, interfaces, packet capture |
| Security operations | Logs, alerts, incident response, threat analysis |

### Required project

**Simulated Enterprise Network and Cybersecurity Lab**

1. Design a multi-subnet network.
2. Configure routers and switches in Packet Tracer.
3. Implement IPv4 and IPv6 addressing.
4. Configure DHCP and verify DNS.
5. Create separate VLANs for users, servers, and IoT devices.
6. Configure routing and access control.
7. Document a threat model.
8. Inspect network traffic and diagnose faults.
9. Prepare an incident report.
10. Build a TCP client-server program on Linux.
11. Connect an IoT device or simulator to the network.
12. Document how credentials, communication, and device access are protected.

### Recommended completion strategy

**Core path:**
- Courses 1–5
- Courses 9–11
- Linux networking practical work
- Enterprise Network project

**Advanced networking:**
- Courses 6–8 (CCNA sequence)

**Advanced cybersecurity:**
- Courses 12–13
- Additional security lab work

This structure prevents the networking specialization from becoming too large before its fundamentals are established.

---

# SPECIALIZATION 5
# ROBOTICS, COMPUTER VISION, AND AUTONOMOUS SYSTEMS

## Objective

Develop knowledge of:
- Robot kinematics and dynamics.
- Coordinate transformations.
- Motion planning.
- Robot control.
- Computer vision.
- Image processing.
- Machine learning.
- Deep learning.
- Object detection and tracking.
- Sensor fusion.
- Localization and mapping.
- Autonomous navigation.

| Order | Course name | Platform link | Expected time | Difficulty | Course prerequisite links |
|---|---|---|---|---|---|
| 1 | Modern Robotics | [Northwestern University](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) / [Coursera Specialization](https://www.coursera.org/specializations/modernrobotics) | 12–20 weeks for focused study | Intermediate–Advanced | [Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), [Differential Equations](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/), [CS50x](https://cs50.harvard.edu/x/), and [Feedback Control Systems](https://ocw.mit.edu/courses/2-14-analysis-and-design-of-feedback-control-systems-spring-2014/). |
| 2 | Introduction to Computer Vision and Image Processing | [IBM — Coursera](https://www.coursera.org/learn/introduction-computer-vision-watson-opencv/) | 2–4 weeks | Intermediate | [CS50x](https://cs50.harvard.edu/x/). Basic Python programming is recommended. |
| 3 | Practical Deep Learning for Coders | [fast.ai](https://course.fast.ai/) | 6–10 weeks | Intermediate–Advanced | [CS50x](https://cs50.harvard.edu/x/) and [Introduction to Computer Vision](https://www.coursera.org/learn/introduction-computer-vision-watson-opencv/). |
| 4 | Sensor Fusion and Autonomous Robot Integration — Guided Study | [Modern Robotics](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) and [MIT Signals and Systems](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/) | 4–6 weeks | Advanced | [Modern Robotics](https://hades.mech.northwestern.edu/index.php/Modern_Robotics), [Signals and Systems](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/), [Digital Control Systems](https://ocw.mit.edu/courses/2-171-analysis-and-design-of-digital-control-systems-fall-2006/), and [Computer Vision](https://www.coursera.org/learn/introduction-computer-vision-watson-opencv/). |

### Core topics to master

| Subject | Required concepts |
|---|---|
| Robot mathematics | Coordinate frames, transformations, rotation matrices |
| Kinematics | Forward and inverse kinematics |
| Dynamics | Forces, torques, robot equations of motion |
| Motion planning | Trajectories, path planning, collision avoidance |
| Control | PID, feedback, trajectory tracking |
| Computer vision | Image filtering, edge detection, feature extraction |
| Deep learning | Neural networks, CNNs, object detection |
| Sensor fusion | IMU, encoders, cameras, odometry |
| Localization | Position estimation, uncertainty, filtering |
| Autonomous navigation | Obstacle detection, mapping, path planning |

### Required project

**Autonomous Mobile Robot Simulation**

1. Create a simulated mobile robot.
2. Implement trajectory tracking.
3. Use a camera to detect obstacles.
4. Implement odometry.
5. Integrate simulated IMU measurements.
6. Implement a basic sensor-fusion algorithm.
7. Implement obstacle avoidance.
8. Compare estimated and actual position.
9. Evaluate navigation under disturbances.
10. Document the complete system architecture.

---

# CROSS-SPECIALIZATION INTEGRATION PROJECTS

These projects connect the five specializations and should be completed after their relevant foundations.

| Project | Specializations integrated | Expected time |
|---|---|---|
| Closed-loop DC motor controller | Electronics, control systems, embedded systems | 3–4 weeks |
| Networked sensor platform | Embedded systems, computer networks, Linux, databases, cybersecurity | 3–4 weeks |
| Autonomous mobile robot | Robotics, computer vision, sensor fusion, electronics, control | 4–6 weeks |

---

# SUGGESTED EXECUTION ORDER

| Phase | Learning focus | Main courses |
|---|---|---|
| Phase 1 | Programming and mathematics | CS50x, calculus, linear algebra |
| Phase 2 | Computer architecture | Nand2Tetris Part I and II, MIT 6.004 |
| Phase 3 | Electronics | MIT 6.002, Georgia Tech Electronics |
| Phase 4 | Algorithms and systems | MIT 6.042J, MIT 6.006, MIT 6.1810 |
| Phase 5 | Signals and control | MIT 18.03SC, MIT 6.003, MIT 2.14 |
| Phase 6 | Embedded systems | Colorado Boulder Embedded Software, Arm courses |
| Phase 7 | Networking and cybersecurity | Cisco Networking Academy core sequence |
| Phase 8 | Databases and Linux | CMU 15-445, Linux systems programming |
| Phase 9 | Robotics and computer vision | Modern Robotics, OpenCV, fast.ai |
| Phase 10 | Advanced integration | Digital control, sensor fusion, final projects |

---

# CERTIFICATION AND COST STRATEGY

| Provider | Recommended approach |
|---|---|
| Harvard CS50 | Complete the assignments and final project for the free CS50 certificate. |
| MIT OCW | Use the free learning materials, problem sets, and exams. A normal OCW completion certificate is generally not provided. |
| Nand2Tetris | Use the free official course materials and projects. |
| Coursera | Audit where available; purchase certificates selectively. Check current enrollment terms. |
| edX | Audit eligible Arm courses; purchase verified certificates only if useful. |
| Cisco Networking Academy | Prioritize free courses and their digital badges. |
| fast.ai | Free learning materials; focus on projects rather than certificates. |

---

# FINAL GUIDELINES

1. Complete the prerequisite courses before advanced courses.
2. Do not repeat shared foundations.
3. Complete assignments and labs instead of merely watching lectures.
4. Maintain a GitHub repository for code, simulations, reports, and projects.
5. Document every practical project with diagrams, measurements, tests, and design decisions.
6. Treat certificates as supplementary evidence, not as a substitute for technical competence.
7. Verify course availability and pricing before enrolling.
8. Do not assume an archived course is actively supported.
9. Prioritize practical implementation over collecting certificates.
10. Complete the core courses and integration projects before adding optional advanced material.
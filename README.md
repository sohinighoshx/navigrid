# NaviGrid
### ROS 2-Based Autonomous Navigation & Robotics Simulation

NaviGrid is a robotics development project focused on building a modular foundation for autonomous navigation using the Robot Operating System 2 (ROS 2).

The project explores robot modeling, ROS 2 package architecture, simulation integration, and the software infrastructure required for autonomous ground vehicle development.

The goal is to develop a structured robotics environment that can support navigation, visualization, simulation, and future autonomy capabilities.

---

## Project Overview

NaviGrid is being developed as a robotics software project with an emphasis on modularity, reproducibility, and simulation-driven development.

The project uses ROS 2 as its middleware framework and Ubuntu as its development environment, with robot descriptions and launch configurations forming the foundation for simulation and visualization.

### Objectives

- Establish a modular ROS 2 workspace for robotics development.
- Develop robot descriptions using URDF.
- Configure launch files for robot visualization and simulation.
- Build a reproducible development environment using ROS 2 Jazzy.
- Establish the foundation for future autonomous navigation and path-planning capabilities.

---

## Technology Stack

| Component | Technology |
|---|---|
| Robotics Middleware | ROS 2 Jazzy |
| Operating System | Ubuntu 24.04 LTS |
| Robot Modeling | URDF |
| Visualization | RViz2 |
| Simulation | Gazebo |
| Build System | colcon |
| Programming | Python, XML |
| Development Environment | UTM Virtualization |
| Host Platform | macOS Apple Silicon |

---

## Architecture

The project follows a modular ROS 2 workspace structure.

```text
navigrid/
│
├── src/
│   └── navigrid_description/
│       ├── urdf/
│       ├── launch/
│       ├── package.xml
│       └── CMakeLists.txt
│
└── .gitignore
```

*The directory structure represents the intended package organization; update it to match the current repository contents.*

### Core Components

**Robot Description**

URDF-based modeling for defining the robot's physical structure, links, joints, and coordinate relationships.

**Launch System**

ROS 2 launch configurations for initializing robot description and visualization components.

**Simulation Infrastructure**

A foundation for integrating the robot model with a physics-based simulation environment.

---

## Development Environment

NaviGrid is developed using ROS 2 Jazzy on Ubuntu 24.04 LTS.

The development environment is hosted on an Apple Silicon Mac using UTM virtualization.

This setup provides a Linux-based environment for robotics development while maintaining a macOS host workflow.

---

## Getting Started

### Prerequisites

- Ubuntu 24.04 LTS
- ROS 2 Jazzy
- Python 3
- colcon
- Git

### 1. Clone the repository

```bash
git clone https://github.com/sohinighoshx/navigrid.git

cd navigrid
```

### 2. Source ROS 2

```bash
source /opt/ros/jazzy/setup.bash
```

### 3. Build the workspace

```bash
colcon build
```

### 4. Source the workspace

```bash
source install/setup.bash
```

### 5. Verify the ROS 2 environment

```bash
ros2 pkg list
```

---

## Engineering Challenges

During development, particular attention was given to ROS 2 integration and environment configuration.

One technical challenge involved robot description parsing during launch initialization.

Debugging involved examining launch configurations, package structure, workspace builds, and parameter handling to identify integration issues.

The project also required configuring a consistent robotics development environment across macOS ARM virtualization and Ubuntu Linux.

---

## Project Status

<sub>Active Development</sub>

| Component | Status |
|---|---|
| ROS 2 workspace setup | Completed |
| Initial ROS 2 implementation | Completed |
| Robot description infrastructure | In development |
| Launch integration | In development |
| Simulation integration | Planned |
| Autonomous path planning | Planned |
| Navigation and obstacle avoidance | Planned |

---

## Future Roadmap

- [ ] Complete robot model and visualization.
- [ ] Integrate Gazebo simulation.
- [ ] Implement autonomous path planning.
- [ ] Integrate ROS 2 Navigation (Nav2).
- [ ] Develop obstacle detection and avoidance.
- [ ] Implement goal-based navigation.
- [ ] Develop a monitoring and visualization interface.
- [ ] Evaluate navigation performance in simulation.

---

## Author

**Sohini Ghosh**

Data Science Student | Robotics & AI Enthusiast

GitHub: [@sohinighoshx](https://github.com/sohinighoshx)

---

## License

This project is currently under development. Licensing details will be added in a future release.

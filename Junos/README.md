# Juniper JNCIA / JNCIS DevOps

## Modern Network Operations

- Automated deployment and configuration
- Rapid, automated, and scalable service provisioning
- Virtualization
- Anaylitics
- Cloud

## Modern Network Trends

- Must keep pace and evolve together
- Network services are frequentyly virtualized
- Networking
    - Is a software project
    - Reduce costs
    - Increases speed and scale of service delivery

## Software Development Models

- **Waterfall**
    - Collect requirements for the new software before software design begins
    - Implement design in code
    - Test and deploy the new software
    - Each development phase begins only after the previous phase is complete
    - Work if you know your requirements very well from the beginning of the process
    - Codebase issue may not be discovered until deployment
    - Considered inflexible and slow

- **Agile**
    - Agile is an umbrella term for multiple softare development
        - [Manifesto for Agile](https://agilemanifesto.org/) Software Development
            - Continuous and reliable software delivery
            - Welcomes change and provides high customer satisfaction
            - Frequent releases
            - Frequent communication between developers and stakeholders
            - Team reflect on ways to become more effective and adjust accordingly
            - Agile processes promote sustainable development
            - Simplicity by maximixing the amount of work not done is essential
        - Agile Values
            - Individuals and interactions over processes and tools
            - Working software over comprehensive documentation
            - Customer collaboration over contract negotitiation
            - Responding to change over rigid plans

## DevOps Principles

- What is **DevOps**?
    - A software or systems development methodology
    - Unifies development, operations, and other teams
        - Enables communication, collaboration, and integration
    - Influenced by lean manugfacturing principles
    - Changes in functionality happen frequently, and improvement move quickly into production
        - Leverage automation and orchestration
        - Easily rollback changes if errors are detected

    ![devops_principles](https://user-images.githubusercontent.com/72455856/220940106-3adaf713-e543-4ac0-a41c-f2379e20add6.png)

## Benefits of DevOps

- Aligns the development and operations team's competing goals
    - Development is focused on creating new features
    - Operations is focused on the stability of existing services
- Enables the development of code in a cotrolled, reliable manner


## Infrastructure as Code (IaC)

- DevOps principles and practices applied to infrastructure
    - Operations provisions and manages network infrastructure using code
        - Enables rapid, consistenct, and scalable deployment of infrastructure
        - Enables development, test, staging, and production environments to be identically configured.
    - IaC Workflow:
        - **Code** --> **Version Control** --> **Code Review** --> **Integrate** --> **Deply**

## **Flow**, **Feedback**, and **Continuous experimentation and learning**

![FFC](https://user-images.githubusercontent.com/72455856/220943643-13599601-fff8-42bd-9457-92d59f23baa4.png)

- **Flow**
    - Consider the entire process
        - From initial request to customer delivery
        - Goal in both manufacturing and software development is to shorten the time to deliver
    - Stop doing things that are going to hurt those in downstream in the production process
    - Common problems include:
        - Poor documentation
        - Sloppy code
        - Implementing new features without sharing with development and IT
    - Do not permit local improvements to degrade the process as whole
    - Always seek to increase rate of flow
    - Avoid technical debt

- **Feedback**
    - Require, encourage, and accept feedback
    - Analyze feedback from each stage
        - Development
        - Deployment
        - Delivery
    - Automate as much feedback as possible
    - *The sooner you get feedback, the sooner you can integrate positive changes into the system*

- **Continuous Experimenting and Learning**
    - Continuous focus on improvement
        - Allocate time for process improvement
        - Find fault with processes not people
        - Reward risk-taking
        - Introduce faults to stress-test the system
    - Continuous Integration (CI)
        - Practice of frequently committing and automatically testing the code
        - For a CI to work, a version control system (VCS) is used
        - Quality, compliance, and security testing are performed at each step of the process
    - Continuous Delivery and Continuous Deployment
        - Continuous Delivery makes sure that the code is ready to deploy at any time
        - Continuous Deployment is a way to automate the code deployment
        - Development, test, state, and production environments are as identical as possible

## Network Reliability Engineering

- Leverages DevOps and automation to ensure reliable network operations
- Focuses on customer satisfaction and service availability
- Networking is inseparable from connected systems and application
- Enhances failure as a way to ensure that the same error does not happen again
- Relies on proactive testing
- A continuous journey
![netdev](https://user-images.githubusercontent.com/72455856/220960418-ce522ce9-e0c2-4a8e-a521-42ad72a51cb0.png)

## Network DevOps

- The application of DevOps philosophies, principles, and behaviors to network operations
- Put in practice by network reliability engineers
- Network DevOps pipeline reduces the time between design changes and production deployment
- NetDevOps Pipeline:
    - **Design Change** -> **Commit Change to VCS** -> **Feedback and Peer Review** -> **Automated Testing** -> **Automated Deployment**

## Junos Automation Tools

- On-Box Junos Scripts
    - Extensible Stylesheet Language Transformations
    - Stylesheet Language Alternative Syntax
    - Python

- Types of on-box scripts
    - Commit scripts
    - Operation scripts
    - Event scripts

- Automation Management Systems
    - Scalability to manage multiple devices
    - Provide a declarative way to program your network
        - Define the desired network state and let automation do the work
        - No low-level coding required
    - Supports some type of configuration templating
        - Renders the templates to create the actual configuration
    - Operational state collections are available
    - Perform maintenance tasks
    - Act based on device events
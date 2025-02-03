# Docker ... but only a little bit

## What even is it?

### Python uses virtual environments

- Isolate dependencies to just that project file
  - One app uses Flask, other app uses Django
  - No need for Flask dev team to have Django installed

### Docker is like a Python environment, except for your **_`entire OS`_**

- Windows vs Mac vs Linux? Who cares!
- Setup individual environment variables? No thanks!
- Version differences? As if!

### From least to greatest "control" and complexity

- Virtual Environment => Docker Container => Virtual Machine
  - Docker is in the Goldilocks zone!

## Three main parts

### Dockerfile

- Code that tells docker how to build the image
  - Step by step instructions for setting up your application

### Image

- A snapshot of your application
  - This includes your OS and all dependencies
- Used to create containers

### Container

Where your application actually runs

- **Isolated:** They do not interact with your local filesystem/OS or other containers
- **Ephemeral:** They can be deleted & recreated easily without worry
- **Lightweight:** They are single-purpose and contain only what they need for that purpose
- **Reproducible:** We can rebuild the same container over & over with a single command


### [Great video to get started](https://www.youtube.com/watch?v=gAkwW2tuIqE)

### [Work through Docker's official intro](https://docs.docker.com/get-started/introduction/)

### [Learn Docker's core concepts](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)

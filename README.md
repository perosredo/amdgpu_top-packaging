# amdgpu_top COPR Packaging

RPM packaging for [amdgpu_top](https://github.com/Umio-Yasuno/amdgpu_top) - AMD GPU monitoring tool

## Supported Platforms
- EPEL 10 (x86_64)

## Updates
A daily GitHub Action checks for new upstream releases, bumps `amdgpu_top.spec`,
and triggers a COPR build via webhook. Run it manually from the Actions tab
("Force build" rebuilds without a version change).

## COPR Repository
https://copr.fedorainfracloud.org/coprs/perosredo/amdgpu_top/

## Installation
```bash
# Enable COPR repo
sudo dnf copr enable perosredo/amdgpu_top

# Install package
sudo dnf install amdgpu_top
```

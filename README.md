# amdgpu_top COPR Packaging

RPM packaging for amdgpu_top - AMD GPU monitoring tool

## Supported Platforms
- Fedora 42 (x86_64)
- EPEL 10 (x86_64)

## Quick Build
```bash
# Build from GitHub release
make copr-build

# Check build status  
make copr-status
```

## COPR Repository
https://copr.fedorainfracloud.org/coprs/perosredo/amdgpu_top/

## Installation
```bash
# Enable COPR repo
sudo dnf copr enable perosredo/amdgpu_top

# Install package
sudo dnf install amdgpu_top
```
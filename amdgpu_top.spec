Name:           amdgpu_top
Version:        0.10.5
Release:        1%{?dist}
Summary:        Tool to displays AMDGPU usage and performance counters

License:        MIT
URL:            https://github.com/Umio-Yasuno/amdgpu_top
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  x86_64

BuildRequires:  rust >= 1.70
BuildRequires:  cargo
BuildRequires:  libdrm-devel >= 2.4.110
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libdrm_amdgpu)
BuildRequires:  gcc

Requires:       libdrm >= 2.4.110

%description
amdgpu_top is a tool that displays AMD GPU utilization, similar to nvidia-smi
or intel_gpu_top. The tool displays information gathered from performance 
counters (GRBM, GRBM2), sensors, fdinfo, gpu_metrics and AMDGPU driver.

Features:
- Simple TUI mode (like nvidia-smi, rocm-smi)
- Full TUI mode with detailed monitoring
- GUI mode with graphical interface
- JSON output for automation/scripting
- Process monitoring and memory usage tracking
- Performance counter access
- GPU metrics and sensor data

%prep
%autosetup -n %{name}-%{version}

%build
cargo build --release --locked

%install
install -Dm755 target/release/amdgpu_top %{buildroot}%{_bindir}/amdgpu_top

# Install man page if it exists
if [ -f docs/amdgpu_top.1 ]; then
    install -Dm644 docs/amdgpu_top.1 %{buildroot}%{_mandir}/man1/amdgpu_top.1
fi

%files
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/amdgpu_top
%{_mandir}/man1/amdgpu_top.1*

%changelog
* Mon Aug 19 2025 ps <ps@k8p> - 0.10.5-1
- Initial COPR package for Fedora 42 and EPEL 10
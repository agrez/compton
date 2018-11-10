%global     commit b7f43ee67a1d2d08239a2eb67b7f50fe51a592a8
%global     commit_short %(c=%{commit}; echo ${c:0:7})

Name:		compton
Version:	0.1
Release:	3.%{commit_short}%{?dist}
Summary:	Compositor for X
License:	MIT
URL:		https://github.com/chjj/compton
Source0:	https://github.com/chjj/compton/archive/%{commit}.tar.gz#/%{name}-%{version}-%{commit_short}.tar.gz
# The patch below fixes the git warning during make and also sets the correct cfflags and ldflags
Patch0:		remove_git_version.patch

BuildRequires:	asciidoc
BuildRequires:	libconfig-devel
BuildRequires:	libdrm-devel
BuildRequires:	mesa-libGL-devel
BuildRequires:	libXrandr-devel
BuildRequires:	libXdamage-devel
BuildRequires:	libXcomposite-devel
BuildRequires:	libXinerama-devel
BuildRequires:	dbus-devel
BuildRequires:	pcre-devel
BuildRequires:	desktop-file-utils

Requires:	xorg-x11-utils

%description
Compton is a standalone lightweight compositor for X, a fork of xcompmgr-dana.


%prep
%autosetup -n %{name}-%{commit}


%build
%{make_build}
make docs


%install
%{make_install}


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/compton.desktop


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-trans
%{_mandir}/man1/compton*.1.*
%{_datadir}/applications/compton.desktop
%{_datadir}/icons/hicolor/*/apps/*


%changelog
* Sat Nov 10 2018 Vaughan <devel at agrez dot net> - 0.1-3.b7f43e
- Rebuild for F29
- Misc spec cleanups

* Tue Feb 14 2017 Vaughan <devel at agrez dot net> - 0.1-2.b7f43e
- Update to git commit: b7f43ee67a1d2d08239a2eb67b7f50fe51a592a8

* Fri Aug 26 2016 Vaughan <devel at agrez dot net> - 0.1-1.2343e4b
- Import package

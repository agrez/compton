%global     commit 2343e4bbd298b35ea5c190c52abd2b0cb9f79a18
%global     commit_short %(c=%{commit}; echo ${c:0:7})

Name:		compton
Version:	0.1
Release:	1.%{commit_short}%{?dist}
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

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-trans
%{_mandir}/man1/compton*.1.*
%{_datadir}/applications/compton.desktop
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Fri Aug 26 2016 Vaughan <devel at agrez dot net> - 0.1-1.2343e4b
- Import package

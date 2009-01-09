%define name freedoom
%define version 0.6.3
%define release %mkrel 1
%define distname %{name}-iwad-%{version}

Summary: Complete independent Doom game
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/freedoom/%{distname}.zip
License: GPL
Group: Games/Arcade
Url: http://freedoom.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Provides: doom-iwad

%description
Freedoom is a project to create a complete, free Doom IWAD
file. Combined with the GPLed Doom source code, it will create a
completely free Doom-based game.

To play it, a game engine such as prboom is required.

%prep
%setup -q -n %{distname}

%build

%install
rm -rf %{buildroot}
install -D doom2.wad %{buildroot}%{_gamesdatadir}/doom/%{name}.wad

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CREDITS ChangeLog NEWS README
%{_gamesdatadir}/doom/%{name}.wad



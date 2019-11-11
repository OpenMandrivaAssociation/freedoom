%define distname %{name}-iwad-%{version}

Summary:	Complete independent Doom game
Name:		  freedoom
Version:	0.12.1
Release:	1
Source0:	 https://github.com/freedoom/freedoom/releases/download/v%{version}/%{name}-%{version}.tar.xz
License:	GPLv2
Group:		Games/Arcade
Url:            http://freedoom.github.io/

BuildArch:      noarch
Provides:       doom-iwad
Requires:       doom-engine

%description
Freedoom is a project to create a complete, free Doom IWAD
file. Combined with the GPLed Doom source code, it will create a
completely free Doom-based game.

To play it, a game engine such as prboom is required.

In order to play it with prboom, install prboom and type:

$ prboom -iwad /usr/share/games/doom/freedoom.wad

%prep
%setup -q -n %{distname}

%build
%install
install -D -m644 %{name}1.wad %{buildroot}%{_gamesdatadir}/doom/%{name}1.wad
install -D -m644 %{name}2.wad %{buildroot}%{_gamesdatadir}/doom/%{name}2.wad

%files
%doc CREDITS.txt README.html NEWS.html freedoom-manual.pdf
%license COPYING.txt
%{_gamesdatadir}/doom/%{name}1.wad
%{_gamesdatadir}/doom/%{name}2.wad




%changelog
* Fri Mar 25 2011 Zombie Ryushu <ryushu@mandriva.org> 0.7-1mdv2011.0
+ Revision: 648448
- Upgrade to 0.7

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.4-2mdv2011.0
+ Revision: 610747
- rebuild

* Sat Mar 06 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.6.4-1mdv2010.1
+ Revision: 514904
- fix license
- clean mixed-use-spaces-and-tabs
- update to 0.6.4

  + Shlomi Fish <shlomif@mandriva.org>
    - Added instructions on how to play

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.6.3-2mdv2010.0
+ Revision: 437589
- rebuild

* Fri Jan 09 2009 Zombie Ryushu <ryushu@mandriva.org> 0.6.3-1mdv2009.1
+ Revision: 327350
- New Version 0.6.3

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.5-3mdv2009.0
+ Revision: 245361
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.5-1mdv2008.1
+ Revision: 136419
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Dec 12 2006 Olivier Blin <oblin@mandriva.com> 0.5-1mdv2007.0
+ Revision: 95949
- initial freedoom release
- Create freedoom


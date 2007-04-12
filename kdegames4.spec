
%define _requires_exceptions devel\(libdns_sd\(.*\)\\|devel\(libdns_sd\)

# remove it when kde4 will be official kde package
%define _prefix /opt/kde4/
%define _libdir %_prefix/%_lib
%define _datadir %_prefix/share/
%define _bindir %_prefix/bin
%define _includedir %_prefix/include/
%define _iconsdir %_datadir/icons/
%define _sysconfdir %_prefix/etc/
%define _docdir %_datadir/doc/

%define branch_date 20070311

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%if %unstable
%define dont_strip 1
%endif


# change compress method to bzip2
%define _source_payload w9.bzdio


%define lib_major 1
%define lib_name_orig libkdegames4
%define lib_name %mklibname kdegames4 %{lib_major}


Name:		kdegames4
Summary:	KDE - Games
Version:    	3.80.3
Release: 	%mkrel 0.%branch_date.3
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPL
Packager:	Mandriva Linux KDE Team <kde@mandriva.com>

URL:		ftp://ftp.kde.org/pub/kde/stable/%version/src/

%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdegames-%version-%branch_date.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdegames-%version.tar.bz2
%endif

Source1:	kfouleggs-16.xpm
Source2:	kfouleggs-32.xpm
Source3:	kfouleggs-48.xpm

Source4:	klickety-16.png
Source5:	klickety-32.png
Source6:	klickety-48.png


Patch2:		kdegames-3.5.0-add-support-avahi.patch


BuildRoot:	%_tmppath/%name-%version-%release-root

Requires:	%lib_name = %epoch:%version-%release



BuildRequires:  XFree86-devel  
BuildRequires:  freetype2-devel 
BuildRequires:  alsa-lib-devel audiofile-devel
BuildRequires:  bzip2-devel jpeg-devel lcms-devel
BuildRequires:  mng-devel png-devel 
BuildRequires:  libz-devel
%define mini_release %mkrel 0.%branch_date.1
BuildRequires: kdelibs4-devel >= %version-%mini_release

BuildRequires:	mesaglu-devel
BuildRequires:	libx11-devel

Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils



%description
Games for the K Desktop Environment.
This is a compilation of various games for KDE project
	- atlantik: Monopoly-like board games
	- kabalone: board game: move 6 pieces from your opponent over the edge
	- kasteroids: shoot at those nasty asteroids
	- katomic: build complex atoms with a minimal amount of moves
	- kbackgammon: play backgammon against a local human player, via a
               game server or against GNU Backgammon (not included)
	- kbattleship: battleship game with built-in game server
	- kblackbox: find atoms in a grid by shooting electrons
	- kfouleggs: a famous japanese game known as puyo-puyo
	- kbounce: claim areas and don't get disturbed
	- kjumpingcube: a tactical game for number-crunchers
	- klines: place 5 equal pieces together, but wait, there are 3 new ones
	- mahjongg: a tile laying patience
	- kmines: the classical mine sweeper
	- kolf: a golf game
	- konquest: conquer the planets of your enemy
	- kpat: several patience card games
	- kpoker: the game of poker
	- kreversi: the old reversi board game, also known as othello
	- ksame: collect pieces of the same color
	- kshisen: patience game where you take away all pieces
	- ksirtet: very known if spelt this backwards
	- ksmiletris: another Tetris-like game
	- ksnake: don't bite yourself, eat apples!
	- ksokoban: move all storage boxes into the cabinet
	- kspaceduel: two player game with shooting spaceships flying around a sun
	- ktron: like ksnake, but without fruits
	- ktuberling: kids game: make your own potato (NO french fries!)
	- kwin4: place 4 pieces in a row
	- libkdegames: KDE game library used by many of these programs
	- lskat: lieutnant skat
	- megami: blackjack card game

%package -n %lib_name-devel
Summary:	Headers files for kdegames
Group:		Development/KDE and Qt
Requires:	%lib_name = %epoch:%version-%release

Provides:   %name-devel = %epoch:%version-%release
Provides:   %lib_name_orig-devel = %epoch:%version-%release
%define mini_release %mkrel 0.%branch_date.1
Requires:	kdelibs4-devel >= %version-%mini_release

%description -n %lib_name-devel
Headers files needed to build applications based on kdegames applications.


%package -n %lib_name
Group:      Graphical desktop/KDE
Summary:    Libraries for kdegame
Provides:   %lib_name_orig = %epoch:%version-%release
%define mini_release %mkrel 0.%branch_date.1
Requires: kdelibs4 >= %version-%mini_release

%description -n %lib_name
Libraries for the K Desktop Environment.


%prep
%setup -q -nkdegames-%version-%branch_date

%build

cd $RPM_BUILD_DIR/kdegames-%version-%branch_date
mkdir build
cd build
export QTDIR=/usr/lib/qt4/
export PATH=$QTDIR/bin:$PATH

cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %use_enable_pie
      -DKDE4_ENABLE_FPIE=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=Debug \
%endif
%if "%{_lib}" != "lib"
      -DLIB_SUFFIX=64 \
%endif
        ../


%make


%install
rm -fr %buildroot

cd $RPM_BUILD_DIR/kdegames-%version-%branch_date/build

# David - 2.2-0.alpha2.3mdk - Don't strip when we are not in final release
%if %unstable
export DONT_STRIP=1
%endif

make install DESTDIR=%buildroot 

mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kasteroids.desktop "More Applications/Games/Arcade" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kbounce.desktop "More Applications/Games/Arcade" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kfouleggs.desktop "More Applications/Games/Arcade" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/klickety.desktop "More Applications/Games/Arcade" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kolf.desktop "More Applications/Games/Arcade" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/ksirtet.desktop "More Applications/Games/Arcade" 
#mandriva-add-xdg-categories.pl kdegames "More Applications/Games/Arcade" %buildroot/%_datadir/applications/kde/ksmiletris.desktop %buildroot/%_menudir/kdegames-ksmiletris
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/ksnake.desktop  "More Applications/Games/Arcade" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kspaceduel.desktop "More Applications/Games/Arcade" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/ktron.desktop "More Applications/Games/Arcade" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/atlantik.desktop "More Applications/Games/Boards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kbackgammon.desktop "More Applications/Games/Boards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kbattleship.desktop "More Applications/Games/Boards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kenolaba.desktop "More Applications/Games/Boards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/KGoldrunner.desktop "More Applications/Games/Arcade" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kblackbox.desktop "More Applications/Games/Boards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kmahjongg.desktop "More Applications/Games/Boards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kreversi.desktop "More Applications/Games/Boards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kshisen.desktop "More Applications/Games/Boards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kwin4.desktop "More Applications/Games/Boards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kpat.desktop "More Applications/Games/Cards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kpoker.desktop "More Applications/Games/Cards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/lskat.desktop "More Applications/Games/Cards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/ktuberling.desktop "More Applications/Games/Cards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/katomic.desktop "More Applications/Games/Strategy" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kjumpingcube.desktop "More Applications/Games/Strategy"
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/klines.desktop  "More Applications/Games/Strategy" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kmines.desktop "More Applications/Games/Strategy" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/konquest.desktop "More Applications/Games/Strategy"
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/ksame.desktop "More Applications/Games/Strategy" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/ksokoban.desktop "More Applications/Games/Strategy" 




install -d %buildroot/%_iconsdir/mini/
install -d %buildroot/%_iconsdir/large/
install -m 644 %SOURCE1 %buildroot/%_iconsdir/mini/kfouleggs.xpm
install -m 644 %SOURCE2 %buildroot/%_iconsdir/kfouleggs.xpm
install -m 644 %SOURCE3 %buildroot/%_iconsdir/large/kfouleggs.xpm

install -m 644 %SOURCE4 %buildroot/%_iconsdir/mini/klickety.png
install -m 644 %SOURCE5 %buildroot/%_iconsdir/klickety.png
install -m 644 %SOURCE6 %buildroot/%_iconsdir/large/klickety.png


%post
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%post -n %lib_name -p /sbin/ldconfig

%postun -n %lib_name -p /sbin/ldconfig

%post -n %lib_name-devel -p /sbin/ldconfig

%postun -n %lib_name-devel -p /sbin/ldconfig

%clean
rm -fr %buildroot

%files 
%defattr(-,root,root)



#
#
%attr(0755,root,root) %_bindir/kbounce
%attr(0755,root,root) %_bindir/kenolaba
%attr(0755,root,root) %_bindir/kasteroids
%attr(0755,root,root) %_bindir/katomic
%attr(0755,root,root) %_bindir/kbackgammon
%attr(0755,root,root) %_bindir/kbattleship
%attr(0755,root,root) %_bindir/kblackbox
%attr(0755,root,root) %_bindir/kfouleggs
%attr(0755,root,root) %_bindir/kjumpingcube
%attr(0755,root,root) %_bindir/klines
%attr(0755,root,root) %_bindir/kmahjongg
%attr(0755,root,root) %_bindir/kmines
%attr(0755,root,root) %_bindir/konquest
%attr(0755,root,root) %_bindir/kpat
%attr(0755,root,root) %_bindir/kpoker
%attr(0755,root,root) %_bindir/kwin4proc
%attr(0755,root,root) %_bindir/kreversi
%attr(0755,root,root) %_bindir/ksame
%attr(0755,root,root) %_bindir/kshisen
%attr(0755,root,root) %_bindir/ksnake
%attr(0755,root,root) %_bindir/ksokoban
%attr(0755,root,root) %_bindir/kspaceduel
%attr(0755,root,root) %_bindir/ktron
%attr(0755,root,root) %_bindir/ktuberling
%attr(0755,root,root) %_bindir/kwin4
%attr(0755,root,root) %_bindir/lskat
%attr(0755,root,root) %_bindir/atlantik
%attr(0755,root,root) %_bindir/klickety
%attr(0755,root,root) %_bindir/kolf
%attr(0755,root,root) %_bindir/kgoldrunner
%attr(0755,root,root) %_bindir/knetwalk

#

#
#
#
#
%dir %_datadir/applications/kde4/
%_datadir/applications/kde4/*.desktop


#
%dir %_datadir/apps/
%dir %_datadir/apps/carddecks/
%dir %_datadir/apps/carddecks/cards-aisleriot/
%_datadir/apps/carddecks/cards-aisleriot/COPYRIGHT
%_datadir/apps/carddecks/cards-aisleriot/*.desktop
%_datadir/apps/carddecks/cards-aisleriot/*.png
#

%dir %_datadir/apps/carddecks/cards-xskat-german/
%_datadir/apps/carddecks/cards-xskat-german/*.png
%_datadir/apps/carddecks/cards-xskat-german/*.desktop
%_datadir/apps/carddecks/cards-xskat-german/COPYRIGHT

%dir %_datadir/apps/carddecks/cards-default/
%_datadir/apps/carddecks/cards-default/*.desktop
%_datadir/apps/carddecks/cards-default/*.png
#
%dir %_datadir/apps/carddecks/cards-dondorf-whist-b/
%_datadir/apps/carddecks/cards-dondorf-whist-b/COPYRIGHT
%_datadir/apps/carddecks/cards-dondorf-whist-b/*.desktop
%_datadir/apps/carddecks/cards-dondorf-whist-b/*.png
#
%dir %_datadir/apps/carddecks/cards-gdkcard-bonded/
%_datadir/apps/carddecks/cards-gdkcard-bonded/COPYRIGHT
%_datadir/apps/carddecks/cards-gdkcard-bonded/*.desktop
%_datadir/apps/carddecks/cards-gdkcard-bonded/*.png
#
%dir %_datadir/apps/carddecks/cards-hard-a-port/
%_datadir/apps/carddecks/cards-hard-a-port/COPYRIGHT
%_datadir/apps/carddecks/cards-hard-a-port/*.desktop
%_datadir/apps/carddecks/cards-hard-a-port/*.png
#
%dir %_datadir/apps/carddecks/cards-konqi-modern/
%_datadir/apps/carddecks/cards-konqi-modern/*.desktop
%_datadir/apps/carddecks/cards-konqi-modern/*.png
#
%dir %_datadir/apps/carddecks/cards-penguins/
%_datadir/apps/carddecks/cards-penguins/COPYRIGHT
%_datadir/apps/carddecks/cards-penguins/*.desktop
%_datadir/apps/carddecks/cards-penguins/*.png
#
%dir %_datadir/apps/carddecks/cards-spaced/
%_datadir/apps/carddecks/cards-spaced/COPYRIGHT
%_datadir/apps/carddecks/cards-spaced/*.desktop
%_datadir/apps/carddecks/cards-spaced/*.png

%dir %_datadir/apps/carddecks/cards-warwick/
%_datadir/apps/carddecks/cards-warwick/*.desktop
%_datadir/apps/carddecks/cards-warwick/*.png
#
%dir %_datadir/apps/carddecks/cards-xskat-french/
%_datadir/apps/carddecks/cards-xskat-french/COPYRIGHT
%_datadir/apps/carddecks/cards-xskat-french/*.desktop
%_datadir/apps/carddecks/cards-xskat-french/*.png
#
%dir %_datadir/apps/carddecks/decks/
%_datadir/apps/carddecks/decks/*.desktop
%_datadir/apps/carddecks/decks/*.png
#
#
%dir %_datadir/apps/kenolaba/
%_datadir/apps/kenolaba/*.rc
%dir %_datadir/apps/kenolaba/pics/
%_datadir/apps/kenolaba/pics/*.xpm

#
%dir %_datadir/apps/kbounce/
%_datadir/apps/kbounce/*.rc
%dir %_datadir/apps/kbounce/pics/
%_datadir/apps/kbounce/pics/*.png
%dir %_datadir/apps/kbounce/sounds/
%_datadir/apps/kbounce/sounds/*.au
%dir %_datadir/apps/kbounce/pics/
%_datadir/apps/kbounce/pics/default_theme.svgz
#
%dir %_datadir/apps/kasteroids/
%_datadir/apps/kasteroids/*.rc
#
%dir %_datadir/apps/kasteroids/sounds/
%_datadir/apps/kasteroids/sounds/*.wav
#
%dir %_datadir/apps/kasteroids/sprites/
%_datadir/apps/kasteroids/sprites/*.png
#
%dir %_datadir/apps/kasteroids/sprites/bits/
%_datadir/apps/kasteroids/sprites/bits/*.png
#
%dir %_datadir/apps/kasteroids/sprites/exhaust/
%_datadir/apps/kasteroids/sprites/exhaust/*.png
#
%dir %_datadir/apps/kasteroids/sprites/missile/
%_datadir/apps/kasteroids/sprites/missile/*.png
#
%dir %_datadir/apps/kasteroids/sprites/powerups/
%_datadir/apps/kasteroids/sprites/powerups/*.png
#
%dir %_datadir/apps/kasteroids/sprites/rock1/
%_datadir/apps/kasteroids/sprites/rock1/*.png
#
%dir %_datadir/apps/kasteroids/sprites/rock2/
%_datadir/apps/kasteroids/sprites/rock2/*.png
#
%dir %_datadir/apps/kasteroids/sprites/rock3/
%_datadir/apps/kasteroids/sprites/rock3/*.png
#
%dir %_datadir/apps/kasteroids/sprites/shield/
%_datadir/apps/kasteroids/sprites/shield/*.png
#
%dir %_datadir/apps/kasteroids/sprites/ship/
%_datadir/apps/kasteroids/sprites/ship/*.png
#
#
%dir %_datadir/apps/katomic/
%_datadir/apps/katomic/*.rc
#
%dir %_datadir/apps/katomic/levels/
%_datadir/apps/katomic/levels/level_*
#
#
#
%dir %_datadir/apps/kbackgammon/
%_datadir/apps/kbackgammon/*rc
#
%dir %_datadir/apps/kbackgammon/pics/
%_datadir/apps/kbackgammon/pics/*.png
%_datadir/apps/kbackgammon/pics/*.xpm
#
%dir %_datadir/apps/kbackgammon/sounds/
%_datadir/apps/kbackgammon/sounds/*.wav
#
#
%dir %_datadir/apps/kbattleship/
%_datadir/apps/kbattleship/*.rc
#
%dir %_datadir/apps/kbattleship/pictures/
%_datadir/apps/kbattleship/pictures/*.png
#
%dir %_datadir/apps/kbattleship/sounds/
%_datadir/apps/kbattleship/sounds/*.ogg
#
#
%dir %_datadir/apps/kblackbox/
%_datadir/apps/kblackbox/*.rc
#
#
#
%dir %_datadir/apps/kdegames/
%dir %_datadir/apps/kdegames/pics/
%_datadir/apps/kdegames/pics/*.png
#
#
%dir %_datadir/apps/kfouleggs/
%_datadir/apps/kfouleggs/*.rc
#
#
%dir %_datadir/apps/kjumpingcube/
%_datadir/apps/kjumpingcube/*.rc
#
#
%dir %_datadir/apps/klines/
%_datadir/apps/klines/*.jpg
%_datadir/apps/klines/*.rc
#
#
%dir %_datadir/apps/kmahjongg/
%_datadir/apps/kmahjongg/*.rc
%dir %_datadir/apps/kmahjongg/pics/
#
#
%dir %_datadir/apps/kmines/
%_datadir/apps/kmines/*.rc
#
#
%dir %_datadir/apps/konquest/
%_datadir/apps/konquest/*.rc
%dir %_datadir/apps/konquest/pics/
%_datadir/apps/konquest/pics/*.png
%_datadir/apps/konquest/pics/*.xpm
#
#
%dir %_datadir/apps/kpat/
%_datadir/apps/kpat/*.rc
#
#
%dir %_datadir/apps/kpoker/
%_datadir/apps/kpoker/*.rc
#
%dir %_datadir/apps/kpoker/sounds/
%_datadir/apps/kpoker/sounds/*.wav
#
#
#
%dir %_datadir/apps/ksame/
%_datadir/apps/ksame/*.rc
#
#
%dir %_datadir/apps/kshisen/
%_datadir/apps/kshisen/*.rc
#
#
%dir %_datadir/apps/ksirtet/
%_datadir/apps/ksirtet/*.rc
#

#
#
%dir %_datadir/apps/ksnake/
%_datadir/apps/ksnake/highScores
%_datadir/apps/ksnake/*.rc
#
%dir %_datadir/apps/ksnake/backgrounds/
%_datadir/apps/ksnake/backgrounds/*.png
#
%dir %_datadir/apps/ksnake/levels/
%_datadir/apps/ksnake/levels/room*
#
%dir %_datadir/apps/ksnake/pics/
%_datadir/apps/ksnake/pics/*.png
#
#
%dir %_datadir/apps/kspaceduel/
%_datadir/apps/kspaceduel/*.rc
#
%dir %_datadir/apps/kspaceduel/icons/
%dir %_datadir/apps/kspaceduel/icons/crystalsvg/
%dir %_datadir/apps/kspaceduel/icons/crystalsvg/16x16/
%dir %_datadir/apps/kspaceduel/icons/crystalsvg/16x16/actions/
%_datadir/apps/kspaceduel/icons/crystalsvg/16x16/actions/*.png
#
%dir %_datadir/apps/kspaceduel/icons/crystalsvg/22x22/
%dir %_datadir/apps/kspaceduel/icons/crystalsvg/22x22/actions/
%_datadir/apps/kspaceduel/icons/crystalsvg/22x22/actions/*.png
#
%dir %_datadir/apps/kspaceduel/icons/crystalsvg/32x32/
%dir %_datadir/apps/kspaceduel/icons/crystalsvg/32x32/actions/
%_datadir/apps/kspaceduel/icons/crystalsvg/32x32/actions/*.png
%dir %_datadir/apps/kspaceduel/icons/locolor/
%dir %_datadir/apps/kspaceduel/icons/locolor/16x16/
%dir %_datadir/apps/kspaceduel/icons/locolor/16x16/actions/
%_datadir/apps/kspaceduel/icons/locolor/16x16/actions/*.png
#
#
%dir %_datadir/apps/kgoldrunner/system/
%_datadir/apps/kgoldrunner/system/*.txt
%_datadir/apps/knetwalk/all.svgz

#
%dir %_datadir/apps/ktron/
%_datadir/apps/ktron/*.rc
#
#
%dir %_datadir/apps/ktuberling/
%_datadir/apps/ktuberling/ktuberlingui.rc
#
%dir %_datadir/apps/ktuberling/museum/
%_datadir/apps/ktuberling/museum/*.tuberling
#
%dir %_datadir/apps/ktuberling/pics/
%_datadir/apps/ktuberling/pics/*.xml 
%_datadir/apps/ktuberling/pics/*.png
#
%dir %_datadir/apps/ktuberling/sounds/
%dir %_datadir/apps/ktuberling/sounds/en/
%_datadir/apps/ktuberling/sounds/en/*.wav
#
#
%dir %_datadir/apps/kwin4/
%_datadir/apps/kwin4/*.rc
#
%_datadir/apps/kblackbox/pics/kblackbox.svgz
%_datadir/apps/kgoldrunner/pics/kgr_1.svg
%_datadir/apps/kmines/themes/kmines_classic.svgz

%_datadir/apps/kspaceduel/sprites/backgr.png

%_datadir/apps/kspaceduel/sprites/default_theme.svgz

%_datadir/apps/kspaceduel/sprites/playerinfo/*.png

%dir %_datadir/apps/kwin4/grafix/
%_datadir/apps/kwin4/grafix/default.rc
%_datadir/apps/kwin4/grafix/default.svg
%_datadir/apps/kwin4/grafix/yellow.rc
%_datadir/apps/kwin4/grafix/yellow.svg
#
#
%dir %_datadir/apps/lskat/
%_datadir/apps/lskat/*.rc
#
%dir %_datadir/apps/lskat/grafix/
%_datadir/apps/lskat/grafix/*.png
#

 



%dir %_datadir/apps/kgoldrunner/
%_datadir/apps/kgoldrunner/*.rc
%dir %_datadir/apps/kgoldrunner/system/
%_datadir/apps/kgoldrunner/system/*.dat

#
%dir %_datadir/apps/atlantik/
%_datadir/apps/atlantik/*.rc

%dir %_datadir/apps/atlantik/themes/
%dir %_datadir/apps/atlantik/themes/default/
%dir %_datadir/apps/atlantik/themes/default/tokens/
%_datadir/apps/atlantik/themes/default/tokens/*.png

%dir %_datadir/apps/atlantik/pics/
%_datadir/apps/atlantik/pics/*.png

%dir %_datadir/apps/atlantik/icons/
%dir %_datadir/apps/atlantik/icons/crystalsvg/
%dir %_datadir/apps/atlantik/icons/crystalsvg/16x16/
%dir %_datadir/apps/atlantik/icons/crystalsvg/16x16/actions/
%_datadir/apps/atlantik/icons/crystalsvg/16x16/actions/*.png

%dir %_datadir/apps/atlantik/icons/crystalsvg/22x22/
%dir %_datadir/apps/atlantik/icons/crystalsvg/22x22/actions/
%_datadir/apps/atlantik/icons/crystalsvg/22x22/actions/*.png

%dir %_datadir/apps/atlantik/icons/crystalsvg/32x32/
%dir %_datadir/apps/atlantik/icons/crystalsvg/32x32/actions/
%_datadir/apps/atlantik/icons/crystalsvg/32x32/actions/*.png

%dir %_datadir/apps/atlantik/icons/locolor/
%dir %_datadir/apps/atlantik/icons/locolor/16x16/
%dir %_datadir/apps/atlantik/icons/locolor/16x16/actions/
%_datadir/apps/atlantik/icons/locolor/16x16/actions/*.png

%dir %_datadir/apps/klickety/
%_datadir/apps/klickety/*.rc

%dir %_datadir/apps/kolf/
%_datadir/apps/kolf/intro
%_datadir/apps/kolf/*.rc
%_datadir/apps/kolf/tutorial.*

%dir %_datadir/apps/kolf/courses/
%_datadir/apps/kolf/courses/*

%dir %_datadir/apps/kolf/pics/
%_datadir/apps/kolf/pics/*.png

%dir %_datadir/apps/kolf/sounds/
%_datadir/apps/kolf/sounds/*.wav


%dir %_datadir/mimelnk/application/
%_datadir/mimelnk/application/*.desktop

%dir %_datadir/services/
%_datadir/services/*.protocol

%dir %_datadir/config/magic
%_datadir/config/magic/*.magic


%_datadir/apps/atlantik/atlantik.notifyrc
%dir %_datadir/apps/carddecks/SVG-cards-2.0/
%_datadir/apps/carddecks/SVG-cards-2.0/*
%dir %_datadir/apps/carddecks/svg-classic/
%_datadir/apps/carddecks/svg-classic/*
%dir %_datadir/apps/carddecks/svg-dondorf/
%_datadir/apps/carddecks/svg-dondorf/*
%dir %_datadir/apps/carddecks/svg-gm-paris/
%_datadir/apps/carddecks/svg-gm-paris/*
%dir %_datadir/apps/carddecks/svg-nicu-ornamental/
%_datadir/apps/carddecks/svg-nicu-ornamental/*
%dir %_datadir/apps/carddecks/svg-nicu-white/
%_datadir/apps/carddecks/svg-nicu-white/*


%dir %_datadir/apps/kasteroids/sprites/bits/
%_datadir/apps/kasteroids/sprites/bits/*
%_datadir/apps/kasteroids/sprites/*
%_datadir/apps/katomic/pics/default_theme.svgz
%_datadir/apps/kbattleship/kbattleship.notifyrc
%_datadir/apps/kfouleggs/kfouleggs.notifyrc
%_datadir/apps/klickety/klickety.notifyrc
%_datadir/apps/kmahjongg/pics/*
%dir %_datadir/apps/kmahjongglib/backgrounds/
%_datadir/apps/kmahjongglib/backgrounds/*
%_datadir/apps/kmahjongglib/tilesets/*
%_datadir/apps/kmines/kmines.notifyrc
%_datadir/apps/knetwalk/knetwalk.notifyrc
%_datadir/apps/kolf/pics/default_theme.svgz
%_datadir/apps/konquest/pics/default_theme.svgz
%_datadir/apps/kpat/backgrounds/background.svg
%_datadir/apps/kpat/pile.svg
%_datadir/apps/kpat/won.svg
%_datadir/apps/kreversi/kreversi.notifyrc
%_datadir/apps/kreversi/kreversiui.rc
%dir %_datadir/apps/kreversi/pics/
%_datadir/apps/kreversi/pics/*.svgz
%dir %_datadir/apps/kreversi/sounds/
%_datadir/apps/kreversi/sounds/*.wav
%_datadir/apps/ksame/pics/default_theme.svgz
%_datadir/apps/ksirtet/ksirtet.notifyrc
%_datadir/apps/ksokoban/ksokobanui.rc


#
%_iconsdir/*.xpm
%_iconsdir/*.png
#
%dir %_iconsdir/mini/
%_iconsdir/mini/*.xpm
%_iconsdir/mini/*.png
#
%dir %_iconsdir/large/
%_iconsdir/large/*.xpm
%_iconsdir/large/*.png
#

%_datadir/apps/zeroconf/*._tcp

%dir %_datadir/apps/knetwalk/
%_datadir/apps/knetwalk/knetwalkui.rc

%dir %_datadir/apps/knetwalk/sounds/
%_datadir/apps/knetwalk/sounds/*.wav

%_iconsdir/crystalsvg/16x16/actions/endturn.png
%_iconsdir/crystalsvg/16x16/actions/highscore.png
%_iconsdir/crystalsvg/16x16/actions/lastmoves.png
%_iconsdir/crystalsvg/16x16/actions/legalmoves.png
%_iconsdir/crystalsvg/16x16/actions/roll.png
%_iconsdir/crystalsvg/22x22/actions/lastmoves.png
%_iconsdir/crystalsvg/22x22/actions/legalmoves.png
%_iconsdir/crystalsvg/22x22/actions/roll.png
%_iconsdir/crystalsvg/32x32/actions/endturn.png
%_iconsdir/crystalsvg/32x32/actions/highscore.png
%_iconsdir/crystalsvg/32x32/actions/lastmoves.png
%_iconsdir/crystalsvg/32x32/actions/legalmoves.png
%_iconsdir/crystalsvg/32x32/actions/roll.png
%_iconsdir/crystalsvg/48x48/actions/lastmoves.png
%_iconsdir/crystalsvg/48x48/actions/legalmoves.png
%_iconsdir/crystalsvg/scalable/actions/lastmoves.svgz
%_iconsdir/crystalsvg/scalable/actions/legalmoves.svgz
%_iconsdir/hicolor/128x128/apps/*.png
%_iconsdir/hicolor/16x16/apps/*.png
%_iconsdir/hicolor/22x22/apps/*.png
%_iconsdir/hicolor/32x32/apps/*.png
%_iconsdir/hicolor/48x48/apps/*.png
%_iconsdir/hicolor/64x64/apps/*.png

%dir %_docdir/HTML/en/atlantik/
%doc %_docdir/HTML/en/atlantik/*.bz2
%doc %_docdir/HTML/en/atlantik/*.docbook
%dir %_docdir/HTML/en/kasteroids/
%doc %_docdir/HTML/en/kasteroids/*.png
%doc %_docdir/HTML/en/kasteroids/*.bz2
%doc %_docdir/HTML/en/kasteroids/*.docbook
%dir %_docdir/HTML/en/katomic/
%doc %_docdir/HTML/en/katomic/*.bz2
%doc %_docdir/HTML/en/katomic/*.docbook
%dir %_docdir/HTML/en/kbackgammon/
%doc %_docdir/HTML/en/kbackgammon/*.png
%doc %_docdir/HTML/en/kbackgammon/*.bz2
%doc %_docdir/HTML/en/kbackgammon/*.docbook
%dir %_docdir/HTML/en/kbattleship/
%doc %_docdir/HTML/en/kbattleship/*.bz2
%doc %_docdir/HTML/en/kbattleship/*.docbook
%dir %_docdir/HTML/en/kblackbox/
%doc %_docdir/HTML/en/kblackbox/*.bz2
%doc %_docdir/HTML/en/kblackbox/*.docbook
%doc %_docdir/HTML/en/kblackbox/*.png
%dir %_docdir/HTML/en/kbounce/
%doc %_docdir/HTML/en/kbounce/*.bz2
%doc %_docdir/HTML/en/kbounce/*.docbook
%doc %_docdir/HTML/en/kbounce/*.png
%dir %_docdir/HTML/en/kenolaba/
%doc %_docdir/HTML/en/kenolaba/*.bz2
%doc %_docdir/HTML/en/kenolaba/*.docbook
%doc %_docdir/HTML/en/kenolaba/*.png
%dir %_docdir/HTML/en/kfouleggs/
%doc %_docdir/HTML/en/kfouleggs/*.png
%doc %_docdir/HTML/en/kfouleggs/*.bz2
%doc %_docdir/HTML/en/kfouleggs/*.docbook
%dir %_docdir/HTML/en/kgoldrunner/
%doc %_docdir/HTML/en/kgoldrunner/*.bz2
%doc %_docdir/HTML/en/kgoldrunner/*.docbook
%doc %_docdir/HTML/en/kgoldrunner/*.png
%dir %_docdir/HTML/en/kjumpingcube/
%doc %_docdir/HTML/en/kjumpingcube/*.bz2
%doc %_docdir/HTML/en/kjumpingcube/*.docbook
%dir %_docdir/HTML/en/klickety/
%doc %_docdir/HTML/en/klickety/*.bz2
%doc %_docdir/HTML/en/klickety/*.docbook
%doc %_docdir/HTML/en/klickety/*.png
%dir %_docdir/HTML/en/klines/
%doc %_docdir/HTML/en/klines/*.bz2
%doc %_docdir/HTML/en/klines/*.docbook
%dir %_docdir/HTML/en/kmahjongg/
%doc %_docdir/HTML/en/kmahjongg/*.png
%doc %_docdir/HTML/en/kmahjongg/*.bz2
%doc %_docdir/HTML/en/kmahjongg/*.docbook
%dir %_docdir/HTML/en/kmines/
%doc %_docdir/HTML/en/kmines/*.bz2
%doc %_docdir/HTML/en/kmines/*.docbook
%doc %_docdir/HTML/en/kmines/*.png
%dir %_docdir/HTML/en/kolf/
%doc %_docdir/HTML/en/kolf/*.bz2
%doc %_docdir/HTML/en/kolf/*.docbook
%dir %_docdir/HTML/en/konquest/
%doc %_docdir/HTML/en/konquest/*.bz2
%doc %_docdir/HTML/en/konquest/*.docbook
%dir %_docdir/HTML/en/kpat/
%doc %_docdir/HTML/en/kpat/*.png
%doc %_docdir/HTML/en/kpat/*.bz2
%doc %_docdir/HTML/en/kpat/*.docbook
%dir %_docdir/HTML/en/kpoker/
%doc %_docdir/HTML/en/kpoker/*.bz2
%doc %_docdir/HTML/en/kpoker/*.docbook
%doc %_docdir/HTML/en/kpoker/*.png
%dir %_docdir/HTML/en/kreversi/
%doc %_docdir/HTML/en/kreversi/*.bz2
%doc %_docdir/HTML/en/kreversi/*.docbook
%doc %_docdir/HTML/en/kreversi/*.png
%dir %_docdir/HTML/en/ksame/
%doc %_docdir/HTML/en/ksame/*.bz2
%doc %_docdir/HTML/en/ksame/*.docbook
%dir %_docdir/HTML/en/kshisen/
%doc %_docdir/HTML/en/kshisen/*.bz2
%doc %_docdir/HTML/en/kshisen/*.docbook
%doc %_docdir/HTML/en/kshisen/*.png
%dir %_docdir/HTML/en/ksirtet/
%doc %_docdir/HTML/en/ksirtet/*.bz2
%doc %_docdir/HTML/en/ksirtet/*.docbook
%dir %_docdir/HTML/en/ksnake/
%doc %_docdir/HTML/en/ksnake/*.bz2
%doc %_docdir/HTML/en/ksnake/*.docbook
%dir %_docdir/HTML/en/ksokoban/
%doc %_docdir/HTML/en/ksokoban/*.bz2
%doc %_docdir/HTML/en/ksokoban/*.docbook
%dir %_docdir/HTML/en/kspaceduel/
%doc %_docdir/HTML/en/kspaceduel/*.bz2
%doc %_docdir/HTML/en/kspaceduel/*.docbook
%doc %_docdir/HTML/en/kspaceduel/*.png
%dir %_docdir/HTML/en/ktron/
%doc %_docdir/HTML/en/ktron/*.bz2
%doc %_docdir/HTML/en/ktron/*.docbook
%dir %_docdir/HTML/en/ktuberling/
%doc %_docdir/HTML/en/ktuberling/*.png
%doc %_docdir/HTML/en/ktuberling/*.bz2
%doc %_docdir/HTML/en/ktuberling/*.docbook
%dir %_docdir/HTML/en/kwin4/
%doc %_docdir/HTML/en/kwin4/*.bz2
%doc %_docdir/HTML/en/kwin4/*.docbook




%files -n %lib_name
%defattr(-,root,root,-)
#
#
%_libdir/libkdegames.so.*
#
%_libdir/libatlantic.so.*
%_libdir/libatlantikclient.so.*
%_libdir/libatlantikui.so.*
#
%_libdir/kde4/kio_atlantik.so

%_libdir/libkmahjongglib.so.*
%_libdir/libkolflib.so.*
%_libdir/libksirtetlib.so.*


%files -n %lib_name-devel
%defattr(-,root,root,-)

%_datadir/apps/cmake/modules/FindLibKDEGames.cmake
%_datadir/apps/cmake/modules/GGZ.cmake

%_libdir/libkmahjongglib.so
%_libdir/libkolflib.so
%_libdir/libksirtetlib.so

%_includedir/*.h

%dir %_includedir/kgame/
%_includedir/kgame/*.h

%dir %_includedir/atlantic/
%_includedir/atlantic/*.h

%dir %_includedir/atlantik/
%dir %_includedir/atlantik/ui
%_includedir/atlantik/ui/*.h



%_libdir/libkdegames.so
%_libdir/libatlantic.so
%_libdir/libatlantikclient.so
%_libdir/libatlantikui.so

%dir %_datadir/config.kcfg/
%_datadir/config.kcfg/*.kcfg




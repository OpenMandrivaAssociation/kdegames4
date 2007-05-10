
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

%define branch_date 20070502

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
Version:	3.90.1
Release: 	%mkrel 0.%branch_date.1
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
	- katomic: build complex atoms with a minimal amount of moves
	- kbackgammon: play backgammon against a local human player, via a
               game server or against GNU Backgammon (not included)
	- kbattleship: battleship game with built-in game server
	- kblackbox: find atoms in a grid by shooting electrons
	- kbounce: claim areas and don't get disturbed
	- klines: place 5 equal pieces together, but wait, there are 3 new ones
	- mahjongg: a tile laying patience
	- kmines: the classical mine sweeper
	- kolf: a golf game
	- konquest: conquer the planets of your enemy
	- kpat: several patience card games
	- kreversi: the old reversi board game, also known as othello
	- ksame: collect pieces of the same color
	- kshisen: patience game where you take away all pieces
	- ksirtet: very known if spelt this backwards
	- ksmiletris: another Tetris-like game
	- kspaceduel: two player game with shooting spaceships flying around a sun
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

mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kbounce.desktop "More Applications/Games/Arcade" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kolf.desktop "More Applications/Games/Arcade" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/ksirtet.desktop "More Applications/Games/Arcade" 
#mandriva-add-xdg-categories.pl kdegames "More Applications/Games/Arcade" %buildroot/%_datadir/applications/kde/ksmiletris.desktop %buildroot/%_menudir/kdegames-ksmiletris
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kspaceduel.desktop "More Applications/Games/Arcade" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kbackgammon.desktop "More Applications/Games/Boards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kbattleship.desktop "More Applications/Games/Boards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/KGoldrunner.desktop "More Applications/Games/Arcade" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kblackbox.desktop "More Applications/Games/Boards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kmahjongg.desktop "More Applications/Games/Boards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kreversi.desktop "More Applications/Games/Boards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kshisen.desktop "More Applications/Games/Boards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kwin4.desktop "More Applications/Games/Boards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kpat.desktop "More Applications/Games/Cards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/lskat.desktop "More Applications/Games/Cards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/ktuberling.desktop "More Applications/Games/Cards" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/katomic.desktop "More Applications/Games/Strategy" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/klines.desktop  "More Applications/Games/Strategy" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kmines.desktop "More Applications/Games/Strategy" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/konquest.desktop "More Applications/Games/Strategy"
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/ksame.desktop "More Applications/Games/Strategy" 




install -d %buildroot/%_iconsdir/mini/
install -d %buildroot/%_iconsdir/large/

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
%attr(0755,root,root) %_bindir/katomic
%attr(0755,root,root) %_bindir/kbackgammon
%attr(0755,root,root) %_bindir/kbattleship
%attr(0755,root,root) %_bindir/kblackbox
%attr(0755,root,root) %_bindir/klines
%attr(0755,root,root) %_bindir/kmahjongg
%attr(0755,root,root) %_bindir/kmines
%attr(0755,root,root) %_bindir/konquest
%attr(0755,root,root) %_bindir/kpat
%attr(0755,root,root) %_bindir/kwin4proc
%attr(0755,root,root) %_bindir/kreversi
%attr(0755,root,root) %_bindir/ksame
%attr(0755,root,root) %_bindir/kshisen
%attr(0755,root,root) %_bindir/kspaceduel
%attr(0755,root,root) %_bindir/ktuberling
%attr(0755,root,root) %_bindir/kwin4
%attr(0755,root,root) %_bindir/lskat
%attr(0755,root,root) %_bindir/kolf
%attr(0755,root,root) %_bindir/kgoldrunner
%attr(0755,root,root) %_bindir/knetwalk

#

%dir %_datadir/applications/kde4/
%_datadir/applications/kde4/*.desktop


%_bindir/kiriki
%_bindir/ksquares


%_datadir/apps/kbattleship/pictures/default_theme.svgz

%_datadir/apps/kgoldrunner/pics/README
%_datadir/apps/kgoldrunner/pics/*.desktop
%_datadir/apps/kgoldrunner/pics/*.svg

%dir %_datadir/apps/kiriki/
%dir %_datadir/apps/kiriki/images/
%_datadir/apps/kiriki/images/*.png
%_datadir/apps/kiriki/kirikiui.rc

%_datadir/apps/klines/klines.svgz

%_datadir/apps/kmines/themes/kmines_oxygen.svgz
%_datadir/apps/ksquares/ksquaresui.rc


%_iconsdir/hicolor/scalable/actions/*.svgz

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
%dir %_datadir/apps/klines/
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
#
%dir %_datadir/apps/kspaceduel/
%_datadir/apps/kspaceduel/*.rc
#
%dir %_datadir/apps/kspaceduel/icons/
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
%dir %_datadir/apps/ktuberling/
%_datadir/apps/ktuberling/ktuberlingui.rc
#
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

%dir %_datadir/apps/kgoldrunner/
%_datadir/apps/kgoldrunner/*.rc
%dir %_datadir/apps/kgoldrunner/system/
%_datadir/apps/kgoldrunner/system/*.dat

#
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


%_datadir/apps/katomic/pics/default_theme.svgz
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


#

%dir %_datadir/apps/knetwalk/
%_datadir/apps/knetwalk/knetwalkui.rc

%dir %_datadir/apps/knetwalk/sounds/
%_datadir/apps/knetwalk/sounds/*.wav

%_iconsdir/hicolor/128x128/apps/*.png
%_iconsdir/hicolor/16x16/apps/*.png
%_iconsdir/hicolor/22x22/apps/*.png
%_iconsdir/hicolor/32x32/apps/*.png
%_iconsdir/hicolor/48x48/apps/*.png
%_iconsdir/hicolor/64x64/apps/*.png


%_datadir/apps/ktuberling/pics/default_theme.svg
%_datadir/apps/ktuberling/pics/layout.xml
%_datadir/apps/ktuberling/pics/potato-game.svg
%_datadir/config/kmines.knsrc

%_datadir/apps/carddecks/decks/deck25_dondorf.svgz
%_datadir/apps/carddecks/decks/deck26_ornamental.svg
%_datadir/apps/carddecks/decks/deck27_classic.svgz

%_datadir/apps/klines/default.desktop

%_datadir/apps/kmines/themes/classic.desktop
%_datadir/apps/kmines/themes/classic_preview.png
%_datadir/apps/kmines/themes/default.desktop
%_datadir/apps/kmines/themes/default_preview.png
%_datadir/apps/kspaceduel/icons/oxygen/16x16/actions/spnewgame.png
%_datadir/apps/kspaceduel/icons/oxygen/16x16/actions/spnewround.png
%_datadir/apps/kspaceduel/icons/oxygen/16x16/actions/sppausegame.png
%_datadir/apps/kspaceduel/icons/oxygen/22x22/actions/spnewgame.png
%_datadir/apps/kspaceduel/icons/oxygen/22x22/actions/spnewround.png
%_datadir/apps/kspaceduel/icons/oxygen/22x22/actions/sppausegame.png
%_datadir/apps/kspaceduel/icons/oxygen/32x32/actions/spnewgame.png
%_datadir/apps/kspaceduel/icons/oxygen/32x32/actions/spnewround.png
%_datadir/apps/kspaceduel/icons/oxygen/32x32/actions/sppausegame.png

%_datadir/apps/lskat/grafix/default.rc
%_datadir/apps/lskat/grafix/default.svg

%_iconsdir/hicolor/scalable/apps/knetwalk.svgz
%_iconsdir/oxygen/16x16/actions/endturn.png
%_iconsdir/oxygen/16x16/actions/highscore.png
%_iconsdir/oxygen/16x16/actions/lastmoves.png
%_iconsdir/oxygen/16x16/actions/legalmoves.png
%_iconsdir/oxygen/22x22/actions/lastmoves.png
%_iconsdir/oxygen/22x22/actions/legalmoves.png
%_iconsdir/oxygen/32x32/actions/endturn.png
%_iconsdir/oxygen/32x32/actions/highscore.png
%_iconsdir/oxygen/32x32/actions/lastmoves.png
%_iconsdir/oxygen/32x32/actions/legalmoves.png
%_iconsdir/oxygen/48x48/actions/lastmoves.png
%_iconsdir/oxygen/48x48/actions/legalmoves.png
%_iconsdir/oxygen/scalable/actions/lastmoves.svgz
%_iconsdir/oxygen/scalable/actions/legalmoves.svgz

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
%dir %_docdir/HTML/en/kgoldrunner/
%doc %_docdir/HTML/en/kgoldrunner/*.bz2
%doc %_docdir/HTML/en/kgoldrunner/*.docbook
%doc %_docdir/HTML/en/kgoldrunner/*.png
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
%dir %_docdir/HTML/en/kspaceduel/
%doc %_docdir/HTML/en/kspaceduel/*.bz2
%doc %_docdir/HTML/en/kspaceduel/*.docbook
%doc %_docdir/HTML/en/kspaceduel/*.png
%dir %_docdir/HTML/en/ktuberling/
%doc %_docdir/HTML/en/ktuberling/*.png
%doc %_docdir/HTML/en/ktuberling/*.bz2
%doc %_docdir/HTML/en/ktuberling/*.docbook
%dir %_docdir/HTML/en/kwin4/
%doc %_docdir/HTML/en/kwin4/*.bz2
%doc %_docdir/HTML/en/kwin4/*.docbook
%dir %_docdir/HTML/en/ksquares/
%doc %_docdir/HTML/en/ksquares/index.cache.bz2
%doc %_docdir/HTML/en/ksquares/index.docbook
%dir %_docdir/HTML/en/kiriki/
%doc %_docdir/HTML/en/kiriki/*.bz2
%doc %_docdir/HTML/en/kiriki/*.docbook
%dir %_docdir/HTML/en/lskat/
%doc %_docdir/HTML/en/lskat/*.bz2
%doc %_docdir/HTML/en/lskat/*.docbook


%files -n %lib_name
%defattr(-,root,root,-)
#
#
%_libdir/libkdegames.so.*
#
%_libdir/libkmahjongglib.so.*
%_libdir/libkolflib.so.*
%_libdir/libksirtetlib.so.*


%files -n %lib_name-devel
%defattr(-,root,root,-)


%_datadir/apps/cmake/modules/FindLibKDEGames.cmake
%_datadir/apps/cmake/modules/GGZ.cmake
%_datadir/apps/cmake/modules/FindLibKSirtet.cmake

%_libdir/libkmahjongglib.so
%_libdir/libkolflib.so
%_libdir/libksirtetlib.so

%_includedir/*.h

%dir %_includedir/kgame/
%_includedir/kgame/*.h

%dir %_includedir/libksirtet/base/
%_includedir/libksirtet/base/*.h
%dir %_includedir/libksirtet/common/
%_includedir/libksirtet/common/*.h
%dir %_includedir/libksirtet/lib/
%_includedir/libksirtet/lib/*.h
%dir %_includedir/libksirtet/
%_includedir/libksirtet/libksirtet_export.h

%_includedir/KDE/KCardDialog
%_includedir/KDE/KChat
%_includedir/KDE/KChatBase
%_includedir/KDE/KChatDialog
%_includedir/KDE/KExtHighscore
%_includedir/KDE/KGame/*
%_includedir/KDE/KGameCanvas
%_includedir/KDE/KGameLCD
%_includedir/KDE/KGameMisc
%_includedir/KDE/KGameProgress
%_includedir/KDE/KGameSvgDigits
%_includedir/KDE/KGameSvgDocument
%_includedir/KDE/KGrid2D
%_includedir/KDE/KHighscore
%_includedir/KDE/KScoreDialog
%_includedir/KDE/KStandardGameAction
%dir %_includedir/digits/
%_includedir/digits/kgamesvgdigits.h

%_libdir/libkdegames.so

%dir %_datadir/config.kcfg/
%_datadir/config.kcfg/*.kcfg

